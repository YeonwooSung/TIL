from flask import Flask


class FlaskAppWrapper(object):

    def __init__(self, app, **configs):
        self.app = app
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)



def action():
    """ Function which is triggered in flask app """
    return "Hello World"



if __name__ == "__main__":
    flask_app = Flask(__name__)
    app = FlaskAppWrapper(flask_app)
    # Add endpoint for the action function
    app.add_endpoint('/action', 'action', action, methods=['GET'])
    app.run(debug=True)
