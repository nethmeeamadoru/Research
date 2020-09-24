import uuid

class DBService:

    def __init__(self, db_conn):
        self.__db_conn = db_conn

    def add_prediction(self, prediction, data):
        """[Add aprediction to the database]

        Args:
            prediction ([string]): [prediction according to the user's data]
            data ([object]): [details of the prediction]
        """        
        self.__db_conn.predictions_table.open()
        self.__db_conn.predictions_table.insert(
            id = str(uuid.uuid4()),
            name = data['name'],
            age = data['age'],
            gender = data['gender'],
            brushingTeeth = data['brushingTeeth'],
            dailyFlossing = data['dailyFlossing'],
            betelChewing = data['betelChewing'],
            betelWithTobacco = data['betelWithTobacco'],
            alcoholConsumption = data['alcoholConsumption'],
            smoking = data['smoking'],
            cariousTeeth = data['cariousTeeth'],
            gumDisease = data['gumDisease'],
            bleedingWhileBrushing = data['bleedingWhileBrushing'],
            depositsTartar = data['depositsTartar'],
            accidentalFracture = data['accidentalFracture'],
            missingTeeth = data['missingTeeth'],
            stainsOnTeeth = data['stainsOnTeeth'],
            malalignedTeeth = data['malalignedTeeth'],
            toothache = data['toothache'],
            facialPain = data['facialPain'],
            headache = data['headache'],
            nightPain = data['nightPain'],
            painWhileBiting = data['painWhileBiting'],
            swollenCheek = data['swollenCheek'],
            painFromAnUlcer = data['painFromAnUlcer'],
            swellingWithPain = data['swellingWithPain'],
            swellingWithoutPain = data['swellingWithoutPain'],
            clickingSoundWhileOpening = data['clickingSoundWhileOpening'],
            sensitiveToHotBeverages = data['sensitiveToHotBeverages'],
            sensitiveToColdBeverages = data['sensitiveToColdBeverages'],
            adultUpperJawDecayed = data['adultUpperJawDecayed'],
            adultUpperJawMissing = data['adultUpperJawMissing'],
            adultUpperJawFilled = data['adultUpperJawFilled'],
            adultLowerJawDecayed = data['adultLowerJawDecayed'],
            adultLowerJawMissing = data['adultLowerJawMissing'],
            adultLowerJawFilled = data['adultLowerJawFilled'],
            treatment = prediction
        )
        self.__db_conn.predictions_table.commit()

    def get_all_predictions(self):
        """[Get all prediction details]

        Returns:
            [array]: [all avialable predictions]
        """            
        predictions = self.__db_conn.predictions_table()
        return predictions

    def get_prediction_details(self, prediction_id):
        """[Get specific prediction details]

        Args:
            prediction_id ([string]): [unique identifier of the prediction details]

        Returns:
            [object]: [details of the prediction]
        """            
        prediction_details = self.__db_conn.predictions_table(id = prediction_id)
        return prediction_details[0]