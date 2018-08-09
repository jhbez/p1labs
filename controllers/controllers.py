# -*- coding: utf-8 -*-
# © Jose Hernandez <jhbez@outlook.com>. All rights reserved.
from odoo import http

# class Msc-client/p1labs(http.Controller):
#     @http.route('/msc-client/p1labs/msc-client/p1labs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/msc-client/p1labs/msc-client/p1labs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('msc-client/p1labs.listing', {
#             'root': '/msc-client/p1labs/msc-client/p1labs',
#             'objects': http.request.env['msc-client/p1labs.msc-client/p1labs'].search([]),
#         })

#     @http.route('/msc-client/p1labs/msc-client/p1labs/objects/<model("msc-client/p1labs.msc-client/p1labs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('msc-client/p1labs.object', {
#             'object': obj
#         })