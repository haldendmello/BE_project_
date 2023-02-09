from django.urls import path
from .import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register/<str:usertype>", views.register, name="register"),

    # path("load_roi", views.load_roi, name="load_roi"),
    # path("get_loan_status", views.get_loan_status, name="get_loan_status"),

    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("applyLoan", views.applyLoanFrom, name="applyLoan"),  # Apply Loan Form
    path("borrowerList", views.borrowerList, name="borrowerList"),  # order lists
    path("loanapplied", views.appledLoanList, name="loanapplied"),  # applied loan list
    path("loanStatus", views.loanStatus, name="loanStatus"),  # loan status
    path("loanRejected", views.loanRejected, name="loanRejected"),  # loan status
    path("storeKYC", views.storeKYC, name="storeKYC"), # Store KYC details in database and check
    path("userProfile", views.userProfile, name="userProfile"),
    path("userPayment", views.userPayment, name="userPayment"),
    path("getKYCDetails", views.getKYCDetails, name="getKYCDetails"),
    path("getKYCAadhar", views.getKYCAadhar, name="getKYCAadhar"),
    path("lenderPay/<str:aadhar>", views.lenderPay, name="lenderPay"),
    path("dashboard", views.lenderDashboard, name="dashboard"),
]
