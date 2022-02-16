from flask_app import app
import os
print( os.environ.get("FLASK_APP_API_KEY"))
from flask_app.controllers import controller_users, controller_players

if __name__=="__main__":
    app.run(debug=True)