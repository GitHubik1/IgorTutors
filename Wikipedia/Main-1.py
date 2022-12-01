import wikipedia as wiki

wiki.set_lang('ru') # Устанавливаем русский язык

page = wiki.page('wikipedia') # Открываем страницу с названием "wikipedia"
print(page.content) # Печатаем содержание страницы