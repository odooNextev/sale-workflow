# Copyright 2023 Nextev
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends("payment_term_id")
    def _compute_general_discount(self):
        for so in self:
            so.general_discount = so.payment_term_id.sale_discount