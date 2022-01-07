# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Practice',
    'version' : '1.0',
    'summary': 'Learning module in odoo',
    'sequence': -100,
    'description': "",
    'category': 'Productivity',
    'depends' : ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale.xml'
        
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
