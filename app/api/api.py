from flask_restx import Namespace, Resource

api = Namespace('api', description='Api Demo')


@api.route('/hello')
class ImageRecognition(Resource):
    @api.response(200, 'Success')
    def get(self):
        """do nothing and return success"""
        return {"result": "success"}
