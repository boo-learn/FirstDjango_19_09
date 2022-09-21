from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

author = {
    "name": "Евгений",
    "surname": "Юрченко",
    "phone": "8-923-600-01-02",
    "email": "eyurchenko@specialist.ru"
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 20, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 5, "name": "Кепка", "quantity": 124},
    {"id": 15, "name": "!!!!", "quantity": 124},
]


def main_page(request):
    return render(request, 'index.html')


def about(request):
    result = f"""Имя: <b>{author['name']}</b> <br>
                Фамилия: <b>{author['surname']}</b> <br>
                телефон: <b>{author['phone']}</b> <br>
                email: <b>{author['email']}</b> <br>
    """
    return HttpResponse(result)


def item(request, item_id: int):
    for item in items:
        if item["id"] == item_id:
            context = {
                "item": item
            }
            return render(request, 'item.html', context)
    # return HttpResponseNotFound(f"Item with id={item_id} not found")
    raise Http404(f"Item with id={item_id} not found")


def items_list(request):
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)
