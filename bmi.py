import requests

url = "https://fitness-calculator.p.rapidapi.com/bmi"
print("Enter Age , Weight , Height :");
age = input();
weight = input();
height = input();
print("Age =",age);
print("Weight =",weight);
print("Height =",height);
querystring = {"age":age,"weight":weight,"height":height}

headers = {
  "X-RapidAPI-Key": "6998965fcfmsh5504f323bf737c0p16b6a5jsn4bfeb9e23b9a",
  "X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
bmi = response.json();
print("BMI of the Person =",bmi['data']['bmi']);
print("BMI Range of the person =",bmi['data']['healthy_bmi_range']);
print("Health of the person =",bmi['data']['health']);