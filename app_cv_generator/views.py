from django.shortcuts import render
from .models import *
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
def cv_form(request):
    if request.method=="POST":
        name=request.POST.get('name', "")
        address=request.POST.get('address', "")
        city=request.POST.get('city', "")
        state=request.POST.get('state', "")
        pin_code=request.POST.get('pin_code', "")
        contact_number=request.POST.get('contact_number', "")
        email=request.POST.get('email', "")
        linkedin_id=request.POST.get('linkedin_id', "")
        summary=request.POST.get('summary', "")
        skills=request.POST.get('skills', "")
        experience=request.POST.get('experience', "")
        higher_secondary=request.POST.get('higher_secondary', "")
        degree=request.POST.get('degree', "")
        certificates=request.POST.get('certificates', "")
        projects=request.POST.get('projects', "")

        profile=Profile(
            name=name,
            address=address,
            city=city,
            state=state,
            pin_code=pin_code,
            contact_number=contact_number,
            email=email,
            linkedin_id=linkedin_id,
            summary=summary,
            skills=skills,
            experience=experience,
            higher_secondary=higher_secondary,
            degree=degree,
            certificates=certificates,
            projects=projects,
        )
        profile.save()
    return render(request, 'app_cv_generator/cv_form.html', )

def cv(request, id):
    user_profile=Profile.objects.get(pk=id)
    template=loader.get_template('app_cv_generator/cv.html')
    html=template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    config = pdfkit.configuration(wkhtmltopdf=r"C:\wkhtmltox\bin\wkhtmltopdf.exe")
    pdf=pdfkit.from_string(html, False, options, configuration=config)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename='resume.pdf'
    return response

def cv_list(request):
    profiles=Profile.objects.all()
    return render(request, 'app_cv_generator/cv_list.html', {'profiles':profiles})