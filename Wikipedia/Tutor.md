# Введение в Wikipedia

Wikipedia - пакет python для работы с одним из самых популярныз сайтов - википедия. На этом сайте можно найти всё, что угодно, а в этой статье вы научитесь этот процесс оптимизировать.
Установка:

```python
pip install wikipedia
```

## Класс `WikipediaPage`

Объект типа `WikipediaPage` можно создать с помощью метода `WikipediaPage`:

```python
import wikipedia as wiki

wiki.set_lang('ru') # Устанавливаем русский язык

page = wiki.page('wikipedia') # Открываем страницу с названием "wikipedia"
print(page.content) # Печатаем содержание страницы
```

С помощью `html()` можно получить html-код страницы. `images` возвращает url-адреса изображений. `links` - все ссылки в странице.

## Исключения

Если время ожидания ответа от сервера будет превышено (например, если у вас плохой интернет), то будет вызванно `HTTPTimeoutError`.
Если страницы не существует, будет вызванно `PageError`.

[Официальная документация](https://wikipedia.readthedocs.io/en/latest/code.html#api)
