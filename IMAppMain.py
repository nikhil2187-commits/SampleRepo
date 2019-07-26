from flask import Flask,Blueprint
from flaskConfig import *
from subCompRoutes import *
from routesMain import *
from commonModules.adminController import *
from commonModules.adminRoute import *
from commonModules.commonRoute import *
from commonModules.dataIngestionController import *
from commonModules.loginController import *
from commonModules.preprocessingController import *
from main import *
from flask_cors import CORS
from commonModules.UserDataPreprocessDb import *
from flask_sqlalchemy import SQLAlchemy
from flask_mongoalchemy import MongoAlchemy

def create_app():
    app = Flask(__name__)
    params = urllib.parse.quote_plus('Driver={%s};''Server=%s;''Database=%s;'%(DRIVER_NAME,SQL_SERVERNAME,SQL_DBNAME))
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.secret_key = SECRETKEY
    app.config['MONGOALCHEMY_DATABASE'] = DATABASENAME
    app.config['MONGOALCHEMY_PORT'] = DATBASEPORT
    CORS(app)
    db.init_app(app)
    dbs.init_app(app)    
    app.register_blueprint(NPS)
    app.register_blueprint(NpsRoutes)
    app.register_blueprint(subCompRoutes)
    app.register_blueprint(adminController)
    app.register_blueprint(adminRoutes)
    app.register_blueprint(commonRoutes)
    app.register_blueprint(dataIngestion)
    app.register_blueprint(loginController)
    app.register_blueprint(preProcessingController)
    return app 
if __name__ == '__main__':
    app = create_app()
    app.run(host=RUNHOST, port=RUNNINGPORT, debug=True)