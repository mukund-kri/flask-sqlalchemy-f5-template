from flask import Flask


def create_app(app_type, *args):

    app = Flask(__name__.split(".")[0])
    if app_type == 'develop':
        app.config.from_object('config.DevelopmentConfig')
    elif app_type == 'test':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.ProductionConfig')
        

    # Configure the DB to config file just loades
    import models
    models.init_db(app)

    # register the blueprints to the app    
    import config
                     
    for bp in config.REGISTERED_BLUEPRINTS:
        app.register_blueprint(bp)

    
    return app

