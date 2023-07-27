from django import forms
from .models import Resume
from datetime import datetime
GENDER_CHOICE=(
    ('Male','Male'),
    ('Female','Female')
)

JOB_CITY_CHOICE=[
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Ranchi','Ranchi'),
    ('Mumbai','Mumbai'),
    ('Bhubaneswar','Bhubaneswar'),
    ('Bengaluru','Bengaluru'),
    ('Sambalpur','Sambalpur'),    
]
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label="Preferred Job Locations",choices=JOB_CITY_CHOICE,
                                       widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields="__all__"
        labels={'dob':'Date Of Birth','pin':'PIN Code','mobile':'Mobile Number','email':'Email id'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                 'gender':forms.Select(attrs={'class':'form-control'}),
                 'locality':forms.TextInput(attrs={'class':'form-control'}),
                 'city':forms.TextInput(attrs={'class':'form-control'}),
                 'pin':forms.TextInput(attrs={'class':'form-control'}),
                 'state':forms.Select(attrs={'class':'form-select'}),
                 'mobile':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'job_city':forms.TextInput(attrs={'class':'form-control'}),
                 'profile_image':forms.FileInput(attrs={'class':'form-control'}),
                 'document_file':forms.FileInput(attrs={'class':'form-control'}),}
        
    def clean_pin(self):
        pin=self.cleaned_data['pin']
        if pin>999999:
            raise forms.ValidationError("PIN must be 6 digit only.")
        if len(str(pin))!=6:
            raise forms.ValidationError("must be 6 digit")
        return pin
    
    def clean_email(self):
        eml=self.cleaned_data['email']
        elist=Resume.objects.values_list('email',flat=True)
        if eml in elist:
            raise forms.ValidationError("Email id already exist. Try with another Email id")
        return eml
    
    def clean_mobile(self):
        mobile=self.cleaned_data['mobile']
        if len(str(mobile))!=10:
            raise forms.ValidationError("Mobile number must be 10 digit only ! ")
        mobiles=Resume.objects.values_list('mobile',flat=True)
        if mobile in mobiles:
            raise forms.ValidationError("Mobile number already Exist. Please try with another one !")
        return mobile
        
        