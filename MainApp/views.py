from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main_page(request):
    html_practice = f'<h1>{h1}</h1><strong>Автор</strong>: <i>{autor["name_surname"]}</i>'
    return HttpResponse(html_practice)

def about_page(request):
    html_practice = f'Имя: <strong>{autor["name"]}</strong> <br> ' \
                    f'Отчество: <strong>{autor["patronymic"]}</strong> <br> ' \
                    f'Фамилия: <strong>{autor["surname"]}</strong> <br> ' \
                    f'Телефон: <strong>{autor["fhone"]}</strong> <br> ' \
                    f'email: <strong>{autor["email"]}</strong>'
    return HttpResponse(html_practice)

def item_page(request, item_id):
    item = next((x for x in items if x["id"] == item_id),None)
    if item:
        html_practice = f'Название: <strong>{item["name"]}</strong> <br> ' \
                    f'кол-во: <strong>{item["quantity"]}</strong>'
    else:
        html_practice = f'Товар с id={item_id} не найден'
    html_practice += f'<br> <a href = "/items">назад к списку товаров</a>'
    return HttpResponse(html_practice)

def items_page(request):
    html_practice = '<table><thead>' \
                    '<th></th>' \
                    '<th align="left">Название</th>' \
                    '<th>Кол-во</th>' \
                    '</thead><tbody>'
    for item in items:
       html_practice += f'<tr>' \
                        f'<td>{items.index(item)+1}</td>' \
                        f'<td><a href = "/item/{item["id"]}">{item["name"]}</a></td>' \
                        f'<td>{item["quantity"]}</td>' \
                        f'</tr>'
    html_practice += '</tbody></table>'
    return HttpResponse(html_practice)

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
   'fhone': '8-903-232-08-02',
    'email': 'kruglovdm@mail.ru'
}

items = [
    {'id': 1, 'name': 'Кроссовки abibas', 'quantity': 5},
    {'id': 2, 'name': 'куртка кожанная', 'quantity': 2},
    {'id': 3, 'name': 'Coca-cola 1 литр', 'quantity': 12},
    {'id': 4, 'name': 'Картофель фри', 'quantity': 0},
    {'id': 5, 'name': 'Кепка', 'quantity': 124},
]
