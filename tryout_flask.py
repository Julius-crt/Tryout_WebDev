from flask import Flask

#ein ligtw9ght Webdev framework ist Flask
#wir können einen server bauen
pp = Flask(__name__)

#routen 'dekorator'
@app.route("/")
def hello_worl():
    return "<p>Hello World da pui pui</p>"