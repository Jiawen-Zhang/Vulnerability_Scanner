import numpy as np
import tensorflow as tf
import pickle
import sys
import pandas as pd

def predictWithTrainedModels(fileName):
    with open('../tokenizer/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    df_temp = pd.DataFrame({'source_code':[]})
    with open('tmp/'+fileName, 'r') as file:
        line = file.readline()
    df_temp = df_temp.append({'source_code':line}, ignore_index=True)
    tokenizedInput = tokenizer.texts_to_sequences(df_temp.loc[0])
    paddedTokenizedInput = tf.keras.preprocessing.sequence.pad_sequences(tokenizedInput, maxlen=500, padding="post")
    CWE119_model = tf.keras.models.load_model('trained_model/Simple_CNN_CWE119')
    CWE120_model = tf.keras.models.load_model('trained_model/Simple_CNN_CWE120')
    CWE469_model = tf.keras.models.load_model('trained_model/Simple_CNN_CWE469')
    CWE476_model = tf.keras.models.load_model('trained_model/Simple_CNN_CWE476')
    binary_model = tf.keras.models.load_model('trained_model/Simple_CNN_binary')
    c119_result = CWE119_model.predict(paddedTokenizedInput)
    c120_result = CWE120_model.predict(paddedTokenizedInput)
    c469_result = CWE469_model.predict(paddedTokenizedInput)
    c476_result = CWE476_model.predict(paddedTokenizedInput)
    binaryModel_result = binary_model.predict(paddedTokenizedInput)
    return c119_result[0][0],c120_result[0][0],c469_result[0][0],c476_result[0][0],binaryModel_result[0][0]


#print(predictWithTrainedModels('test_17.txt'))

