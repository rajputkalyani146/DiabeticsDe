import config
import pickle
import json
import numpy as np
import pandas as pd
#for DEPLOYMENT
class Diabetes:
    def __init__(self, Glucose, BloodPressure, SkinThickness, Insulin, BMI,  DiabetesPedigreeFunction, Age):
        self.model_File_Path = "Diabetes_logistics.pkl"        
        self.Glucose = Glucose
        self.BloodPressure =BloodPressure
        self.SkinThickness=SkinThickness 
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age
    def load_saved_data(self):
        with open (self.model_File_Path, "rb") as f:
            self.lg_model = pickle.load(f)
        with open ("Project_data.json", 'r') as f:
            self.Project_data = json.load(f)
        print(self.lg_model) 
    def get_predicted_outcome(self):
        self.load_saved_data()
        Glucose = self.Glucose        
        BloodPressure = self.BloodPressure
        SkinThickness = self.SkinThickness
        Insulin = self.Insulin
        BMI = self.BMI
        DiabetesPedigreeFunction = self.DiabetesPedigreeFunction
        Age = self.Age
        test_array = np.array([Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                            DiabetesPedigreeFunction, Age], ndmin = 2)
        print("this is array:",test_array)
        predicted_class = self.lg_model.predict(test_array)[0]
        print("Predicted Class : ", predicted_class)
        return predicted_class

#FOR TESTING POSTMAN
# class Diabetes:
#     def __init__(self, user_data):
#         self.model_File_Path = "Diabetes_logistics.pkl"
#         self.user_data = user_data     
#     def load_saved_data(self):
#         with open (self.model_File_Path, "rb") as f:
#             self.log_clf_model = pickle.load(f)
#         with open ("project_data.json", 'r') as f:
#             self.project_data = json.load(f)
#         print(self.log_clf_model) 

#     def get_predicted_outcome(self):
#         self.load_saved_data()
#         Glucose = eval(self.user_data['Glucose'])
#         BloodPressure = eval(self.user_data['BloodPressure'])
#         print("BP",BloodPressure)
#         SkinThickness = eval(self.user_data['SkinThickness'])
#         Insulin = eval(self.user_data['Insulin'])
#         BMI = eval(self.user_data['BMI'])
#         DiabetesPedigreeFunction = eval(self.user_data['DiabetesPedigreeFunction'])
#         Age = eval(self.user_data['Age'])

#         test_array = np.array([Glucose, BloodPressure, SkinThickness, Insulin, BMI,
#                             DiabetesPedigreeFunction, Age], ndmin = 2)
#         print(test_array)
#         predicted_class = self.log_clf_model.predict(test_array)[0]

#         print("Predicted Class : ", predicted_class)

#         return predicted_class



if __name__ == "__main__":
    dbs = Diabetes()


