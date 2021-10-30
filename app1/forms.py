from django import forms

# creating a form
class InputForm(forms.Form):
 link = forms.URLField()
