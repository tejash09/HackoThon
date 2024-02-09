import requests
food = input("Enter the food item: ")
query = food
api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': 'Bv9ERavHt0J9zaSth2kNQQ==gvnOnIJgrozJmHQK'})
if response.status_code == requests.codes.ok:
    food_details = response.json()[0];
    print("The name of Item = ",food_details['name'])
    print("The calories of Item = ",food_details['calories'])
    print("Fat content of Item = ",food_details['fat_total_g'],"percent")
    print("Protein content of Item = ",food_details['protein_g'],"percent")
    print("Carbohydrate content of Item = ",food_details['carbohydrates_total_g'],"percent")
    print("Sugar content of Item = ",food_details['sugar_g'],"percent")
    print("Sodium content of Item = ",food_details['sodium_mg'],"percent")
    print("Potassium content of Item = ",food_details['potassium_mg'],"percent")
    print("Fiber content of Item = ",food_details['fiber_g'],"percent")
    print("Colestrol content of Item = ",food_details['cholesterol_mg'],"percent")
else:
    print("Error:", response.status_code, response.text)