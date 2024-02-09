from odoo import fields, models

class hotelRoom(models.Model):
    _name = "hotel.room"
    _description = "Hotel Room Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    code = fields.Char(string="Room Code", default="RC/AC-00", required=True)
    description = fields.Text()
    type = fields.Selection(
        selection = [('ac_room', 'AC Room'), ('non_ac_room', 'Non AC Room')],
        string = "Room Type",
        default = "non_ac_room",
    )
    is_available = fields.Boolean(string = "Available", default=True)
    floor = fields.Integer(string ="Floor Number")
    price = fields.Integer(string = "Price (in Rupees)", required=True)
    capacity = fields.Selection(
        selection = [('single', 'Single Bed'),
                     ('double', "Double Bed"),
                     ('four', "Group of Four"),
                     ('five', 'Group of Five')],
        default='single',
        required=True
    )
