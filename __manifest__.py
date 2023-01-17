# -*- coding: utf-8 -*-
{
    'name': "Agreement",
    'sequence': 1,
    'author': "Zaleusky Yauheny",
    'category': 'Marketing',
    'version': '0.1',

    'summary': """ Тестовое задание (Модуль "Договоры") """,
    'description': """
        Тестовое задание (Модуль "Договоры")
    """,

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3'
}
