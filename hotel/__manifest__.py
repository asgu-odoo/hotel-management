{
    'name' : 'Hotel Management',
    'version' : '1.0',
    'depends' : ['base', 'mail'],
    'description' : """Hotel Management System """,
    'application' : 'True',
    'data' : [
        'security/ir.model.access.csv',
        'views/hotel_room_views.xml',
        'views/hotel_menus.xml',
    ]
}
