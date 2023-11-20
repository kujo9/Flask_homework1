from flask import Flask 
from flask_migrate import Migrate 
from flask_cors import CORS 
from flask_jwt_extended import JWTManager 




from .blueprints.site.routes import site 
from .blueprints.auth.routes import auth
from config import Config 
from .models import login_manager, db 
from .helpers import JSONEncoder 


app = Flask(__name__) 
app.config.from_object(Config)
jwt = JWTManager(app) 


login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in'
login_manager.login_message = "Hey you! Log in please!"
login_manager.login_message_category = 'warning'





app.register_blueprint(site)
app.register_blueprint(auth)


#instantiating our datbase & wrapping our app
db.init_app(app)
migrate = Migrate(app, db)
app.json_encoder = JSONEncoder  #we are not instantiating an object we are simply pointing to this class we made when we need to encode data objects
#add this ^^^^^^^^^^
cors = CORS(app) #Cross Origin Resource Sharing aka allowing other apps to talk to our flask app/server
#add this ^^^^^^^^^^