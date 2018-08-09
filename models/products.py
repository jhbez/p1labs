# -*- coding: utf-8 -*-
# © Jose Hernandez <jhbez@outlook.com>. All rights reserved.

from odoo import models, fields, api, _

TYPE_SALES = [
    ('prepaid', _("Prepaid")),
    ('plan', _("Plan")),
    ('activations', _("Activations")),
]


class P1labsProduct(models.Model):
    _name = 'p1labs.product'
    _rec_name = 'display_name'

    type_sale = fields.Selection(selection=TYPE_SALES, string=_("Type sale"), default='prepaid', required=True)
    product_id = fields.Many2one(comodel_name='product.product', string=_("Product"), domain=[('type', '=', 'product')])
    service_id = fields.Many2one(comodel_name='product.product', string=_("Service"), domain=[('type', '=', 'service')])
    display_name = fields.Char(compute='_compute_display_name')
    price = fields.Float(string=_("Price"), required=True)
    contract = fields.Integer(string=_("Contract"))
    # series_id = fields.Many2one(comodel_name='p1labs.product.series', string=_("Series"))
    stock_product_lot_id = fields.Many2one(comodel_name='stock.production.lot', string=_("Series"))
    warranty_id = fields.Many2one(comodel_name='p1labs.product.warranty', string=_("Warranty"))

    # @api.depends('type_sale', 'product_id', 'service_id')
    @api.multi
    def _compute_display_name(self):
        for row in self:
            if row.type_sale == 'prepaid':
                row.display_name = row.product_id.name
            elif row.type_sale == 'plan':
                row.display_name = row.service_id.name
            else:
                row.display_name = str(row.product_id.name) + " + " + str(row.service_id.name)


class P1labsProductWarranty(models.Model):
    _name = 'p1labs.product.warranty'
    _rec_name = 'name'

    name = fields.Char(string=_("Name"))

# class P1labsProductSeries(models.Model):
#    _name = 'p1labs.product.series'
#    _rec_name = 'name'

#    name = fields.Char(string=_("Name"))
