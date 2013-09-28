from django.shortcuts import render
from .models import Activation


def activate(request):
    key = request.GET.get('key', '')
    user = Activation.objects.activate(key)
    if not user:
        raise Http404
    return render(request, 'accounts/activation_success.html')
