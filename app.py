from flask import Flask, jsonify, request
from Statistics.t_test import Independent
from resources.t_test_re import t_blueprint
from resources.z_test_re import z_blueprint

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():
	return "Start"

@app.route('/stat/')
def stat_index():
	data = {
		'message': "Go to /stat/{z_test,t_test,anova}/ to use the stat treatments"
	}
	return jsonify(data)

app.register_blueprint(z_blueprint)
app.register_blueprint(t_blueprint)

if __name__ == '__main__':
	app.run(port=8080)