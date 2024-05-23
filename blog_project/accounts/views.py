from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')