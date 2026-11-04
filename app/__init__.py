from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicontrol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app import models
    

    from app.blueprints.medicos import bp_medicos
    from app.blueprints.pacientes import bp_pacientes
    from app.blueprints.citas import bp_citas
    
    app.register_blueprint(bp_medicos, url_prefix='/medicos')
    app.register_blueprint(bp_pacientes, url_prefix='/pacientes')
    app.register_blueprint(bp_citas, url_prefix='/citas')
    


    @app.route('/')
    def index():
        return "Bienvenido a MediControl - Sistema en línea"
        
    return app