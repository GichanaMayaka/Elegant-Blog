from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from blog.forms import UserForm, UserProfileForm
from . import models


# Create your views here.


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = 'index.html'
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = 'post.html'


def about(request):
    return render(request, 'about.html', {'me': 'Gichana'})


def contact(request):
    return render(request, 'contact.html', {})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()
            registered = True

            return HttpResponseRedirect('/blog/home/')

        else:
            print(user_form.errors, end='\n')
            print(profile_form.errors, end='\n')

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form,
                                             'registered': registered}
                  )


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/blog/home/')
            else:
                return HttpResponse('Your account has been disabled')

        else:
            return HttpResponse('Invalid credentials')

    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/home/')