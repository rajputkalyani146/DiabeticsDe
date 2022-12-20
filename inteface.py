from flask import Flask, jsonify, render_template, request, redirect
import config
from utils import Diabetes
app = Flask(__name__)

@app.route('/',methods=['GET', "POST"])
def hello():
    # return 'hello'
    return render_template("index1.html")

#FOR DEPLOYMENT
@app.route('/predict',methods = ['GET', "POST"])
def prediction():
    if request.method == 'GET':       
        Glucose = eval(request.args.get("Glucose"))
        BloodPressure = eval(request.args.get("BloodPressure"))
        SkinThickness = eval(request.args.get("SkinThickness"))
        Insulin = eval(request.args.get("Insulin"))
        BMI = eval(request.args.get("BMI"))
        DiabetesPedigreeFunction = eval(request.args.get("DiabetesPedigreeFunction"))
        Age = eval(request.args.get("Age"))
        print('value',Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                            DiabetesPedigreeFunction, Age)
        med_dbs = Diabetes(Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                            DiabetesPedigreeFunction, Age)
        pred_class = med_dbs.get_predicted_outcome()
        print("::::::::::",pred_class)  
        if pred_class == 1:        
            return render_template("index1.html", prediction = 'You have diabetics')
        else:
            return render_template("index1.html", prediction = 'You do not diabetics')


# FOR TESTING FLASK AND POSTMAN

# @app.route('/predict',methods = ['GET', "POST"])
# def prediction():
#     if request.method == 'POST':
#         data = request.form        
#         print('data :',data)
#         med_dbs = Diabetes(data)
#         pred_class = med_dbs.get_predicted_outcome()
#         print("::::::::::",pred_class)
#         #return jsonify({"Outcome :":pred_class})
#         return f"{pred_class}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
    # app.run()
