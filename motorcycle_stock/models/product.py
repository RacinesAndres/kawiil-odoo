from odoo import api, fields, models

class Product(models.Model):
    _inherit = 'product.template'

    horsepower = fields.Float(string="Caballos de fuerza")
    top_speed = fields.Float(string="Velocidad maxima")
    torque = fields.Float(string="Torque")
    battery_capacity =  fields.Selection(selection=[
        ('xs', 'Small'),
        ('0m', 'Medium'),
        ('0l', 'Large'),
        ('xl', 'Extra Large')], copy=False, string="Capacidad de Bateria")
    charge_time = fields.Float(string="Tiempo de carga")
    range = fields.Float(string="Rango")
    curb_weight = fields.Float(string="Peso")
    make = fields.Char(string="Marca")
    model = fields.Char(string="Modelo")
    year = fields.Char(string="Año")
    launch_date = fields.Date()

    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle')], ondelete={'motorcycle': 'set product'})

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping
    
    
    