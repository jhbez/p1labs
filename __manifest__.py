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
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       ## 'views/views.xml',
     ##   'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        ##'demo/demo.xml',
    ],
}