# -*- coding: utf-8 -*-
# © Jose Hernandez <jhbez@outlook.com>. All rights reserved.

from odoo import models, fields, api

# class msc-client/p1labs(models.Model):
#     _name = 'msc-client/p1labs.msc-client/p1labs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100