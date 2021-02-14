from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def invoice_generator():
    return render_template('invoice.html')


if __name__ == '__main__':
    app.run()
