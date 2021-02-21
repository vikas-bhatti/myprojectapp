from flask import flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():



    return render_template('index.html',animal="", noise="")
if __name__ =="__main__": 