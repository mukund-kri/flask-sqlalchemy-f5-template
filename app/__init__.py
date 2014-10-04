from flask import Flask


def create_app(app_type):

    app = Flask(__name__)
    if app_type == 'develop':
        app.config.from_object('app.settings.DevelopmentConfig')
    elif app_type == 'test':
        app.config.from_object('app.settings.TestingConfig')
    else:
        app.config.from_object('app.settings.ProductionConfig')
        

    # Configure the DB to config file just loades
    import models
    models.init_db(app)

    # register the blueprints to the app
    from home import homebp
    app.register_blueprint(homebp)

    
    # from books import bookbp
    # app.register_blueprint(bookbp)
    
    return app

