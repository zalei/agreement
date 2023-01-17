# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class AgreementContract(models.Model):
  _name = 'agreement.contract'
  _description = 'Договоры'

  def send_for_approval(self):
    self.state = 'for_approval'

  def do_enabled(self):
    self.state = 'enabled'

  def submit_for_revision(self):
    self.state = 'draft'

  @api.model
  def create(self, vals):
    if vals.get('number', _('New')) == _('New'):
      vals['number'] = self.env['ir.sequence'].next_by_code('agreement.contract')
    return super().create(vals)

  number = fields.Char('Номер', default=lambda self: _('New'), copy=False, readonly=True, tracking=True)
  partner_id = fields.Many2one('res.partner', string='Клиент', required=True, ondelete='restrict')
  kind_id = fields.Many2one('agreement.contract.type', string='Вид договора', required=True)
  state = fields.Selection([('draft', 'Черновик'),
                            ('for_approval', 'На согласовании'),
                            ('enabled', 'Активен'),
                            ('closed', 'Завершен')], string='Статус', default='draft', required=True)

  start_date = fields.Date('Дата начала', required=True)
  end_date = fields.Date('Дата завершения', required=True)

  author_id = fields.Many2one('res.users', string='Автор', default=lambda self: self.env.user, required=True)


class AgreementContractType(models.Model):
  _name = 'agreement.contract.type'
  _description = 'Справочник “Виды договоров”'
  _sql_constraints = [
        ('contract_type_name_uniq', 'UNIQUE (name)',
         'Внимание! Такое название вида договора уже есть!'),
    ]

  name = fields.Char('Название', required=True)
  active = fields.Boolean('Активно', default=True)