#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template

app = Flask(__name__)

my_name = "Patrik Karlsson"
my_course = "OOPython"

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html", name=my_name, course=my_course)

if __name__ == "__main__":
    app.run()
