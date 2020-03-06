from django.shortcuts import render




# Create your views here.

def home(request):
    template = 'index.html'

    return render(request, template)

def portfolio(request):
    template = 'portfolio.html'

    return render(request, template)

def contacts(request):
    template = 'contacts.html'

    return render(request, template)

def services(request):
    template = 'services.html'

    return render(request, template)

def testimonial(request):
    template = 'testimonial.html'

    return render(request, template)


def blog(request):
    template = 'blog.html'

    return render(request, template)

def pricing(request):
    template = 'pricing.html'

    return render(request, template)

def FAQs(request):
    template = 'FAQs.html'

    return render(request, template)