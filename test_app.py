import requests
from flask import Flask, render_template, send_file
data = {
    "invoice_number": 126,

    "from_address": {
        'company_name': 'Larkwor LLC',
        'addr1': '112 East Lindsay St',
        'addr2': 'NC 27401, Greensboro'
    },

    "to_address": {
        'client_name': 'Edward Azeleor',
        'addr1': '123 Salem Stree',
        'addr2': 'NC 27401, Greensboro'
    },

    "items": [
        {
            'name': 'Web Design',
            'charge': 400
        },
        {
            'name': 'Hosting',
            'charge': 151
        },
        {
            'name': 'Domain Name',
            'charge': 1222
        }
    ]
}

url = 'http://127.0.0.1:5000/'

html = requests.post(url, json=data)
with open('invoice_test.pdf', 'wb') as f:
    f.write(html.content)
