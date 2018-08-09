# -*- coding: utf-8 -*-
# © Jose Hernandez <jhbez@outlook.com>. All rights reserved.
{
    'name': "P1labs",

    'description': """
        Three sales 
    """,

    'author': "Jose Hernandez",
    'website': "https://github.com/jhbez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menus.xml',
        'views/products.xml',
        'views/sales.xml',
        'data/sequence.xml',
        #'data/p1labs.product.series.csv',
        'data/p1labs.product.warranty.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        ##'demo/demo.xml',
    ],
}