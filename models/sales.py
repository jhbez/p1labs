# -*- coding: utf-8 -*-
# © Jose Hernandez <jhbez@outlook.com>. All rights reserved.

from odoo import models, fields, api, _, exceptions
from . import products


class P1labsSale(models.Model):
    _name = 'p1labs.sale'
    _rec_name = 'folio'

    state = fields.Selection(selection=[('draft', _("Draft")), ('confirmed', _("Confirmed"))], default='draft')
    date = fields.Datetime(string=_("Date"), default=lambda self: fields.datetime.now(), required=True)
    folio = fields.Char(string=_("Folio"), readonly=True, default=' /')
    partner_id = fields.Many2one(comodel_name='res.partner', string=_("Partner"), required=True)
    picking_type_id = fields.Many2one(comodel_name='stock.picking.type', string=_("Operation"), required=True,
                                      domain=[('code', '=', 'outgoing')])
    sale_line_ids = fields.One2many('p1labs.sale.line', 'p1labs_sale_id', string=_("Products"))
    amount = fields.Float(string=_("Total"), compute='_set_amount', readonly=True)

    location_id = fields.Many2one('stock.location', _("Source Location"))
    location_dest_id = fields.Many2one('stock.location', _("Destination Location"))
    stock_picking_id = fields.Many2one('stock.picking', _("Stock picking"), readonly=True)

    @api.depends('sale_line_ids')
    @api.onchange('sale_line_ids')
    @api.multi
    def _set_amount(self):
        for row in self:
            row.amount = 0
            for product in row.sale_line_ids:
                row.amount += product.price

    @api.multi
    def action_validate(self):
        self.ensure_one()
        if self.validation(_type='stock'):
            self.folio = self.env['ir.sequence'].next_by_code('p1labs.sales')
            if self.stock_picking():
                self._set_workflow('confirmed')
                if self.stock_picking_id:
                    return {
                        'name': _("Stock picking"),
                        'type': 'ir.actions.act_window',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'stock.picking',
                        'target': 'current',
                        'res_id': self.stock_picking_id.id,
                        #    'context': self.env._ctx
                    }

    def _set_workflow(self, _state):
        self.state = _state

    @api.model
    def validation(self, _type):
        if _type == 'stock':
            product_list = {}
            for product in self.sale_line_ids:
                if product.type_sale != 'plan':
                    code = str(product.product_id.product_id.id) + "-" + \
                           str(self.location_id.id) + "-" + \
                           str(product.product_id.stock_product_lot_id.id)

                    if code in product_list:
                        p = product_list.get(code)
                        p.update({'qty': p.get('qty') + 1})
                    else:
                        product_list.update(
                            {code: {'qty': 1, 'p': product.product_id.product_id,
                                    'l': product.product_id.stock_product_lot_id}})
            for p in product_list:
                product = product_list.get(p)
                stock = self.env['stock.quant']._get_available_quantity(
                    product.get('p'),
                    self.location_id,
                    product.get('l'))
                if stock < product.get('qty'):
                    raise exceptions.ValidationError(msg=_("Product: %s  Lot: %s Stock: %s  Required: %s" % (
                        product.get('p').name,
                        product.get('l').name,
                        stock,
                        product.get('qty'))))
        return True

    @api.model
    def stock_picking(self):
        vals = {
            'location_dest_id': self.location_dest_id.id,
            'company_id': self.env.user.company_id.id,
            'picking_type_id': self.picking_type_id.id,
            'location_id': self.location_id.id,
            'owner_id': False,
            'move_type': 'direct',
            'move_lines': self.move_lines(),
            'priority': '1',
            'is_locked': True,
            'partner_id': self.partner_id.id,
            'origin': self.folio}
        if len(vals.get('move_lines')):
            self.stock_picking_id = self.env['stock.picking'].create(vals=vals)
        # self.stock_picking_id.action_done()
        return True

    @api.model
    def move_lines(self):
        lines = []
        for product in self.sale_line_ids:
            if product.type_sale != 'plan':
                p = [0, False, {
                    'location_dest_id': self.location_dest_id.id,
                    'product_uom': product.product_id.product_id.uom_id.id,
                    'name': product.product_id.product_id.name,
                    'picking_type_id': self.picking_type_id.id,
                    'location_id': self.location_id.id,
                    'quantity_done': 1,
                    # 'lot_id': product.product_id.stock_product_lot_id.id,
                    # 'lot_name': product.product_id.stock_product_lot_id.name,
                    'date_expected': str(fields.datetime.now()),
                    'product_id': product.product_id.product_id.id,
                    'additional': False,
                    'state': 'draft'}]
                lines.append(p)
        return lines

    @api.onchange('picking_type_id', 'partner_id')
    def location(self):
        if self.picking_type_id:
            if self.picking_type_id.default_location_src_id:
                location_id = self.picking_type_id.default_location_src_id.id
            elif self.partner_id:
                location_id = self.partner_id.property_stock_supplier.id
            else:
                customerloc, location_id = self.env['stock.warehouse']._get_partner_locations()

            if self.picking_type_id.default_location_dest_id:
                location_dest_id = self.picking_type_id.default_location_dest_id.id
            elif self.partner_id:
                location_dest_id = self.partner_id.property_stock_customer.id
            else:
                location_dest_id, supplierloc = self.env['stock.warehouse']._get_partner_locations()
            self.location_id = self.env['stock.location'].browse(location_id)
            self.location_dest_id = self.env['stock.location'].browse(location_dest_id)
            return {'domain': {'location_id': [('id', '=', self.location_id.id)],
                               'location_dest_id': [('id', '=', self.location_dest_id.id)]}}


class P1LabsSaleLines(models.Model):
    _name = 'p1labs.sale.line'

    p1labs_sale_id = fields.Many2one(comodel_name='p1labs.sale', required=True, ondelete='cascade')
    product_id = fields.Many2one(comodel_name='p1labs.product', required=True)
    type_sale = fields.Selection(selection=products.TYPE_SALES, related='product_id.type_sale', readonly=True)
    price = fields.Float(string=_("Price"))

    @api.depends('product_id')
    @api.onchange('product_id')
    @api.multi
    def _set_price(self):
        for row in self:
            row.price = row.product_id.price
