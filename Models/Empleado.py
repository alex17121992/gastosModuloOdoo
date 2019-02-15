#-*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api

class Empleado(models.Model):
    _name = 'gastos.empleado'
    foto=fields.Binary()
    dni=fields.Char('Dni',required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    departamento  = fields.Many2one('gastos.departamento','Departamento')
    fechaNac=fields.Date('Fecha de Nacimento',default=datetime.now())

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res