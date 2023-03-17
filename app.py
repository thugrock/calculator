from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import math
from logging.config import dictConfig
import logging
import test_app

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sqrt', methods=['POST'])
def square_root():
    number = float(request.form['number'])
    result = math.sqrt(number)
    app.logger.critical("number is "+str(number)+", operation is square root, result is "+str(result))
    return render_template('result.html', operation='Square Root', number=number, result=result)

@app.route('/ln', methods=['POST'])
def natural_logarithm():
    number = float(request.form['number'])
    result = math.log(number)
    app.logger.critical("number is "+str(number)+", operation is natural logarithm, result is "+str(result))
    return render_template('result.html', operation='Natural Logarithm', number=number, result=result)

@app.route('/pow', methods=['POST'])
def power():
    number = float(request.form['number'])
    exponent = float(request.form['exponent'])
    result = math.pow(number, exponent)
    app.logger.critical("number is "+str(number)+", exponent is "+str(exponent)+", operation is power, result is "+str(result))
    return render_template('result.html', operation='Power', number=number, exponent=exponent, result=result)

@app.route('/fact', methods=['POST'])
def factorial():
    number = int(request.form['number'])
    result = math.factorial(number)
    app.logger.critical("number is "+str(number)+" operation is factorial, result is "+str(result))
    return render_template('result.html', operation='Factorial', number=number, result=result)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": '%(asctime)s "%(name)s" %(levelname)s "%(funcName)s" "%(lineno)d" "%(message)s"',
            }
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "filename": "logs/flask.log",
                "formatter": "default",
            },
        },
        "root": {"level": "CRITICAL", "handlers": ["file"]},
    }
)
if __name__ == '__main__':
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.CRITICAL)
    app.run(debug=True, host="0.0.0.0", port=13962)
    test_app()
