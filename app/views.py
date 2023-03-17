from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import random

#connect mysql to django using mysqlconnector
import mysql.connector
from mysql.connector import Error

def generate_unique_id():
    return str(random.randint(100000, 999999))


def check(id):
    query = "select id FROM qubit_dbms.login where id = %s"
    cursor.execute(query, (id,))

    ids = cursor.fetchall()
    if id in ids:
        return False
    else:
        return True
    
def check_user_name(username):
    query = "select user_mail FROM qubit_dbms.login where user_mail = %s"
    cursor.execute(query, (username,))
    names = cursor.fetchall()
    if names:
        return True
    else:
        return False


db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="pab2719100coc1!",
        database="qubit_dbms"
    )

cursor = db.cursor()





# Create your views here.

def index(request):
    return JsonResponse({'message': 'Hello, world!'})

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if check_user_name(username):
            return JsonResponse({'message': 'username already exists'})
        password = request.POST.get('password')
        id = generate_unique_id()
        while not check(id):
            id = generate_unique_id()
        query = "INSERT INTO qubit_dbms.login (user_mail,pswd,id) VALUES (%s, %s,%s)"
        values = (username, password,id)
        cursor.execute(query, values)
        db.commit()
        
        return JsonResponse({'message': 'success'})
    else:
        return render(request, 'login.html')

def details(request):
    query = "select * FROM qubit_dbms.login"
    cursor.execute(query)
    result = cursor.fetchall()
    # return this as json
    return JsonResponse({'message': result})


    