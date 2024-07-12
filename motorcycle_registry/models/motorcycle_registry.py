from odoo import models, fields

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"

    certificate_title = fields.Binary(string = "Titulo de propiedad")
    current_mileage = fields.Float(string = "Millaje actual")
    first_name = fields.Char(string = "Nombre", required = True)
    last_name = fields.Char(string = "Apellido", required = True)
    license_plate = fields.Char(string = "Matrícula")
    registry_date = fields.Date(string = "Fecha de registro")
    registry_number = fields.Char(string = "Nombre de Registro", required = True)
    active = fields.Boolean(string = "Activo", default = True)