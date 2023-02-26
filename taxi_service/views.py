from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages

from taxi_service.forms import SubscriberForm, MainOrderForm


def index(request):
    sub_form = SubscriberForm()
    order_form = MainOrderForm()

    if request.method == "POST":
        if "order_form" in request.POST:
            order_form = MainOrderForm(request.POST)
            if order_form.is_valid():
                order_form.save()
                messages.success(request, 'Order accepted', extra_tags='order')
                return HttpResponseRedirect(reverse('index'))
        elif "subscribe_form" in request.POST:
            sub_form = SubscriberForm(request.POST)
            if sub_form.is_valid():
                sub_form.save()
                messages.success(request, 'Thank you for subscribing', extra_tags='subscribe')
                return HttpResponseRedirect(reverse('index'))

    context = {
        "subscribe_form": sub_form,
        "order_form": order_form,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def why(request):
    return render(request, 'why.html')





