from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.
def main_page(request):
    context = autor
    return render(request, 'index.html', context)

def about_page(request):
    context = autor
    return render(request, 'about.html', context)

def item_page(request, item_id: int):
    item = next((x for x in items if x["id"] == item_id), None)
    context = {'item': item}
    if item:
        return render(request, 'item.html', context)

    html_practice = f'Товар с id={item_id} не найден'
    raise Http404(html_practice)

def itemslist_page(request):
    context = {
        'items': items
    }
    return render(request, 'items_list.html', context)

h1 = '"Изучаем Django"'
#autor_name_surname = 'Круглов Д.М.'
#autor_name = 'Денис'
#autor_patronymic = 'Михайлович'
#autor_surname = 'Круглов'
#autor_fhone = '8-903-232-08-02'
#autor_email = 'kruglovdm@mail.ru'

autor = {
   'name_surname': 'Круглов Д.М.',
   'name': 'Денис',
   'patronymic': 'Михайлович',
   'surname': 'Круглов',
   'phone': '8-903-232-08-02',
    'email': 'kruglovdm@mail.ru'
}

items = [
    {'id': 1, 'name': 'Кроссовки abibas', 'quantity': 5},
    {'id': 2, 'name': 'куртка кожанная', 'quantity': 2},
    {'id': 3, 'name': 'Coca-cola 1 литр', 'quantity': 12},
    {'id': 4, 'name': 'Картофель фри', 'quantity': 0},
    {'id': 5, 'name': 'Кепка', 'quantity': 124},
    {'id': 6, 'name': 'Ремень', 'quantity': 1},
]
