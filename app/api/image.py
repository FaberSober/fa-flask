from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.recognition import recognize_image

api = Namespace('image', description='Image recognition operations')

upload_model = api.model('Upload', {
    'filename': fields.String(description='Uploaded file name')
})

@api.route('/recognize')
class ImageRecognition(Resource):
    @api.expect(api.parser().add_argument('file', location='files', type='file', required=True))
    @api.response(200, 'Success', upload_model)
    def post(self):
        """Recognize content from uploaded image"""
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            api.abort(400, "No file uploaded")

        result = recognize_image(uploaded_file)
        return {"filename": uploaded_file.filename, "result": result}
