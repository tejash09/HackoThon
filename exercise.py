import requests
bodyPart= input("1.back\n2.cardio\n3.chest\n4.lower arms\n5.lower legs\n6.neck\n7.shoulders\n8.upper arms")
url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/"+bodyPart

querystring = {"limit":"5"}

headers = {
	"X-RapidAPI-Key": "0f491a5108mshbe7b62a9976bafbp15461ejsn7894515d0926",
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

exercise_details=response.json()
d= 1
for details in exercise_details:
    Name = details['name']
    equipment = details['equipment']
    url = details['gifUrl']
    target = details['target']
    
    print("The details of "+str(d)+"nd element")
    print("The name of Exercise = "+Name)
    print("The equipment used = "+equipment)
    print("URL = "+url)
    print("Target = "+target)
    secondary_muscles_dict = details['secondaryMuscles']
    for muscles in secondary_muscles_dict:
        print(muscles)
    instructions= details['instructions']
    c = 1
    for instruction in instructions:
        print(str(c)+" : "+instruction)
        c+=1
    d+=1
    print()
