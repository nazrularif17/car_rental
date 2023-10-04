from django.contrib import admin
from .models import Admin, User, CarOwner, CarRenter, CarDetail, Booking, Feedback

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(CarRenter)
admin.site.register(CarOwner)
admin.site.register(CarDetail)
admin.site.register(Booking)
admin.site.register(Feedback)