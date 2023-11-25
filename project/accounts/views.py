from django.contrib.auth.models import User
from .forms import SignUpForm
from django.views.generic.edit import CreateView

# Create your views here.
class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'
