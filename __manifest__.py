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

    'depends': ['base', 'mail'],

    'data': [
        'views/views.xml',
        'views/sequence.xml',
        'security/security.xml',
        'security/rules.xml',
        'security/cron.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3'
}
