#-*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api

class Ingresos(models.Model):
    _name = 'gastos.ingresos'
    codigo = fields.Integer('Codigo',default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    concepto = fields.Char('Concepto', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    cantidad = fields.Float('Cantidad', required=True)
    fecha = fields.Date('Fecha del ingreso',default=datetime.now())
    empleado = fields.Many2one('gastos.empleado', 'Empleado')

