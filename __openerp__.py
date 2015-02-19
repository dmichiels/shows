# -*- coding: utf-8 -*-
{
    'name': "shows",

    'summary': """
        Manage the different shows""",

    'description': """
        Manage the different shows
    """,

    'author': "Scratch",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Apps',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'stages.xml',
        'templates.xml',
        'views/shows.xml',
        'views/stage.xml',
        'views/spectacle.xml',
        'views/users.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
