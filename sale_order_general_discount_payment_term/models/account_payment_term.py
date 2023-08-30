from odoo import api, exceptions, fields, models, _
from odoo.exceptions import UserError, ValidationError

from dateutil.relativedelta import relativedelta


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"   

    sale_discount = fields.Float(
            # compute="_compute_discount",
            store=True,
            readonly=False,
        )