import requests
import webbrowser
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def get_info():
    return render_template('input.html')

@app.route('/process',methods=['POST'])

def process():
    global option
    option = request.form['option']
    if(option == '1'):
        return render_template('exercise_input.html')
    elif(option =='2'):
        return render_template('Food_input.html')
    else:
        return render_template('bmi_input.html')

@app.route('/submit',methods=['POST'])
def submit():
    if(option =='1'):
        bodyPart = request.form['bodyPart']
        url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/" + bodyPart

        querystring = {"limit": "5"}

        headers = {
            "X-RapidAPI-Key": "0f491a5108mshbe7b62a9976bafbp15461ejsn7894515d0926",
            "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            exercise_details = response.json()

            exercise_all_details = []

            for idx, details in enumerate(exercise_details, start=1):
                exercise_data = {
                    "index": idx,
                    "name": details['name'],
                    "equipment": details['equipment'],
                    "url": details['gifUrl'],
                    "target": details['target'],
                    "secondary_muscles": details['secondaryMuscles'],
                    "instructions": details['instructions']
                }
                exercise_all_details.append(exercise_data)

            return render_template('exercise_output.html', title="ALL EXERCISE DETAILS", items=exercise_all_details)

        except Exception as e :
                return render_template('error.html', error=f"Error: {str(e)}")

    elif(option =='2'):
        try:
            food = request.form['food']
            query = food
            api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
            response = requests.get(api_url, headers={'X-Api-Key': 'Bv9ERavHt0J9zaSth2kNQQ==gvnOnIJgrozJmHQK'})
            if response.status_code == requests.codes.ok:
                food_details = response.json()[0]
                food_all_details_list=[]
                food_all_details_list.append("The name of Item = "+food_details['name'])
                food_all_details_list.append("The calories of Item = "+str(food_details['calories'])+'Kcal')
                food_all_details_list.append("Fat content of Item = "+str(food_details['fat_total_g'])+"g")
                food_all_details_list.append("Protein content of Item = "+str(food_details['protein_g'])+"g")
                food_all_details_list.append("Carbohydrate content of Item = "+str(food_details['carbohydrates_total_g'])+"g")
                food_all_details_list.append("Sugar content of Item = "+str(food_details['sugar_g'])+"g")
                food_all_details_list.append("Sodium content of Item = "+str(food_details['sodium_mg'])+"mg")
                food_all_details_list.append("Potassium content of Item = "+str(food_details['potassium_mg'])+"mg")
                food_all_details_list.append("Fiber content of Item = "+str(food_details['fiber_g'])+"g")
                food_all_details_list.append("Colestrol content of Item = "+str(food_details['cholesterol_mg'])+"mg")
                return render_template('food_output.html',title ='FOOD DETAILS',items = food_all_details_list)
            else:
                return render_template('error.html',error = "ERROR IN GETTING FOOD DETAILS")
        except:
            return render_template('error.html',error = "ENTER VALID INPUT DETAILS")
    
    else:
        try:
            url = "https://fitness-calculator.p.rapidapi.com/"
            
            age = request.form['age']
            gender = request.form['gender']
            height = request.form['height']
            weight = request.form['weight']
            querystring = {"age":age,"weight":weight,"height":height}

            headers = {
            "X-RapidAPI-Key": "311c72f141msh4fc8cd54dc38698p16cac1jsn2296a78a6bac",
            "X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com"
            }

            response = requests.get(url+"bmi", headers=headers, params=querystring)
            
            bmis = response.json()
            bmi_all_details=[]
            bmi_all_details.append('age of the person'+str(age))
            bmi_all_details.append('gender of the person'+str(gender))
            bmi_all_details.append('height of the person'+str(height))
            bmi_all_details.append('weight of the person'+str(weight))
            
            bmi_all_details.append("BMI of the Person ="+str(bmis['data']['bmi']))
            bmi_all_details.append("BMI Range of the person ="+str(bmis['data']['healthy_bmi_range']))
            bmi_all_details.append("Health of the person ="+str(bmis['data']['health']))
            querystring={"gender":gender,"height":height}
            response=requests.get(url+"idealweight",headers=headers,params=querystring)
            bmis = response.json()
            bmi_all_details.append("Idealweight of the person ="+str(bmis['data']['Robinson']))
            return render_template('bmi_output.html',title='Body Mass Index',items=bmi_all_details)
        except:
            return render_template('error.html',error = 'INVALID INPUT DETAILS FOR BODY MASS INDEX CALCULATION OR SERVER UNAVAILABLE')


urll='http://127.0.0.1:5000'
webbrowser.open(urll)
app.run(debug=True)