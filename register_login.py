import os
import re
import json
from json import JSONDecodeError
def registration(type):

    #Name :-
    name=input("Enter your Name : ")
    name_characters=re.findall("[a-zA-Z]",name)
    if name_characters==[]:
        print("Enter only Alphabets")
        name=input("Enter your Name : ")

    #Email :-
    email=input("Enter your email ID : ")
    email_check=re.search("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",email)
    if email_check==None:
        print("Enter email ID in correct format")
        email=input("Enter you email ID : ")

    #Password :-
    password=input("Enter your password...\n(Note:password must contain at least eight characters, at least one number and both lower and uppercase letters and special characters) : ")
    password_check=re.search("(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$",password)
    if password_check==None:
        print("Enter password in correct format")
        password=input("Enter your password...\n(Note:password must contain at least eight characters, at least one number and both lower and uppercase letters and special characters) : ")
                
    #Details :-
    print(f"\nYour Details : \nName : {name} \nEmail ID : {email} \nPassword : {password}\nRegistration Done Successfully!!!")

    #storing data to json file
    if type.lower()=='admin':
        f=open('admin.json','r+')
        d={
            "Full Name":name,
            "Email":email,
            "Password":password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open('user.json','r+')
        d={
            "Full Name":name,
            "Email":email,
            "Password":password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    option()

def login(type):

    #Email :-
    email=input("Enter your email ID : ")
    email_check=re.search("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",email)
    if email_check==None:
        print("Enter email ID in correct format")
        email=input("Enter you email ID : ")

    #Password :-
    password=input("Enter your password...\n(Note:password must contain at least eight characters, at least one number and both lower and uppercase letters and special characters) : ")
    password_check=re.search("(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$",password)
    if password_check==None:
        print("Enter password in correct format")
        password=input("Enter your password...\n(Note:password must contain at least eight characters, at least one number and both lower and uppercase letters and special characters) : ")

    d=0
    if type.lower()=='admin':
        f=open("admin.json",'r+')
    else:
        f=open("user.json",'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==email and content[i]["Password"]==password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def option():
    type=int(input("Welcome !!!\nPress 1 for Registration \nPress 2 for Login\nPress 3 for Logout \nEnter your choice : "))
    if type==1:
        type=int(input("Press 1 for admin registration \nPress 2 for user registration\nPress for Logout \nEnter your choice : "))
        if type==1:
            register_type="admin"
            registration(register_type)
        elif type==2 :
            register_type="user"
            registration(register_type)
        elif type==3:
            print("Logged out successfully")
            exit()
        else:
            print("Enter Valid value")
            option()

    elif type==2:
        type=int(input("Press 1 for admin login \nPress 2 for user login\nPress 3 for Logout \nEnter your choice : "))
        if type==1:
            login_type="admin"
            login(login_type)
        elif type==2:
            login_type="user"
            login(login_type)
        elif type==3:
            print("Logged out successfully")
            exit()
        else:
            print("Enter Valid value")
            option()

    elif type==3:
        print("Logged out successfully")
        exit()
    else:
        print("Enter either 1 or 2")
        option()
option()