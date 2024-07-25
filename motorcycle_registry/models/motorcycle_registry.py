import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _sql_constraints = [('vin_unique', 'UNIQUE(vin)', 'El vin no puede ser reutilizable')]
    _rec_name = "registry_number"


    certificate_title = fields.Binary(string = "Titulo de propiedad")
    current_mileage = fields.Float(string = "Millaje actual")
    vin = fields.Char(string = "VIN")
    first_name = fields.Char(string = "Nombre")
    last_name = fields.Char(string = "Apellido")
    license_plate = fields.Char(string = "Matrícula")
    registry_date = fields.Date(string = "Fecha de registro")
    registry_number = fields.Char(string = "Numero de Registro", required=True, copy=False, readonly=True,  default=lambda self:self.env['ir.sequence'].next_by_code('registry.number'))
    active = fields.Boolean(string = "Activo", default = True)

    #Nuevo campos
    make = fields.Char(string="Marca")
    model = fields.Char(string ="Modelo")
    year = fields.Char(string ="Año")
    battery_capacity = fields.Char(string ="Capacidad de Bateria")
    serial_number = fields.Char(string = "Numero de serie")
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    @api.constrains('license_plate')
    def _comprobar_matricula(self):
        pattern = r'^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$'
        for record in self.filtered(lambda r: r.license_plate):
            match = re.match(pattern, record.license_plate)
            if not match:
                raise ValidationError('La matricula NO cumple con la secuencia valida.')

    @api.constrains('vin')
    def _comprobar_vin(self):
            pattern = r'^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$'
            match = re.match(pattern, self.vin)
            if not match:
                raise ValidationError('El vin NO se cumple con la secuencia valida.')

    def action_test(self):
        return {
            "effect": {
                "fadeout": "slow",
                "message": 'Click para continuar',
                "type": "rainbow_man",
            }
        }
        
