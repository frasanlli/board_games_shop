from django.shortcuts import render
from service_app.models import Service

# Create your views here.
def service (request):

    services = Service.objects.all()
    return render(request, "service_app/service.html", {"services": services})
