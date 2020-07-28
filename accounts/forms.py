from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import user_registrated

users = User.objects.exclude(email='')
user_emails = users.values_list('email', flat=True).distinct()


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='E-mail')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label='Password (again)', widget=forms.PasswordInput,
        help_text='Enter the same password again for verification'
    )

    def clean_password1(self):
        self.password1 = self.cleaned_data["password1"]
        if self.password1:
            password_validation.validate_password(self.password1)
        return self.password1

    def clean_password2(self):
        self.password2 = self.cleaned_data["password2"]
        if self.password2:
            password_validation.validate_password(self.password2)
        return self.password2

    def clean(self):
        super().clean()
        if self.password1 and self.password2 and self.password1 != self.password2:
            errors = {"password2": ValidationError(
                'The passwords entered do not match', code='password_mismatch'
            )}
            raise ValidationError(errors)
        if self.cleaned_data["email"] in user_emails:
            errors = {"email": ValidationError(
                'Such an e-mail address is already in use', code='invalid_email'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name')
