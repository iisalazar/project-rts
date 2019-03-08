from Statistics.t_test import Independent
from flask_restful import Api, Resource
from flask import Blueprint, request

t_blueprint = Blueprint('t', __name__)
api = Api(t_blueprint)


# An API resource for T-test independent
class tIndependentAPI(Resource):
	def get(self):
		return { 'message' : "Invalid request. Only accepts POST request"}

	def post(self):
		data = request.get_json()
		group1 = data.get('group1', None)
		group2 = data.get('group2', None)
		if group1 is not None and group2 is not None:
			t = Independent()
			t.add_elements(group1=group1, group2=group2)
			return {"t_critical": t.get_t()}
		return {'error': "Groups should not be blank"}


api.add_resource(tIndependentAPI, '/stat/t/independent/')

