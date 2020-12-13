from django import forms

class loginform(forms.Form):
    userid=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR EMAIL OR PHONE NUMBER','class':'form-control border','autocomplete':"off"}))
    password=forms.CharField(min_length=5,widget=forms.PasswordInput(attrs={'placeholder': 'CREATE PASSWORD','class':'form-control border','autocomplete':"off"}))