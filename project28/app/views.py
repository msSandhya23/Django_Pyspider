from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def registration(request):
    EUMFO = UserForm()
    EPMFO = ProfileForm()
    d = {"EUMFO":EUMFO,"EPMFO":EPMFO}
    if request.method == 'POST' and request.FILES:
        NMUFDO = UserForm(request.POST)
        NMPFDO = ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO = NMUFDO.save(commit = False)
            pw = NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = NMPFDO.save(commit = False)
            MPFDO.username = MUFDO
            MPFDO.save()

            # HTML Message
            html_message = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                        <div style="display:flex; justify-content:center; align-items: center">
                            <img src="https://img.freepik.com/free-vector/stylish-welcome-lettering-banner-join-with-joy-happiness_1017-57675.jpg?t=st=1745672548~exp=1745676148~hmac=1d7e1d7ddea28a3ff028e977fa69b499b3788afbe5795ff7a4233047d7884e70&w=1480" name="welcome" alt="welcomepic" width=400px height=200px />
                        </div>
                        <h2 style="color: #2c3e50;">Welcome to Our Platform!</h2>
                        <p>Dear <strong>{MUFDO.username}</strong>,</p>

                        <p>Thank you for registering with us! Your account has been successfully created.</p>

                        <div style="background-color: #faccff; padding: 15px; border-radius: 5px; margin: 20px 0;">
                            <h3 style="margin-top: 0;">Your Account Details:</h3>
                            <p>Username: <strong style="color: #845ec2">{MUFDO.username}</strong></p>
                            <p>Email: <strong  style="color: #845ec2">{MUFDO.email}</strong></p>
                        </div>

                        <p>We're excited to have you as part of our community!</p>

                        <p style="margin-top: 30px;">Best regards,<br>Sandhya ❣️</p>
                    </div>
                </body>
            </html>
            """
            
            # Plain text version for email clients that don't support HTML
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject='Welcome to Our Platform!',
                message=plain_message,
                html_message=html_message,
                from_email='sandhyabehera33090@gmail.com',
                recipient_list=[MUFDO.email],
                fail_silently=False
            )
            
            return HttpResponse("Registration successful!")
    
    return render(request, 'registration.html',d)