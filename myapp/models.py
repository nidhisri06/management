from django.db import models

class Visitor(models.Model):
    visitor_id=models.PositiveIntegerField(unique=True)
    Visitor_name=models.CharField(max_length=100)
    Visitor_email=models.EmailField()
    Category=models.CharField(max_length=50)
    Document=models.FileField(upload_to='visitors document')
    Appointment_Date=models.DateField()
    Appointment_Time=models.TimeField()
    reason=models.TextField()
    designated_attendee = models.CharField(max_length=100)
    document = models.FileField(upload_to='visitor_documents/', null=True, blank=True)  

    def _str_(self):
       return self.visitor_name