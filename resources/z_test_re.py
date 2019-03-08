from Statistics.z_test import two_sample
from flask_restful import Api, Resource
from flask import Blueprint, request

z_blueprint = Blueprint('z', __name__)
api = Api(z_blueprint)


class zTwoSampleAPI(Resource):
	def get(self):
		return { 'message' : "Invalid request. Only accepts POST request"}

	def post(self):
		data = request.get_json()
		group1 = data.get('group1', None)
		group2 = data.get('group2', None)
		z = two_sample()
		z.add_data(group1=group1, group2=group2)
		return {'z_critical' : z.get_z_value()}

api.add_resource(zTwoSampleAPI, '/stat/z/two_sample/')

