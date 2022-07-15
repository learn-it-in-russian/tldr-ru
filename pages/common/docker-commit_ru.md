# docker commit

> Создаёт новый образ из изменений контейнера.

- Создать новый образ из указанного контейнера:

`docker commit {{container}} {{image}}:{{tag}}`

- Применить `CMD` инструкцию Dockerfile для создания образа:

`docker commit --change="CMD {{command}}" {{container}} {{image}}:{{tag}}`

- Добавить переменную окружения `ENV` из Dockerfile к создаваемому образу:

`docker commit --change="ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- Добавляем данные мета-данных (автор) к создаваемому из контейнера образу:

`docker commit --author="{{author}}" {{container}} {{image}}:{{tag}}`

- Комментируем создаваемый образ из контейнера:

`docker commit --message="{{comment}}" {{container}} {{image}}:{{tag}}`

- Создаём образ из docker контейнера, но не останавливаем оригинальный контейнер:

`docker commit --pause={{false}} {{container}} {{image}}:{{tag}}`

- Вывести подсказки:

`docker commit --help`
