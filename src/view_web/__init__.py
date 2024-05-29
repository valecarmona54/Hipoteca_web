"""
The flask application package.
"""

from flask import Flask, make_response
app = Flask(__name__)
app.secret_key = 'root'

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

import src.view_web.views
