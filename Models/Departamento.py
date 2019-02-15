#-*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api

class Departamento(models.Model):
    _name = 'gastos.departamento'
    codigo = fields.Integer('Codigo', default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    nombre = fields.Char('Nombre', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res