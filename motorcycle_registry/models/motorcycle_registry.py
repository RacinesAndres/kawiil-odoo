from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

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
    registry_number = fields.Char(string = "Numero de Registro", default="MRN0004", required=True, copy=False, readonly=True)
    active = fields.Boolean(string = "Activo", default = True)
    
    make = fields.Char(string="Marca")
    model = fields.Char(string ="Modelo")
    year = fields.Integer(string ="Año")
    battery_capacity = fields.Char(string ="Capacidad de Bateria")
    
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)
        
    @api.constrains('license_plate')
    def _comprobar_matricula(self):
        for record in self:
            match = re.match('^[A-Z]{1,3}{1,4}[A-Z]{0,2}$', record.license_plate)
            if match == None:
                raise ValidationError('La matricula NO cumple con la secuencia valida.')

    @api.constrains('vin')
    def _comprobar_vin(self):
            match = re.match('^[A-Z]{4}{2}[A-Z0-9]{2}{5}$', self.vin)
            if match == None:
                raise ValidationError('El vin NO se cumple con la secuencia valida.')

    def action_test(self):
        return {
            "effect": {
                "fadeout": "slow",
                "message": 'Click para continuar',
                "type": "rainbow_man",
            }
        }