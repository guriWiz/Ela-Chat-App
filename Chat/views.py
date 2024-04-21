from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from django.contrib import messages

class Home(TemplateView):
    template_name = 'index.html'

@login_required
def index(request):
    return render(request,'login.html')

def register(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'dashboard.html')
    context['form']=form
    return render(request,'register.html',context)

@login_required
def room(request, room_name):
    return render(request, 'roomlobby.html', {
        'room_name': room_name
    })

class SearchUser(ListView):
    model = User
    template_name = 'searchusers.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User.objects.all()
        return object_list

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('Dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context={'u_form': u_form}
    return render(request, 'updateprofile.html',context )