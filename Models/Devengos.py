#-*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api

class Devengos(models.Model):
    _name = 'gastos.devengos'
    codigo=fields.Integer('Codigo',default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    concepto = fields.Char('Concepto', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    producto  = fields.Char('Producto', required=True)
    precio = fields.Float('Precio', required=True)
    cantidad=fields.Integer('Cantidad',required=True)
    fecha=fields.Date('Fecha del gasto',default=datetime.now())
    empleado=fields.Many2one('gastos.empleado','Empleado')



