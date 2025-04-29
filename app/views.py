from django.shortcuts import render

# Create your views here.
def users(request):
    context= {
        "user_details":
            {
      "id": 1,
      "firstName": "Emily",
      "lastName": "Johnson",
      "maidenName": "Smith",
      "age": 28,
      "gender": "female",
      "email": "emily.johnson@x.dummyjson.com",
      "phone": "+81 965-431-3024",
      "username": "emilys",
      "password": "emilyspass",
      "birthDate": "1996-5-30",
      "image": "https://dummyjson.com/icon/emilys/128",
      "bloodGroup": "O-",
      "height": 193.24,
      "weight": 63.16,
      "eyeColor": "Green",
      "hair": {
        "color": "Brown",
        "type": "Curly"
      }
            }

        
    }
    return render(request,'index.html',context)






# import json 
# file=open(r'C:\Users\ganes\OneDrive\Desktop\Dj projects\user.json','r')
# json_data=file.read()
# py_data=json.loads(json_data)

# users_info =py_data["users"]


# def usersview(request):
#     context={
#         'users':users_info
#     }
#     return render(request,'users.html',context)




import json 
file=open(r'C:\Users\ganes\OneDrive\Desktop\Dj projects\recipes.json','r')
json_data=file.read()
py_data=json.loads(json_data)

recipes =py_data["recipes"]


def usersviews(request):
    context={
        'recipes': recipes
    }
    return render(request,'recipes.html',context)


def recipe_details(request,idx):
    context={
    'recipes': recipes,
    'recipe':recipes[idx - 1]
    }
    return render(request,'recipes_details.html',context)




import json 
file=open(r'C:\Users\ganes\OneDrive\Desktop\Dj projects\cars.json','r')
json_data=file.read()
py_data=json.loads(json_data)

cars =py_data

def user_car(request):
    context={
        'car': cars,
    }
    return render(request,'cars.html',context)







