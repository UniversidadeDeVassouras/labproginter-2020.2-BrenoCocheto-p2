from flask import Flask, render_template
import os

app = Flask(
    __name__,
    static_folder=os.path.abspath("application/view/static"),
    template_folder=os.path.abspath("application/view/templates"),
)

from application.controller.home_controller import home
from application.controller.subject_controller import subject
