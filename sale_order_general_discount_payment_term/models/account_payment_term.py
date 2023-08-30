from odoo import fields, models


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    sale_discount = fields.Float(
        store=True,
        readonly=False,
    )
