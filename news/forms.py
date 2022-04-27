from .models import Comment
from .models import Authorizing
from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput




class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'text', 'date_at']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'comment'
            }),
            "date_at": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'data of comment'
            })
        }

class AuthorizeForm(forms.Form):
    username = forms.CharField( max_length=200,label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField( max_length=200, label='Surname')
    education = forms.CharField(max_length=300,label='Educations', widget=forms.TextInput(attrs={'class': 'form-input'}))
    birth_date = forms.DateField(label='Date of birthday')
    password = forms.CharField( max_length=200, label='Password')
    city = forms.CharField( max_length=200, label='City')
    email = forms.EmailField( max_length=300, label='Email')
    phone = forms.CharField( max_length=400, label='Phone number')

    '''class Meta:
        model = Authorizing
        fields = '__all__'

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'surname'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
            "education": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'education'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'city'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'phone'
            }),
            "birth_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'data of birthday'
            })
        
        }'''