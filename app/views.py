# from asyncio import start_unix_server
from asyncio import constants
from cgitb import html
import json
import imp
import re
from telnetlib import STATUS
from urllib import request
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError
from .models import User, kyc
from app.decorators import unauthenticated_user, allowed_users
from django.views.decorators.csrf import csrf_exempt


import pickle,gzip
# import numpy as np

@unauthenticated_user
def register(request, usertype):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, 'Password do not match',
                           extra_tags='danger')
            return render(request, "app/register.html", {
                "usertype": usertype,
            })

        # Attempt to create new farmer user
        try:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=username,
                password=password,
                user_type=usertype.lower()
            )
            user.save()

        except IntegrityError:
            messages.error(
                request, 'User with email already exsists', extra_tags='danger')
            return render(request, "app/register.html", {
                "usertype": usertype,
            })
        login(request, user)

        return HttpResponseRedirect(reverse("index"))

    return render(request, "app/register.html", {
        "usertype": usertype,
    })


@unauthenticated_user
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(
                request, 'Invalid username or password.', extra_tags='danger')
    return render(request, "app/login.html")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Create your views here.

def index(request):
    # load_roi(request)
    return render(request, "app/index.html")

# Apply Form function


# @login_required(login_url="login")
# @allowed_users(allowed_rolls=["borrower"])
def applyLoanFrom(request):

    if request.method == "POST":

        loan_a = request.POST["loan_a"]
        p_o_loan = request.POST["p_o_loan"]
        gender = request.POST["gender"]
        status = request.POST["status"]
        buss_comm = request.POST["buss_comm"]
        age = request.POST["age"]
        property_value = request.POST["property_value"]
        term = request.POST["term"]
        # credit_score = request.POST["credit_score"]
        credit_worthiness = 1

        a_income = request.POST["a_income"]

        # print(loan_a, p_o_loan, gender, status, buss_comm, a_income, age, credit_score, property_value, term, loan_type, credit_worthiness)

        # if(p_o_loan == ):

# Gender,Loan_purpose,Credit_Worthiness,Loan_amount,Term,Income,Credit_Score,Age


        # status = get_loan_status(float(gender),p_o_loan,credit_worthiness,loan_a,term,a_income,credit_score,age)
        # status=get_loan_status()
        status = 1
        print("Status : ",status)
        if(status == 1):
            roi = load_roi(float(gender),p_o_loan,credit_worthiness,loan_a,term,a_income,credit_score,age,status)
            roi = 12
            # print("ppppp",float(gender),p_o_loan,credit_worthiness,loan_a,term,a_income,credit_score,age,status)
            # roi = 12
            context = {
                'status' : 1,
                'loan_a':loan_a,
                'p_o_loan' :p_o_loan,
                'term':term,
                'credit_worthiness' : credit_worthiness,
                'roi' :float(roi)
            }
            return render(request, "app/loanStatus.html", context)
        else:
            return render(request, "app/loanrejected.html")
    else:
        return render(request, "app/apply.html")


# loan applied
def appledLoanList(request):

    return render(request, "app/appliedLoanList.html")


def loanStatus(request):

    return render(request, "app/loanStatus.html")


def loanRejected(request):

    return render(request, "app/loanrejected.html")


# borrower Profile
def userProfile(request):

    return render(request, "app/userProfile.html")


# borrower payment
def userPayment(request):

    return render(request, "app/userPayment.html")


def lenderPay(request, aadhar):

    return  render(request, "app/lenderPay.html")


def lenderDashboard(request):

    return render(request, "app/dashboard.html")


# Pending orders for lenders
# @login_required(login_url="login")
# @allowed_users(allowed_rolls=["lender"])
def borrowerList(request):

    return render(request, "app/borrowerList.html")


def about(request):

    return render(request, "app/about.html")


def services(request):

    return render(request, "app/services.html")


def contact(request):

    return render(request, "app/contact.html")


