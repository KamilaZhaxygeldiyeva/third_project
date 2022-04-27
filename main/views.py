from django.shortcuts import render
from django.core.mail import  EmailMessage, send_mail
#from .models import Universities
# Create your views here.
def index(request):
    #universities = Universities.objects.all
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

#def courses(request):
    #return render(request, 'main/courses.html')

def send_message(request):
    '''send_mail('Topic', 'Content', '200103315@stu.sdu.edu.kz', ['200103315@stu.sdu.edu.kz'], fail_silently=False,
              html_message='<li><ul>1</ul><ul>2</ul></li>')
    '''
    email = EmailMessage(
        'Topic',
        'This is my message',
        '200103315@stu.sdu.edu.kz',
        ['200103315@stu.sdu.edu.kz'],
        headers={'Message-ID': '2'}
    )
    email.attach_file('D://1//la.txt')
    email.send(fail_silently=False)
    return render(request, 'main/successful.html')