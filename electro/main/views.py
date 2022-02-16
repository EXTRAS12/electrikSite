from django.shortcuts import render, redirect
from .models import WorkList, Category, PriceCategory
from .forms import CallForm
from django.core.mail import send_mail
from django.contrib import messages


def base_page(request):
    """Главная страница"""
    return render(request, 'main/index.html')


def get_category(request):
    """Категорий"""
    categories = Category.objects.all()
    prices = PriceCategory.objects.all().select_related('category')
    context = {
        'prices': prices,
        'categories': categories,
    }
    return render(request, 'main/price_list.html', context=context)


def our_work(request):
    """Наши работы"""
    works = WorkList.objects.all()
    context = {
        'works': works,
        'title': 'Фото для Вас',
        'content': 'Контент',
        'photo': 'Фото', }
    return render(request, 'main/work.html', context=context)


def about(request):
    """Страница о нас"""
    return render(request, 'main/about.html')


def contacts(request):
    """Контакты"""
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],
                             form.cleaned_data['content'], 'akkurat-energo.info@yandex.ru',
                             ['akkurat-energo@yandex.ru'], fail_silently=True)
            if mail:
                messages.success(request, 'Отправлено')
                return redirect('price')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')

    else:
        form = CallForm()
    return render(request, 'main/contacts.html', {"form": form})
