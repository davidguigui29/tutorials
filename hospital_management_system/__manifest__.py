# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",

    'summary': "",

    'description': """
    """,

    'author': "Guidasworld",
    'website': "https://www.guidasworld.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'sequence': 3,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/patient_views.xml",
        "views/menu.xml",
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    
    'license': "LGPL-3",
}

