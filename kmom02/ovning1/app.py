#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template, request
import handler

app = Flask(__name__)

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")


@app.route("/company", methods=["POST", "GET"])
def company():
    """ Company route"""

    if request.method == "POST":
        handler.add_employee(request.form)

    return render_template("company.html", persons=handler.get_persons())

if __name__ == "__main__":
    app.run()
