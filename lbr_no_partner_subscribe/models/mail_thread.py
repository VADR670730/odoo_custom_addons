from odoo import api, fields, models
from odoo.http import request


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _message_subscribe(self, partner_ids=None, channel_ids=None, subtype_ids=None, customer_ids=None):
        # Don't add partners as a followers for next models:
        if self._name in ['sale.order', 'purchase.order', 'crm.lead', 'project.project', 'project.task']:
            if partner_ids:
                users = request.env['res.users'].search([('partner_id', 'in', partner_ids)])
                # Only add contact as a follower if it has a assigned Odoo user
                partner_ids = users.mapped('partner_id').ids if users else []
        # Call to super with modified 'partner_ids' list
        return super(MailThread, self)._message_subscribe(
            partner_ids=partner_ids, channel_ids=channel_ids, subtype_ids=subtype_ids, customer_ids=customer_ids)
