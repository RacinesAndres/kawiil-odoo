{
    'name': 'Motorcycle Registry',
    'version': '0.0.1',
    'author': 'Andres Racines',
    'sequence': -100,
    'category': 'Custom Module/Kawiil',
    'summary': 'Manage Registration of Motorcycles',
    'description': """Motorcycle Registry 
    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of 
        the brand""",
    'license': 'OPL-1',
    'depensds': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'security/motorcycle_registry.xml',
        'views/motorcycle_registry_menuitems.xml',
    ],
    'demo': ['demo/motorcycle_registry_demo.xml'],
    'application': True,
    'auto_install': False,
    'website': 'https://github.com/RacinesAndres/kawiil-odoo-academy/tree/17.0-motorcycle-registry',
}