def load_roi(Gender,Loan_purpose,Credit_Worthiness,Loan_amount,Term,Income,Credit_Score,Age,Status):
    print("roiiii........")
    with gzip.open("roi.pklz", 'rb') as ifp:
        model=pickle.load(ifp)
        print(model)
    # a=[2,1,3,1,0,19650,180.0,268000.0,3840.0,852,69,1]
    op=model.predict(np.array([Gender,Loan_purpose,Credit_Worthiness,Loan_amount,Term,Income,Credit_Score,Age,Status]).reshape(1,-1))
    print(op)

    return op

# def get_loan_status(Gender,Loan_purpose,Credit_Worthiness,Loan_amount,Term,Income,Credit_Score,Age):
def get_loan_status():
    print("statusss..............")
    with gzip.open("status.pklz", 'rb') as ifp:
        modell=pickle.load(ifp)
        print(modell)
    # a=[3,1,0,1,0,316500,4.045476,324.0,338000.0000,9720.0,678,39]
    # op=modell.predict(np.array([Gender,Loan_purpose,Credit_Worthiness,Loan_amount,Term,Income,Credit_Score,Age]).reshape(1,-1))
    op=modell.predict(np.array([3,0,1,316500,324.0,972000.0,678,39]).reshape(1,-1))
    
    print(op)

    return op

@csrf_exempt
def storeKYC(request):
    if request.method == 'POST' :
        userData = json.loads(request.body)
        user = kyc.objects.filter(AadharNumber = userData['aadharNo']).values()

        print(user)
        print(userData)

        if user :
            userAddInfo = kyc.objects.get(id = user[0]['id'])

            # Data from user
            firstName = userData["firstName"].lower().capitalize().strip()
            lastName = userData["lastName"].lower().capitalize().strip()
            panNo = str(userData["panNo"]).strip()
            aadharNo = str(userData["aadharNo"]).strip()
            walletAddress = str(userData["walletAddress"]).strip()

            # model KYC data
            modelFirstName = user[0]["firstName"]
            modelLastName = user[0]["lastName"]
            modelPANnumber =  user[0]["PANnumber"]
            modelAadharNumber = user[0]["AadharNumber"]


            if firstName == modelFirstName and lastName == modelLastName and panNo == modelPANnumber and aadharNo == modelAadharNumber :

                userAddInfo.WalletAddress = walletAddress
                userAddInfo.save()
                data = {
                    'success' : 1,
                }
                return JsonResponse(data, status=400)
            else : 
                print("..")
                data = {
                    'success' : 0,
                }
                return JsonResponse(data, status=400)
        else:
            data = {
                'success' : 0,
            }
            return JsonResponse(data, status=400)
    else:

        return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def getKYCDetails(request):

    if request.method == 'POST':
        userData = json.loads(request.body)
        user = kyc.objects.filter(WalletAddress = userData["walletAddress"]).values()

        data = {
            'FirstName' : user[0]["firstName"],
            'LastName' : user[0]["lastName"],
            'PANnumber' :  user[0]["PANnumber"],
            'AadharNumber' : user[0]["AadharNumber"],
            'CreditScore' : user[0]["CreditScore"],
            'WalletAddress' : user[0]["WalletAddress"]
        }
        
        return JsonResponse(data, status=400)
    else:
        return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def getKYCAadhar(request):

    if request.method == 'POST':
        userData = json.loads(request.body)
        user = kyc.objects.filter(AadharNumber = userData["aadharNo"]).values()

        data = {
            'FirstName' : user[0]["firstName"],
            'LastName' : user[0]["lastName"],
            'PANnumber' :  user[0]["PANnumber"],
            'AadharNumber' : user[0]["AadharNumber"],
            'CreditScore' : user[0]["CreditScore"],
            'WalletAddress' : user[0]["WalletAddress"]
        }
        
        return JsonResponse(data, status=400)
    else:
        return HttpResponseRedirect(reverse("index"))


# accept
# 3,0,1,316500,324.0,972000.0,678,39
