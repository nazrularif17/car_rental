from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CarRenter, CarOwner, Admin, User, CarDetail, Feedback, Booking
from .forms import UserForm, CarRenterForm, CarOwnerForm, CarDetailForm, BookingForm, OwnerAddCarForm, RenterBookingForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    if request.user.is_authenticated and request.user.is_carrenter:
        current_user = request.user.carrenter
        booking_exists = Booking.objects.filter(RentID=current_user, ReturnDate__gte=timezone.now().date()).exists()

        context = {
            'booking_exists': booking_exists,
        }
        return render (request,"index.html", context)
    else:
        return render (request,"index.html")

def adminlogin(request):
    if request.method=='POST':
        user_ID = request.POST['user_ID']
        password = request.POST['password']
        user = authenticate(request, user_ID=user_ID, password=password)
        if user is not None and user.is_admin:
            login(request, user)
            return redirect('adminpanel')
        else:
            return render(request, 'adminlogin.html', {'error': 'Enter correct ID and password'})
    else:
        return render(request, 'adminlogin.html')
    
def adminpanel(request):
    if request.user.is_authenticated and request.user.is_admin:
        return render(request, 'adminpanel.html')
    else:
        return redirect('adminlogin')
    
class adminrenterlist(ListView):
    model = CarRenter
    template_name = 'adminrenterlist.html'
    context_object_name = 'renterlist'
class adminownerlist(ListView):
    model = CarOwner
    template_name = 'adminownerlist.html'
    context_object_name = 'ownerlist'
class admincarlist(ListView):
    model = CarDetail
    template_name = 'admincarlist.html'
    context_object_name = 'carlist'
class adminbookinglist(ListView):
    model = Booking
    template_name = 'adminbookinglist.html'
    context_object_name = 'bookinglist'
class adminfeedbacklist(ListView):
    model = Feedback
    template_name = 'adminfeedbacklist.html'
    context_object_name = 'feedbacklist'

class adminrenterdetail(DetailView):
    model = CarRenter
    template_name = 'adminrenterdetail.html'
    context_object_name = 'renterlist'
class adminownerdetail(DetailView):
    model = CarOwner
    template_name = 'adminownerdetail.html'
    context_object_name = 'ownerlist'
class admincardetail(DetailView):
    model = CarDetail
    template_name = 'admincardetail.html'
    context_object_name = 'carlist'
class adminbookingdetail(DetailView):
    model = Booking
    template_name = 'adminbookingdetail.html'
    context_object_name = 'bookinglist'
class adminfeedbackdetail(DetailView):
    model = Feedback
    template_name = 'adminfeedbackdetail.html'
    context_object_name = 'feedbacklist'

class adminrenterupdate(UpdateView):
    model = CarRenter
    fields = ["RentPhonenum","RentEmail","RentLicense"]
    template_name = "adminrenterupdate.html"
    success_url = reverse_lazy("adminrenterlist")
class adminownerupdate(UpdateView):
    model = CarOwner
    fields = ["OwnPhonenum","OwnEmail"]
    template_name = "adminownerupdate.html"
    success_url = reverse_lazy("adminownerlist")
class admincarupdate(UpdateView):
    model = CarDetail
    fields = ["CarImg","CarPrice"]
    template_name = "admincarupdate.html"
    success_url = reverse_lazy("admincarlist")
class adminbookingupdate(UpdateView):
    model = Booking
    fields = ["BookDate","ReturnDate","BookStatus"]
    template_name = "adminbookingupdate.html"
    success_url = reverse_lazy("adminbookinglist")

class adminrenterdelete(DeleteView):
    model = CarRenter
    success_url = reverse_lazy("adminrenterlist")
class adminownerdelete(DeleteView):
    model = CarOwner
    success_url = reverse_lazy("adminownerlist")
class admincardelete(DeleteView):
    model = CarDetail
    success_url = reverse_lazy("admincarlist")
class adminbookingdelete(DeleteView):
    model = Booking
    success_url = reverse_lazy("adminbookinglist")

class admincarcreate(CreateView):
    model = CarDetail
    template_name = "admincarcreate.html"
    form_class = CarDetailForm
    success_url = reverse_lazy("admincarlist")
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['CarPlatenum'].widget.attrs['placeholder'] = 'Car plate number'
        form.fields['CarModel'].widget.attrs['placeholder'] = 'Car model'
        form.fields['NumofPassenger'].widget.attrs['placeholder'] = 'Number of passenger'
        form.fields['CarPrice'].widget.attrs['placeholder'] = 'Car price'
        return form
class adminbookingcreate(CreateView):
    model = Booking
    template_name = "adminbookingcreate.html"
    form_class = BookingForm
    success_url = reverse_lazy("adminbookinglist")
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['RentID'].widget.attrs['placeholder'] = 'Renter ID'
        form.fields['CarPlatenum'].widget.attrs['placeholder'] = 'Car plate number'
        form.fields['BookDate'].widget.attrs['placeholder'] = 'Booking date'
        form.fields['ReturnDate'].widget.attrs['placeholder'] = 'Return date'
        return form
    
