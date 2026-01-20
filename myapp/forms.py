from django import forms
from .models import Profile
from .models import Visitor

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_picture','name','emp_id','email',
            'designation','department','reporting_to','mobile'
        ]



class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'visitor_name','visitor_email','category','appointmrnt_date',
            'appointment_time','reason','designates_attendee','document'
         ]
        


class RescheduleMeetForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['appointment_date', 'appointment_time']  # Allow only date and time to be updated
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }