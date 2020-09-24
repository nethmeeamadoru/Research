from pydblite.sqlite import Database, Table

class DBConnect(object):
    """[configure pydblite db connection]
    
    Arguments:
        object {[Object]} -- [description]
    """

    db = Database('treatment_app_db', check_same_thread=False)

    predictions_table = Table("Predictions", db)

    db.conn.text_factory = str

    def __init__(self):
        self.predictions_table.create(
            ('id', 'TEXT'),
            ('name', 'TEXT'),
            ('age', 'INTEGER'),
            ('gender', 'INTEGER'),
            ('brushingTeeth', 'INTEGER'),
            ('dailyFlossing', 'INTEGER'),
            ('betelChewing', 'INTEGER'),
            ('betelWithTobacco', 'INTEGER'),
            ('alcoholConsumption', 'INTEGER'),
            ('smoking', 'INTEGER'),
            ('cariousTeeth', 'INTEGER'),
            ('gumDisease', 'INTEGER'),
            ('bleedingWhileBrushing', 'INTEGER'),
            ('depositsTartar', 'INTEGER'),
            ('accidentalFracture', 'INTEGER'),
            ('missingTeeth', 'INTEGER'),
            ('stainsOnTeeth', 'INTEGER'),
            ('malalignedTeeth', 'INTEGER'),
            ('toothache', 'INTEGER'),
            ('facialPain', 'INTEGER'),
            ('headache', 'INTEGER'),
            ('nightPain', 'INTEGER'),
            ('painWhileBiting', 'INTEGER'),
            ('swollenCheek', 'INTEGER'),
            ('painFromAnUlcer', 'INTEGER'),
            ('swellingWithPain', 'INTEGER'),
            ('swellingWithoutPain', 'INTEGER'),
            ('clickingSoundWhileOpening', 'INTEGER'),
            ('sensitiveToHotBeverages', 'INTEGER'),
            ('sensitiveToColdBeverages', 'INTEGER'),
            ('adultUpperJawDecayed', 'INTEGER'),
            ('adultUpperJawMissing', 'INTEGER'),
            ('adultUpperJawFilled', 'INTEGER'),
            ('adultLowerJawDecayed', 'INTEGER'),
            ('adultLowerJawMissing', 'INTEGER'),
            ('adultLowerJawFilled', 'INTEGER'),
            ('treatment', 'TEXT'),
             mode="open" )

