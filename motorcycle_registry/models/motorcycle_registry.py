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
    # first_name = fields.Char(string = "Nombre")
    # last_name = fields.Char(string = "Apellido")
    license_plate = fields.Char(string = "Matrícula")
    registry_date = fields.Date(string = "Fecha de registro")
    registry_number = fields.Char(string = "Numero de Registro", required=True, copy=False, readonly=True,  default=lambda self:self.env['ir.sequence'].next_by_code('registry.number'))
    active = fields.Boolean(string = "Activo", default = True)

    #Nuevo campos
    make = fields.Char(string="Marca", compute= "_compute_from_vin")
    model = fields.Char(string ="Modelo", compute= "_compute_from_vin")
    year = fields.Char(string ="Año", compute= "_compute_from_vin")

    #Campos Propietario
    owner_id = fields.Many2one(comodel_name="res.partner", ondelete="restrict", string = "Propietario")
    owner_phone = fields.Char(related="owner_id.phone", string="Telefono")
    owner_email = fields.Char(related="owner_id.email", string="Correo Electronico")
    
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
                raise ValidationError('La matricula NO cumple con la secuencia valida Ej: KJA123')
                

    @api.constrains('vin')
    def _comprobar_vin(self):
        pattern = r'^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$'
        for record in self.filtered(lambda r: r.vin):
            match = re.match(pattern, record.vin)
            if not match:
                raise ValidationError('El vin NO se cumple con la secuencia valida Ej: KAIN220M00001')
            if not record.vin[0:2] == "KA":
                raise ValidationError('Oops No se cumple')
                

    @api.depends('vin')
    def _compute_from_vin(self):
        registries_with_vin = self.filtered(lambda r: r.vin)
        registries_with_vin._comprobar_vin()
        for registry in registries_with_vin:
            registry.make = registry.vin[:2]
            registry.model = registry.vin[2:4]
            registry.year = registry.vin[4:6]
        for registry in (self - registries_with_vin):
            registry.make = False
            registry.model = False
            registry.year = False        
