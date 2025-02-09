{
    'name': "Klinik",
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'author': "naura",
    'category': 'Klinik',
    'description': """
    HI!
    """,
    'sequence' : -1000,

    'data': [
        
        'views/patient_views.xml',
        'views/medical_record_views.xml',
        'reports/patient_report.xml',
        'views/menu.xml',
        
        'security/ir.model.access.csv'
        
    ],

    'demo': [
        
    ],

    'installable' : True,
    'application' : True,
}