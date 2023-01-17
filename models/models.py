# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class AgreementContract(models.Model):
  _name = 'agreement.contract'
  _description = 'agreement.contract'

  @api.model
  def create(self, vals):
    if vals.get('number', _('New')) == _('New'):
      vals['number'] = self.env['ir.sequence'].next_by_code('agreement.contract')
    return super().create(vals)

  # number = fields.Char('Номер', default=lambda self: _('New'), copy=False, readonly=True, tracking=True)
  number = fields.Char('Номер', default=lambda self: _('New'))
