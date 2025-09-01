from django.contrib.auth import authenticate, login, get_user_model
#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView
from django.contrib import messages
from .models import GuestEmail
from .forms import RegisterForm, LoginForm, GuestForm, MerchantRegisterForm

User = get_user_model()

# Create your views here.
def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context ={'form':form}
    next_ = request.GET.get("next")
    next_post = request.POST.get("next")
    redirect_path   =   next_ or next_post or None
    if form.is_valid():
        email   =   form.cleaned_data.get('email')
        new_guest_email =   GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path,request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'
    
    def form_valid(self,form):
        request = self.request
        next_ = request.GET.get("next")
        next_post = request.POST.get("next")
        redirect_path   =   next_ or next_post or None
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                try:
                    del request.session['guest_email_id']
                except:
                    pass
                if is_safe_url(redirect_path,request.get_host()):
                    return redirect(redirect_path)
                else:
                    return redirect("/")
            else:
                form.add_error(None, 'Your account is inactive. Please contact support.')
                return self.form_invalid(form)
        else:
            form.add_error(None, 'Invalid email or password. Please try again.')
            return self.form_invalid(form) 


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name =  'accounts/register.html'
    success_url = '/login/'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registration successful! You can now login with your credentials.')
        return response


class MerchantRegisterView(CreateView):
    form_class = MerchantRegisterForm
    template_name = 'accounts/merchant_register.html'
    success_url = '/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Merchant Registration'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Merchant registration successful! You can now login and start managing your products.')
        return response
    
    
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context ={
#         'form':form
#         }
#     if form.is_valid():
#         form.save()
# #         print(form.cleaned_data)
# #         username = form.cleaned_data.get("full_name")
# #         email = form.cleaned_data.get("email")
# #         password = form.cleaned_data.get("password1")
# #         User.objects.create_user(email,username,password)
#         return redirect("/login")
#     return render(request,'accounts/register.html',context)


# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context ={'form':form}
#     next_ = request.GET.get("next")
#     next_post = request.POST.get("next")
#     redirect_path   =   next_ or next_post or None
#     if form.is_valid():
#         print(form.cleaned_data)
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password')
#         user = authenticate(request,username=email,password=password)
#         if user is not None:
#             login(request,user)
#             try:
#                 del request.session['guest_email_id']
#             except:
#                 pass
#             if is_safe_url(redirect_path,request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect("/")
#         else:
#             print("Error")
#     return render(request,'accounts/login.html',context)
    