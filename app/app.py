import os

import flask
import db
import auth
import blog


def create_app():
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "lookersdk-flask.sqlite"),
    )



    # Initialize app and register our blueprints
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=8080, debug=False, ssl_context='adhoc')
    # Cloud Run/ App Engine settings
    #server_port = os.environ.get('PORT', '8080')
    #app.run(debug=False, port=server_port, host='0.0.0.0')
