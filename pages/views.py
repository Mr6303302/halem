from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .models import project, main_project, project_image


def index(request):
    return render(request, 'Halem/index.html')


def work(request):
    return render(request, 'Halem/work.html', {'pro': project.objects.all()})


def cv(request):
    return render(request, 'Halem/cv.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_from = request.POST['email']
        subject = request.POST['subject']
        message1 = request.POST['message']
        x = {'x': 'sucsseful'}
        # headers = {'Reply-To': from_email}
        message =  name +"\n\n"+ message1 
        if message and subject and email_from:
           try:
                email = EmailMessage(
                subject=subject,
                body=message,
                from_email=email_from,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email_from],
                     ) 
                email.send()
                messages.success(request, 'message sent successful')
                return render(request, 'Halem/contact.html')
           except BadHeaderError:
                messages.error(request, 'make sure all filed is filled')
                return render(request, 'Halem/contact.html')
        else:
            messages.error(request, 'make sure all filed is filled')
            return render(request, 'Halem/contact.html')
    return render(request, 'Halem/contact.html')



    

def projec(request, id):
    if id == 5:
        return render(request, 'Halem/projects/5/p5.html', {'images': project_image.objects.filter(id_n=id)})
    else:
        return render(request, 'Halem/projects/frist/p1.html', {'project': main_project.objects.get(id=id), 'images': project_image.objects.filter(id_n=id)})


# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(name, message, from_email, [settings.EMAIL_HOST_USER])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')
