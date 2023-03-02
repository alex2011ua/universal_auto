from django.http import JsonResponse
from django.shortcuts import render


from taxi_service.forms import SubscriberForm, MainOrderForm


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def index(request):
    sub_form = SubscriberForm(prefix='subscriber')
    order_form = MainOrderForm(prefix='order')

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if "order_form" in request.POST:
            order_form = MainOrderForm(request.POST, prefix='order')
            if order_form.is_valid():
                order_form.save()
                order_form = MainOrderForm(prefix='order')

        elif "subscribe_form" in request.POST:
            sub_form = SubscriberForm(request.POST, prefix='subscriber')
            if sub_form.is_valid():
                sub_form.save()
                sub_form = SubscriberForm(prefix='subscriber')

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





