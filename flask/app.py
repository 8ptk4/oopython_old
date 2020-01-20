#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from person import Person
import handler
from flask import Flask, render_template, request


# born-date must be in format yyyy-mm-dd
person1 = Person("Patrik", "Karlsson", "1984-04-09", "OOPython", "pig.png")

app = Flask(__name__)

@app.route("/")
def main():
    """ Main route """
    return render_template(
        "index.html",
        course=person1.course,
        img=person1.image(),
        age=person1.age(),
        name=person1.name()
    )

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html", course=person1.course)

@app.route("/redovisning")
def redovisning():
    """ Report route """
    return render_template("redovisning.html", course=person1.course)

@app.route("/shape", methods=["POST", "GET"])
def shape():
    """ Shape route """

    if request.method == "POST":
        handler.create_objects(request.form)

    return render_template(
        "shape.html",
        shapes=handler.get_shapes(),
        course=person1.course,
        message=handler.get_message()
    )

@app.route("/show_shape")
def show_shape():
    """ Show Shape route """
    return render_template(
        "show_shape.html",
        course=person1.course,
        shapes=handler.get_shapes()
    )


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
