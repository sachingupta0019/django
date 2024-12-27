from django import forms
from .models import Resume

GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
jOB_LOCATION_CHOICES = [
    ('Delhi', 'Delhi'),
    ('Noida', 'Noida'),
    ('Ahemdabad', 'Ahemdabad'),
    ('Pune', 'Pune'),
    ('Hyderabad', 'Hyderabad'),
    ('Banglore', 'Banglore'),
]
class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': ''}))
    preferred_location = forms.MultipleChoiceField(choices=jOB_LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {
            'name' : 'Full Name',
            'user_file' : 'Upload Resume',
            'preferred_location' : 'Preferred Location'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email_id' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'phone_no' : forms.TextInput(attrs={'class' : 'form-control'}),
            'dob' : forms.DateInput(attrs={'class' : 'form-control',  
                                            'type': 'date',
                                            'min': '1950-01-01',
                                            'max': '2024-12-31',
                                            'placeholder': 'YYYY-MM-DD'}),
            'landmark' : forms.TextInput(attrs={'class' : 'form-control'}),
            'city' : forms.TextInput(attrs={'class' : 'form-control'}),
            'zip_code' : forms.TextInput(attrs={'class' : 'form-control'}),
            'state' : forms.Select(attrs={'class' : 'form-select',}),
            'user_file' : forms.ClearableFileInput(attrs={'class' : 'form-control', 'type' : 'download'}),
            'profile_img' : forms.ClearableFileInput(attrs={'class' : 'form-control'}),
            'country' : forms.TextInput(attrs={'class' : 'form-control'}),
        }