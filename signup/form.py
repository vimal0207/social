from django import forms

class signupform(forms.Form):
    name=forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR NAME','class':'form-control border'}))
    goption=[('Male','Male'),("female ",'Female'),('Other ','Other'),]
    gender=forms.CharField(widget=forms.Select(choices=goption,attrs={'class':'form-control border'}))
    phone=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR MOBILE NUMBER','class':'form-control border','autocomplete':"off"}))
    email=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR EMAIL','class':'form-control border','autocomplete':"off"}))
    password=forms.CharField(min_length=5,widget=forms.PasswordInput(attrs={'placeholder': 'CREATE PASSWORD','class':'form-control border','autocomplete':"off"}))
    cpassword=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'CONFIRM PASSWORD','class':'form-control border','autocomplete':"off"}))
    accept=forms.BooleanField()