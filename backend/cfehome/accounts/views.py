from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login
from .forms import UserSignupForm, StaffSignupForm


# Create your views here.

def user_signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            user_type = form.cleaned_data['user_type']
            group_name = 'Customer' if user_type == 'customer' else 'Seller'
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

            login(request, user)
            return redirect('home')  # change as needed
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})


def staff_signup_view(request):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access

    if request.method == 'POST':
        form = StaffSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = True
            user.save()

            staff_group = Group.objects.get(name='Staff')
            user.groups.add(staff_group)

            return redirect('admin:index')  # or custom staff dashboard
    else:
        form = StaffSignupForm()
    return render(request, 'staff_signup.html', {'form': form})