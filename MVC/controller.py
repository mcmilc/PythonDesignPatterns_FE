from flask import redirect
from flask import render_template
from flask import request
from flask import Flask
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import NotFound

import model

app = Flask(__name__, template_folder="view")


@app.route("/")
def index():
    return render_template("main_page.html")


@app.route("/shorten/")
def shorten():
    # Validate user input
    full_url = request.args.get("url")
    if not full_url:
        raise BadRequest()

    # Model returns object with short_url property
    url_model = model.Url.shorten(full_url)
    if not url_model:
        raise NotFound()
    short_url = request.host + "/" + url_model.short_url
    return render_template("success.html", short_url=short_url)


@app.route("/<path:path>")
def redirect_to_full_path(path=""):
    print(f"Redirection path {path}")
    url_model = model.Url.get_by_short_url(path)
    if not url_model:
        raise NotFound()
    print(f"Retrieved full url: {url_model.full_url}")
    return redirect(url_model.full_url)


if __name__ == "__main__":
    app.run(debug=True)
