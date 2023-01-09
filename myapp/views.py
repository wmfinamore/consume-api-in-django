from django.shortcuts import render
import requests


def users(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()

    return render(request, "myapp/users.html", {'users': users})
