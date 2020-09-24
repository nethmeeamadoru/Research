import pickle
import numpy as np
import pandas as pd

from collections import Counter
from imblearn.over_sampling import RandomOverSampler

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split


def predict_treatment(object):
    """[Predict treatment according to the user's input]

    Args:
        object ([object]): [input data of the user]

    Returns:
        [string]: [prediction according to the user's data]
    """    
    input = np.array(
        [[
            object['age'],
            object['gender'],
            object['brushingTeeth'],
            object['dailyFlossing'],
            object['betelChewing'],
            object['betelWithTobacco'],
            object['alcoholConsumption'],
            object['smoking'],
            object['cariousTeeth'],
            object['gumDisease'],
            object['bleedingWhileBrushing'],
            object['depositsTartar'],
            object['accidentalFracture'],
            object['missingTeeth'],
            object['stainsOnTeeth'],
            object['malalignedTeeth'],
            object['toothache'],
            object['facialPain'],
            object['headache'],
            object['nightPain'],
            object['painWhileBiting'],
            object['swollenCheek'],
            object['painFromAnUlcer'],
            object['swellingWithPain'],
            object['swellingWithoutPain'],
            object['clickingSoundWhileOpening'],
            object['sensitiveToHotBeverages'],
            object['sensitiveToColdBeverages'],
            object['adultUpperJawDecayed'],
            object['adultUpperJawMissing'],
            object['adultUpperJawFilled'],
            object['adultLowerJawDecayed'],
            object['adultLowerJawMissing'],
            object['adultLowerJawFilled'],
        ]]
    )
    # input = np.array([[15,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    loaded_model = pickle.load(open('test/sample_test.pkl', 'rb'))
    prediction = loaded_model.predict(input)
    return prediction[0]