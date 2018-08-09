# -*- coding: utf-8 -*-
# © Jose Hernandez <jhbez@outlook.com>. All rights reserved.

from odoo import models, fields, api, _
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
        self.folio = self.env['ir.sequence'].get('p1labs.sales')
        self._set_workflow('confirmed')

    def _set_workflow(self, _state):
        self.state = _state


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
