from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.contrib import messages
from .forms import LoginForm, SignupForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        request = self.request
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        messages.error(request,'username or password not correct')

        return super(LoginView, self).form_invalid(form)


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')