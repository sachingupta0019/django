from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import BlogPost


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label="Confirm Password (again)", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1', 'password2']
        labels = {
            'username' : 'Username',
            'first_name' : 'First Name',
            'last_name' : "Last Name",
            'email' : 'E-mail',
        }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'class' : 'form-control', 'autocomplete' : 'Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'form-control'}))


class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','excerpt', 'post_thumbnail','post_image','content','post_tag','author_name']
        labels  = {
            'title' : 'Title',
            'excerpt' : 'Description',
            'post_thumbnail' : 'Thumbnail Image',
            'post_image' : 'Featured Image',
            'content' : 'Post Content',
            'post_tag' : 'Tags',
            'author_name' : 'Author',
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'excerpt' : forms.Textarea(attrs={'class' : 'form-control text-area-desc'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
            'post_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'post_thumbnail': forms.ClearableFileInput(attrs={
                'class': 'form-control custom-file-input',
                'id': 'post_thumbnail'
            }),
            'post_image': forms.ClearableFileInput(attrs={
                'class': 'form-control custom-file-input',
                'id': 'post_image'}),
            # 'post_thumbnail' : forms.ImageField(label='Upload Thumbnail Image'),
        }

