from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

# Form for adding a post to the system. Includes customization for field attributes.
class AddPostForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      # Setting a custom label for the 'cat' field when no category is selected.
      self.fields['cat'].empty_label="Категория не выбрана"

  class Meta:
     model=Product
     # Defining the fields to be included in the form.
     fields=['name','slug','content','image','author','is_published', 'cat', 'user']
     # Customizing the appearance of specific fields using widgets.
     widgets = {
         'name': forms.TextInput(attrs={'class':'form-input'}),
         'content': forms.Textarea(attrs={'cols':60, 'rows':10}),
     }

  def clean_title(self):
      # Custom cleaning method for the 'name' field, raising a ValidationError if the length exceeds 200 characters.
      name=self.cleaned_data['name']
      if len(name)>200:
          raise ValidationError('Длина превышает 200 символов')

      return name

# Form for user registration, inheriting from Django's UserCreationForm. Includes customization for field attributes.
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        # Defining the fields to be included in the form.
        fields = ('username', 'email', 'password1', 'password2')


# Form for user login, inheriting from Django's AuthenticationForm. Includes customization for field attributes.
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

# Contact form with fields for name, email, content, and a captcha field. Inherits from Django's Form class.
class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    capatcha = CaptchaField()