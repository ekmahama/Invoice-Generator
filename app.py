from flask import Flask, render_template, send_file
from datetime import datetime, timedelta
from weasyprint import HTML
app = Flask(__name__)


@app.route("/")
def invoice_generator():
    today = datetime.today()
    duedate = today + timedelta(15)
    invoice_number = 124

    from_address = {
        'company_name': 'Larkwor LLC',
        'addr1': '112 East Lindsay St',
        'addr2': 'NC 27401, Greensboro'
    }

    to_address = {
        'client_name': 'Edward Azeleor',
        'addr1': '123 Salem Stree',
        'addr2': 'NC 27401, Greensboro'
    }

    items = [
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
    rendered_pdf = html.write_pdf('./static/invoice.pdf')
    return send_file('./static/invoice.pdf')


if __name__ == '__main__':
    app.run()
