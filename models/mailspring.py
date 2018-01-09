# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MailSpring(models.Model):
    _name = 'mailspring'

    @api.model
    def get_stats(self, email):

        partner = self.env['res.partner'].search([('email', '=', email)])

        leads = self.env['crm.lead'].search_count([('partner_id.id', '=', partner.id), ('stage_id.name', '=', 'New')])

        if partner.currency_id.position == 'after':
            total_invoiced = str(partner.total_invoiced) + str(partner.currency_id.symbol)
        else:
            total_invoiced = str(partner.currency_id.symbol) + str(partner.total_invoiced)

        if not partner:
            return {'exist': 0}

        return {'exist': 1, 'leads': leads, 'name': partner.name, 'total_invoiced': total_invoiced}
