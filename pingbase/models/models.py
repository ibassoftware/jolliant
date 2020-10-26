from odoo import models, fields, api
from odoo.models import AbstractModel


class PubWarrantyOverride(AbstractModel):
    
    _inherit = 'publisher_warranty.contract'
    
    def update_notification(self, cron_mode=True):
        
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('database.expiration_date', '2050-10-10')
        set_param('database.expiration_reason', 'demo')
        set_param('database.enterprise_code', 'exc123abc')
        
        return True