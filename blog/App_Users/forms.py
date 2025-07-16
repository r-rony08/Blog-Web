from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_Users.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)
    # email_or_phone = forms.CharField(label="Email or Phone", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Mobile number or email address'}))

    # date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('custom', 'Custom')])

    # password1 = forms.CharField(
    #     label="Password",
    #     widget=forms.PasswordInput(attrs={'placeholder': 'New password'})
    # )
    # password2 = forms.CharField(
    #     label="Confirm Password",
    #     widget=forms.PasswordInput(attrs={'placeholder': 'Re-type password'})
    # )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
