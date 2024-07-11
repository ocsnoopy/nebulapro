from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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
    email = forms.EmailField(required=True, widget = forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, widget = forms.EmailInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget = forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role')
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True, widget = forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, widget = forms.EmailInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget = forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'role')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(RoleForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')