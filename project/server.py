from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "Highly secret key"
user_input = []

#hardcoded, needs a better solution but this will do for now
