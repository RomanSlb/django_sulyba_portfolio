from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .models import Post
from django.core.mail import send_mail
from django.conf import settings
import os
from xhtml2pdf import pisa


def render_pdf_view(request):
    template_path = 'portfolio/pages/ppdd.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def home_view(request):
    posts = Post.objects.all()
    return render(request, 'portfolio/pages/home.html', {'posts': posts})


def about_me(request):
    return render(request, 'portfolio/about.html')


def contact_me_view(request):
    return render(request, 'portfolio/pages/contact.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'portfolio//pages/projects.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status='published', slug=post, publish__year=year,
                             publish__month=month, publish__day=day)
    return render(request, 'portfolio/pages/detail.html', {'post': post})

