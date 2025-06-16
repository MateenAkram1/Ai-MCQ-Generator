from flask import Flask, request, render_template, send_file

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)