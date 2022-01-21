from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '84jf-02+kdfm3s?2fs6n'

    return app