from flask import  request,redirect
import connexion
from connexion import request,FlaskApp

import pathlib




basedir = pathlib.Path(__file__).parent.resolve()
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route('/')
def home():
    return redirect('/api/ui/')






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)