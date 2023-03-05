"""
Файл для создания и регистрации собственных фильтров
"""
from django import template

register = template.Library()  # Необходимо зарегистрировать наш фильтр, чтобы Django знал, где его искать. Чтобы
# использовать фильтр, нужно в HTML-шаблоне прописать следующий тэг: {% load custom_filters %}

censor_list = ['матёрый', 'волк', 'редиска', 'белка', 'белке', 'белку', 'подлый', 'грызун']  # Список цензуры


@register.filter(name='censor')  # Декоратор register.filter() указывает Django, что нужно запомнить про
# # существование нового фильтра. Регистрируем наш фильтр под именем censor, чтоб Django понимал, что это именно
# # фильтр, а не простая функция
def censor(value):
    if not isinstance(value, str):  # Проверка, что значение (value) является строкой (str),
        raise ValueError('Ценз только строк!')  # в ином случае вызывается исключение

    for word in censor_list:  # В цикле проходим по тексту, если слово входит в список цензуры,
        value = value.replace(word[1:], '*' * (len(word)-1))  # то делаем замену (метод replace) этого слова на "*" со
        # второй буквы в слове. Функция len() возвращает длину (количество элементов) в объекте word (минус 1 элемент)
    return value  # и возвращаем значение