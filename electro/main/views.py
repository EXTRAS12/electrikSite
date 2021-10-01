from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import WorkList, Category, PriceCategory
from .forms import CallForm
from django.core.mail import send_mail
from django.contrib import messages


def base_page(request):
    return render(request, 'index.html')


def get_category(request):
    categories = Category.objects.all
    prices = PriceCategory.objects.all
    context = {
        'prices': prices,
        'categories': categories,
    }
    return render(request, 'price_list.html', context=context)


def work(request):
    works = WorkList.objects.all()
    context = {
        'works': works,
        'title': 'Фотокарточки',
        'content': 'Контент',
        'photo': 'Фото',
 }
    return render(request, 'work.html', context=context)


def comments(request):
    return render(request, 'comments.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def contacts(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'extra-kent@mail.ru', ['intfloatwork@yandex.ru'], fail_silently=True)
            if mail:
                messages.success(request, 'Отправлено')
                return redirect('about')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')

    else:
        form = CallForm()
    return render(request, 'contacts.html', {"form": form})