def rentersignup(request):
    if request.method=='POST':
        userform = UserForm(request.POST)
        renterform = CarRenterForm(request.POST)
        if userform.is_valid() and renterform.is_valid():
            user = userform.save(commit=False)
            user.user_type = 'car renter'
            user.is_staff = False
            user.is_superuser = False
            user.save()
            renter = renterform.save(commit=False)
            renter.RentID = user
            renter.save()
            login(request, user)
            return redirect('index')
    else:
        userform = UserForm()
        renterform = CarRenterForm()
    return render (request,"rentersignup.html", {'userform': userform, 'renterform': renterform})

def renterlogin(request):
    if request.method=='POST':
        user_ID = request.POST['user_ID']
        password = request.POST['password']
        user = authenticate(request, user_ID=user_ID, password=password)
        if user is not None and user.is_carrenter:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'renterlogin.html', {'error': 'Enter correct ID and password'})
    else:
        return render(request, 'renterlogin.html')
    
def renterbookcar(request):
    if request.method == 'POST':
        bookform = RenterBookingForm(request.POST)
        if bookform.is_valid():
            renter = CarRenter.objects.get(RentID = request.user)
            book = bookform.save(commit=False)
            book.RentID = renter
            book.BookStatus = 'Pending'
            book.save()
            return redirect('carlist')
    else:
        bookform = RenterBookingForm()
    return render(request, 'renterbookcar.html', {'bookform': bookform,})

def renterbookstatus(request):
    current_user = request.user.carrenter
    current_date = timezone.now().date()
    booking_exists = Booking.objects.filter(RentID=current_user, ReturnDate__gte=timezone.now().date()).exists()
    try:
        booking = Booking.objects.get(RentID=current_user, ReturnDate__gte=current_date)
    except Booking.DoesNotExist:
        return render(request, 'renterbookstatus.html')
    context = {
        'booking': booking,
        'renter': current_user,
        'car': booking.CarPlatenum,
        'booking_exists': booking_exists,
    }
    return render(request, 'renterbookstatus.html', context)

def renterfeedback(request):
    current_user = request.user.carrenter
    booking_exists = Booking.objects.filter(RentID=current_user, ReturnDate__gte=timezone.now().date()).exists()
    context = {
            'booking_exists': booking_exists,
        }
    if request.method=='POST':
        comment = request.POST['comment']
        feedback = Feedback.objects.create(RentID=current_user, Comment=comment)
        feedback.save()
        return redirect('index')
    
    return render(request, 'renterfeedback.html', context)
        
def ownersignup(request):
    if request.method=='POST':
        userform = UserForm(request.POST)
        ownerform = CarOwnerForm(request.POST)
        if userform.is_valid() and ownerform.is_valid():
            user = userform.save(commit=False)
            user.user_type = 'car owner'
            user.is_staff = False
            user.is_superuser = False
            user.save()
            owner = ownerform.save(commit=False)
            owner.OwnID = user
            owner.save()
            login(request, user)
            return redirect('index')
    else:
        userform = UserForm()
        ownerform = CarOwnerForm()
    return render (request,"ownersignup.html", {'userform': userform, 'ownerform': ownerform})

def ownerlogin(request):
    if request.method=='POST':
        user_ID = request.POST['user_ID']
        password = request.POST['password']
        user = authenticate(request, user_ID=user_ID, password=password)
        if user is not None and user.is_carowner:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'ownerlogin.html', {'error': 'Enter correct ID and password'})
    return render(request, 'ownerlogin.html')

def owneraddcar(request):
    if request.method == 'POST':
        carform = OwnerAddCarForm(request.POST, request.FILES)
        if carform.is_valid():
            owner = CarOwner.objects.get(OwnID = request.user)
            car = carform.save(commit=False)
            car.OwnID = owner
            car.save()
            return redirect('carlist')
    else:
        carform = OwnerAddCarForm()
    return render(request, 'owneraddcar.html', {'carform': carform,})
    
class ownerupdatecar(UpdateView):
    model = CarDetail
    fields = ["CarImg","CarPrice"]
    template_name = "ownerupdatecar.html"
    success_url = reverse_lazy("carlist")

class ownerdeletecar(DeleteView):
    model = CarDetail
    success_url = reverse_lazy("carlist")
        
class cardetail(DetailView):
    model = CarDetail
    template_name = 'cardetail.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        context['car'] = car.OwnID
        if self.request.user.is_authenticated and self.request.user.is_carrenter:
            current_user = self.request.user.carrenter
            booking_exists = Booking.objects.filter(RentID=current_user, ReturnDate__gte=timezone.now().date()).exists()
            context['booking_exists'] = booking_exists
        return context
    
def logout_view(request):
    logout(request)
    return redirect('index')

class carlist(ListView):
    model = CarDetail
    template_name = 'carcatalog.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated and self.request.user.is_carrenter:
            current_user = self.request.user.carrenter
            booking_exists = Booking.objects.filter(RentID=current_user, ReturnDate__gte=timezone.now().date()).exists()
            context['booking_exists'] = booking_exists
        return context