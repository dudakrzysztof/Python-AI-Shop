from django.shortcuts import redirect, render
from .forms import SubscribeForm
from .models import Subscriber

def subscribe(request):
    form = SubscribeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        Subscriber.objects.update_or_create(email=form.cleaned_data["email"], defaults={"subscribed": True})
        return render(request, "newsletter/result.html", {"message": "You are subscribed."})
    return render(request, "newsletter/form.html", {"form": form})

def unsubscribe(request):
    form = SubscribeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        Subscriber.objects.filter(email=form.cleaned_data["email"]).update(subscribed=False)
        return render(request, "newsletter/result.html", {"message": "You are unsubscribed."})
    return render(request, "newsletter/form.html", {"form": form, "unsubscribe": True})
