from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from ribbit_app.models import Ribbit


class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class':"input-medium"}))
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name', 'class':"input-medium"}))
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name', 'class':"input-medium"}))
	username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class':"input-medium"}))
	password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class':"input-medium"}))
	password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':"input-medium"}))

	def is_valid(self):
		form = super(UserCreateForm, self).is_valid()

		for f, error in self.errors.iteritems():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form

	class Meta:
		fields = ['email', 'username', 'first_name', 'last_name', 'username', 'password1', 'password2']
		model = User

class AuthenticateForm(AuthenticationForm):
	username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

	def is_valid(self):
		form = super(AuthenticateForm, self).is_valid()

		for f, error in self.errors.iteritems():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form

class RibbitForm(forms.ModelForm):
	content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'ribbitText'}))

	def is_valid(self):
		form = super(RibbitForm, self).is_valid()

		for f in self.errors.iterkeys():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error ribbitText'})
		return form
	class Meta:
		model = Ribbit
		exclude = ('user',)