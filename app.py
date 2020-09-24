from flask import Flask,jsonify
from flask_restplus import Api, Resource, fields
from flask_cors import CORS, cross_origin
from helpers.predict import predict_treatment
from infrastructure.db_connect import DBConnect
from services.db_service import DBService


db_conn = DBConnect()
db_service = DBService(db_conn)

app = Flask(__name__)
CORS(app)


api = Api(app, version='1.0', title='Predict Treatment',
    description='',
)

treatment_api = api.namespace('api', description='Predict Treatment')

treatment_model = api.model('Treatment',{
    'name': fields.String(description='', required=True),
    'age': fields.Integer(description='', required=True),
    'gender': fields.Integer(required=True, description=''),
    'brushingTeeth': fields.Integer(description='', required=True),
    'dailyFlossing': fields.Integer(required=True, description=''),
    'betelChewing': fields.Integer(description='', required=True),
    'betelWithTobacco': fields.Integer(required=True, description=''),
    'alcoholConsumption': fields.Integer(description='', required=True),
    'smoking': fields.Integer(required=True, description=''),
    'cariousTeeth': fields.Integer(description='', required=True),
    'gumDisease': fields.Integer(required=True, description=''),
    'bleedingWhileBrushing': fields.Integer(description='', required=True),
    'depositsTartar': fields.Integer(required=True, description=''),
    'accidentalFracture': fields.Integer(required=True, description=''),
    'missingTeeth': fields.Integer(description='', required=True),
    'stainsOnTeeth': fields.Integer(required=True, description=''),
    'malalignedTeeth': fields.Integer(description='', required=True),
    'toothache': fields.Integer(required=True, description=''),
    'facialPain': fields.Integer(description='', required=True),
    'headache': fields.Integer(description='', required=True),
    'nightPain': fields.Integer(required=True, description=''),
    'painWhileBiting': fields.Integer(description='', required=True),
    'swollenCheek': fields.Integer(required=True, description=''),
    'painFromAnUlcer': fields.Integer(description='', required=True),
    'swellingWithPain': fields.Integer(required=True, description=''),
    'swellingWithoutPain': fields.Integer(description='', required=True),
    'clickingSoundWhileOpening': fields.Integer(required=True, description=''),
    'sensitiveToHotBeverages': fields.Integer(description='', required=True),
    'sensitiveToColdBeverages': fields.Integer(required=True, description=''),
    'adultUpperJawDecayed': fields.Integer(required=True, description=''),
    'adultUpperJawMissing': fields.Integer(description='', required=True),
    'adultUpperJawFilled': fields.Integer(required=True, description=''),
    'adultLowerJawDecayed': fields.Integer(description='', required=True),
    'adultLowerJawMissing': fields.Integer(required=True, description=''),
    'adultLowerJawFilled': fields.Integer(description='', required=True),
})

@treatment_api.route('/predict')
class PredictTreatment(Resource):
    """[Predict treatment api]

    Arguments:
        Resource {[Object]} -- [packecge of the flask_restplus]
    """

    @treatment_api.doc('predict_treatment')
    @treatment_api.expect(treatment_model)
    def post(self):
        '''Predict treatment'''
        try:
            treatment = predict_treatment(api.payload)
            db_service.add_prediction(treatment, api.payload)
            return jsonify(treatment)
        except Exception as e:
            return jsonify(str(e))

@treatment_api.route('/alltreatments')
class AllTreatmentDetails(Resource):
    """[Get all treatment details api]

    Arguments:
        Resource {[Object]} -- [packecge of the flask_restplus]
    """

    @treatment_api.doc('get_all_treatments')
    def get(self):
        '''All treatment details'''
        try:
            predictions = db_service.get_all_predictions()
            return jsonify(predictions)
        except Exception as e:
            return jsonify(str(e))

@treatment_api.route('/treatment/<string:prediction_id>')
class TreatmentDetails(Resource):
    """[Get specific treatment details api]

    Arguments:
        Resource {[Object]} -- [packecge of the flask_restplus]
    """

    @treatment_api.doc('compare_texts')
    def get(self, prediction_id):
        '''Specific treatment details'''
        try:
            prediction_details = db_service.get_prediction_details(prediction_id)
            return jsonify(prediction_details)
        except Exception as e:
            return jsonify(str(e))

if __name__ == '__main__':
    app.run(debug=True)