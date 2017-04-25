from flask import Flask

__author__ = 'denz alovera'

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1> hello world! </h1>'

if __name__ == '__main__':
    app.run()
