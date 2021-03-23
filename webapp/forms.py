from django import forms
from django.core import validators
from.models import User
class RegistrationForm(forms.Form):
    fname=forms.CharField(max_length=10)
    lname=forms.CharField(max_length=10)
    email=forms.EmailField(max_length=30)
    password=forms.CharField(max_length=20)
    conform_password=forms.CharField(max_length=20)
    def clean(self):
        all_data=super().clean()
        un=all_data['email']
        u=User.objects.all().values('email')
        ul=[i['email'] for i in u]
        if un in ul:
            raise forms.ValidationError('email allready exist please try again!')
        print(ul)
        p1=all_data['password']
        l=len(p1)
        p2=all_data['conform_password']
        if p1!=p2 and l!=8:
            raise forms.ValidationError('paaswords must be more than 8 digits \n both password must be same\n ')

        '''
            for i in p1:
                raise forms.ValidationError('paaswords must be more than 8 digits \n both password must be same')'''


