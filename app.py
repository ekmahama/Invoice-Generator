from flask import Flask, render_template, send_file, request
from datetime import datetime, timedelta
from weasyprint import HTML, CSS
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def invoice_generator():
    today = datetime.today()
    posted_data = request.get_json() or {}
    duedate = today + timedelta(15)

    defualt_data = {
        "invoice_number": 124,

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
                'charge': 200
            },
            {
                'name': 'Hosting',
                'charge': 150
            },
            {
                'name': 'Domain Name',
                'charge': 1000
            }
        ]
    }

    invoice_number = posted_data.get(
        "invoice_number", defualt_data["invoice_number"])
    from_address = posted_data.get(
        "from_address", defualt_data["from_address"])
    to_address = posted_data.get("to_address", defualt_data["to_address"])
    items = posted_data.get("items", defualt_data["items"])
    total = sum([i['charge'] for i in items])

    rendered = render_template('invoice.html',
                               today=today.strftime("%B %-d, %Y"),
                               duedate=duedate.strftime("%B %-d, %Y"),
                               invoice_number=invoice_number,
                               from_address=from_address,
                               to_address=to_address,
                               items=items,
                               total=total)

    html = HTML(string=rendered)
    # print(rendered)
    css = CSS('./static/css/style.css')
    rendered_pdf = html.write_pdf(
        './static/invoice.pdf', stylesheets=[css])
    return send_file('./static/invoice.pdf')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()
