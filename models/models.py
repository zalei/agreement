# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class AgreementContract(models.Model):
  _name = 'agreement.contract'
  _description = 'Договоры'
  _inherit = ['mail.thread', 'mail.activity.mixin']

  def send_for_approval(self):
    self.state = 'for_approval'

  def do_enabled(self):
    self.state = 'enabled'

  def submit_for_revision(self):
    self.state = 'draft'

    message = f"Договор [{self.number}] отправлен на доработку"
    channel = self.env['mail.channel'].channel_get(
      [self.author_id.partner_id.id])
    channel_id = self.env['mail.channel'].browse(channel["id"])
    channel_id.message_post(
      body=(message),
      message_type='notification',
      subtype_xmlid='mail.mt_note',
    )


  @api.model
  def create(self, vals):
    if vals.get('number', _('New')) == _('New'):
      vals['number'] = self.env['ir.sequence'].next_by_code('agreement.contract')
    return super().create(vals)

  number = fields.Char('Номер', default=lambda self: _('New'), copy=False, readonly=True, tracking=True)
  partner_id = fields.Many2one('res.partner', string='Клиент', required=True, ondelete='restrict', tracking=True)
  kind_id = fields.Many2one('agreement.contract.type', string='Вид договора', required=True, tracking=True)
  state = fields.Selection([('draft', 'Черновик'),
                            ('for_approval', 'На согласовании'),
                            ('enabled', 'Активен'),
                            ('closed', 'Завершен')], string='Статус', default='draft', required=True, tracking=True)

  start_date = fields.Date('Дата начала', required=True, tracking=True)
  end_date = fields.Date('Дата завершения', required=True, tracking=True)

  author_id = fields.Many2one('res.users', string='Автор', default=lambda self: self.env.user,
                              required=True, tracking=True)

  def do_auto_close_contracts(self):
    close_contract_ids = self.env['agreement.contract'].search([('state', '=', 'enabled'),
                                                                ('end_date', '<=', fields.Date.today())])
    for contract_id in close_contract_ids:
      contract_id.state = 'closed'


class AgreementContractType(models.Model):
  _name = 'agreement.contract.type'
  _description = 'Справочник “Виды договоров”'
  _inherit = ['mail.thread', 'mail.activity.mixin']
  _sql_constraints = [
        ('contract_type_name_uniq', 'UNIQUE (name)',
         'Внимание! Такое название вида договора уже есть!'),
    ]

  name = fields.Char('Название', required=True, tracking=True)
  active = fields.Boolean('Активно', default=True, tracking=True)