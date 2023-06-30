from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(UserCreationForm):
    rollno = forms.IntegerField( widget=(forms.NumberInput(attrs={'autofocus': True,'placeholder':'RollNo'})))
    name = forms.CharField(  widget=(forms.TextInput(attrs={'placeholder':'Name'})))
    email = forms.CharField(  widget=(forms.TextInput(attrs={'placeholder':'Email'})))
    mobileNo = forms.IntegerField(  widget=(forms.NumberInput(attrs={'placeholder':'Mobile'})))
    address = forms.CharField(  widget=(forms.TextInput(attrs={'placeholder':'Address'})))
    
    
    class Meta:
        model = User
        fields = ['rollno','name','mobileNo','email','address']
    
    def clean(self):
        super(StudentForm,self).clean()
        # extract mobile Number
        mobileNo = self.cleaned_data.get('mobileNo')
        if len(str(mobileNo))!=10:
            self._errors['mobileNo'] = self.error_class([
                'Mobile Number Should be 10 digits'])
        return self.cleaned_data