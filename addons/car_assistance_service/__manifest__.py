# -*- coding: utf-8 -*-
{
    'name': "Asistencia y Servicio de Autos",

    'summary': """
        Gestión de asistencia y reparación de vehículos en talleres.
        """,

    'description': """
        Este módulo permite gestionar la asistencia y reparación de vehículos en talleres mecánicos.  
    Incluye funcionalidades como:  
    - Registro de vehículos y clientes.  
    - Gestión de órdenes de reparación.  
    - Seguimiento del estado de las reparaciones.  
    - Control de inventario de repuestos utilizados.  
    - Generación de reportes sobre reparaciones y servicios.  

    Ideal para talleres mecánicos que buscan optimizar sus operaciones y ofrecer un mejor servicio a sus clientes.

    """,

    'author': "bitsis.gt",
    'website': "https://www.bitsis.gt",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/bas
    # e/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/order_service_car_views.xml",
        "views/order_service_stages_views.xml"
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
