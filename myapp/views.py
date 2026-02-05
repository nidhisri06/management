from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponse
from .models import Visitor  # ONLY import Visitor
from django.conf import settings
from django.contrib import messages

def reschedule_meet(request, id):
    visitor = get_object_or_404(Visitor, id=id)

    if request.method == 'POST':
        visitor.appointment_date = request.POST.get('date')
        visitor.appointment_time = request.POST.get('time')
        visitor.status = 'Rescheduled'
        visitor.save()
        return redirect('dashboard')
  
def delete_meet(request, id):
    Visitor.objects.filter(id=id).delete()
    return redirect('dashboard')



def home(request):
    return render(request, 'home.html')

def dashboard(request):
    visitors = Visitor.objects.all().order_by('-appointment_date')
    return render(request, 'dashboard.html', {'visitors': visitors})

def accept_meet(request, id):
    meet = get_object_or_404(Visitor, id=id)
    meet.status = 'Approved'  # Capital A to match model choices
    meet.save()
    return redirect('Approved Meet')

def reject_meet(request, id):
    visitor = get_object_or_404(Visitor, id=id)
    visitor.status = 'Rejected'  # Capital R
    visitor.save()
    return redirect('Rejected Meet')


def visitor_registration(request):
    if request.method == 'POST':
        try:
            # Get form data
            visitor_name = request.POST.get('visitor_name')
            visitor_email = request.POST.get('visitor_email')
            appointment_date = request.POST.get('appointment_date')
            appointment_time = request.POST.get('appointment_time')
            category = request.POST.get('category')
            reason = request.POST.get('reason')
            designated_attendee = request.POST.get('designated_attendee')
            
            # GENERATE VISITOR_ID
            # Get the last visitor's ID or start from 101
            last_visitor = Visitor.objects.order_by('-visitor_id').first()
            if last_visitor:
                next_visitor_id = last_visitor.visitor_id + 1
                # Make sure the ID is unique (just in case)
                while Visitor.objects.filter(visitor_id=next_visitor_id).exists():
                    next_visitor_id += 1
            else:
                next_visitor_id = 101  # Start from 101 if no visitors exist
            
            # Create visitor with visitor_id
            visitor = Visitor.objects.create(
                visitor_id=next_visitor_id,  # ADDED THIS LINE
                visitor_name=visitor_name,
                visitor_email=visitor_email,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                category=category,
                reason=reason,
                designated_attendee=designated_attendee,
                status='Pending'  # REQUIRED FIELD
            )
            
            # Handle file upload
            if 'document' in request.FILES:
                visitor.document = request.FILES['document']
                visitor.save()
            
            # Optional: Send email notifications (uncomment if needed)
            """
            # Send email to attendee
            attendee_email_mapping = {
                'Member 1': 'nidhisri06@gmail.com',
                'Member 2': 'nidhisri06@gmail.com',
                'General': 'nidhisri06@gmail.com'
            attendee_email = attendee_email_mapping.get(designated_attendee)
            
            if attendee_email:
                send_mail(
                    f'New Visitor Scheduled - {visitor_name}',
                    f'Visitor {visitor_name} has scheduled an appointment.',
                    settings.EMAIL_HOST_USER,
                    [attendee_email],
                    fail_silently=False,
                )
            """
            
            messages.success(request, f'Registration successful! Your Visitor ID: {next_visitor_id}')
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('visitor_registration')
    
    return render(request, 'home.html')