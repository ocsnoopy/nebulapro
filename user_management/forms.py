from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Role
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role')

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'role')

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']
