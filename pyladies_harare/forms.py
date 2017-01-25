from django import forms
# from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
<<<<<<< HEAD
from crispy_forms.bootstrap import FormActions
=======
>>>>>>> 98cea01602e7e33d2f135a2914e9d707cba3c5a2

from .models import Contact, Comment


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'subject', 'message',)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_ContactForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('send', 'Send Email'))


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password',)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_LoginForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('login', 'Log in'))


<<<<<<< HEAD
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_SignupForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('signup', 'sign up'))


=======
>>>>>>> 98cea01602e7e33d2f135a2914e9d707cba3c5a2
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_ContactForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('send', 'Submit'))
