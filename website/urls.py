from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("",views.index, name="index"),
    #ADMIN
    path("adminlogin",views.adminlogin, name="adminlogin"),
    path("adminpanel",views.adminpanel, name="adminpanel"),
    #CARRENTER
    path("adminrenterlist",adminrenterlist.as_view(), name="adminrenterlist"),
    path("adminrenterdetail/<pk>",adminrenterdetail.as_view(), name="adminrenterdetail"),
    path("adminrenterupdate/<pk>",adminrenterupdate.as_view(), name="adminrenterupdate"),
    path("adminrenterdelete/<pk>",adminrenterdelete.as_view(), name="adminrenterdelete"),
    #CAROWNER
    path("adminownerlist",adminownerlist.as_view(), name="adminownerlist"),
    path("adminownerdetail/<pk>",adminownerdetail.as_view(), name="adminownerdetail"),
    path("adminownerupdate/<pk>",adminownerupdate.as_view(), name="adminownerupdate"),
    path("adminownerdelete/<pk>",adminownerdelete.as_view(), name="adminownerdelete"),
    #CARDETAIL
    path("admincarlist",admincarlist.as_view(), name="admincarlist"),
    path("admincardetail/<pk>",admincardetail.as_view(), name="admincardetail"),
    path("admincarupdate/<pk>",admincarupdate.as_view(), name="admincarupdate"),
    path("admincardelete/<pk>",admincardelete.as_view(), name="admincardelete"),
    path("admincarcreate",admincarcreate.as_view(), name="admincarcreate"),
    #BOOKING
    path("adminbookinglist",adminbookinglist.as_view(), name="adminbookinglist"),
    path("adminbookingdetail/<pk>",adminbookingdetail.as_view(), name="adminbookingdetail"),
    path("adminbookingupdate/<pk>",adminbookingupdate.as_view(), name="adminbookingupdate"),
    path("adminbookingdelete/<pk>",adminbookingdelete.as_view(), name="adminbookingdelete"),
    path("adminbookingcreate",adminbookingcreate.as_view(), name="adminbookingcreate"),
    #FEEDBACK
    path("adminfeedbacklist",adminfeedbacklist.as_view(), name="adminfeedbacklist"),
    path("adminfeedbackdetail/<pk>",adminfeedbackdetail.as_view(), name="adminfeedbackdetail"),
    #RENTER
    path("rentersignup",views.rentersignup, name="rentersignup"),
    path("renterlogin",views.renterlogin, name="renterlogin"),
    path("renterbookcar",views.renterbookcar, name="renterbookcar"),
    path("renterbookstatus",views.renterbookstatus, name="renterbookstatus"),
    path("renterfeedback",views.renterfeedback, name="renterfeedback"),
    #OWNER
    path("ownersignup",views.ownersignup, name="ownersignup"),
    path("ownerlogin",views.ownerlogin, name="ownerlogin"),
    path("owneraddcar",views.owneraddcar, name="owneraddcar"),
    path("ownerupdatecar<pk>",ownerupdatecar.as_view(), name="ownerupdatecar"),
    path("ownerdeletecar<pk>",ownerdeletecar.as_view(), name="ownerdeletecar"),

    path("carlist",carlist.as_view(), name="carlist"),
    path("cardetail<pk>",cardetail.as_view(), name="cardetail"),

    path('logout', views.logout_view, name='logout'),
]