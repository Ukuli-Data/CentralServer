from flask import Flask 
app = Flask(__name__) 
 
@app.route('/') 
def hello_world(): 
    return 'Hello to the World of Flask!' 
 
app = Flask(__name__, static_folder='./static/') 
# app.config.from_object('configuration.DevelopmentConfig') 

if __name__ == '__main__': 
    app.run() 
