from django.db import models

# Create your models here.
class Resume(models.Model):
    INDIAN_STATES = [
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CT', 'Chhattisgarh'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OR', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TS', 'Telangana'),
    ('TR', 'Tripura'),
    ('UP', 'Uttar Pradesh'),
    ('UK', 'Uttarakhand'),
    ('WB', 'West Bengal')
]

    name = models.CharField(max_length=256)
    email_id = models.EmailField()
    phone_no = models.PositiveIntegerField()
    dob = models.DateField(auto_now = False, auto_now_add = False)
    gender = models.CharField(max_length=10)
    profile_img = models.ImageField(upload_to='media/candidates_images', blank=True)
    landmark = models.CharField(max_length=520)
    city = models.CharField(max_length=128)
    zip_code = models.PositiveIntegerField()
    state = models.CharField(choices= INDIAN_STATES, max_length=128)
    country = models.CharField(max_length=128, default="INDIA")
    preferred_location = models.CharField(max_length=128)
    user_file = models.FileField(upload_to='document/', blank=True)

    def __str__(self):
        return self.name
