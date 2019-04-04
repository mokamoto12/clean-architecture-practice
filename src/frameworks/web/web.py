import json
from typing import Tuple

from flask import Flask, redirect, url_for
from werkzeug.wrappers import Response

from src.interfaceadapters.controllers.controller import Controller
from src.interfaceadapters.presenters.presenter import View
from src.registry import controller
from src.usecases.exceptions import ResourceNotFound

app = Flask(__name__)


@app.route('/')
def index() -> Response:
    return redirect(url_for('show', timezone='UTC'))


@app.route('/<timezone>')
def show(timezone: str) -> str:
    c: Controller
    view: View
    c, view = controller()
    c.show(timezone)
    if view.buffer is None:
        raise Exception()

    return view.buffer()


@app.errorhandler(ResourceNotFound)
def resource_not_found(error: ResourceNotFound) -> Tuple[str, int]:
    return json.dumps({'message': error.message}), 404


@app.errorhandler(Exception)
def exception(_: Exception) -> Tuple[str, int]:
    return json.dumps({'message': 'internal server error.'}), 500
