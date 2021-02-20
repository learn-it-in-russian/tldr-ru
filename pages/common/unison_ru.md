# unison

> Программа для двунаправленной синхронизации файлов.

- Синхронизировать две директории (создаёт файл журнала синхронизации для данных двух директорий):

`unison {{path/to/directory_1}} {{path/to/directory_2}}`

- Автоматически принимать (если не конфликтуют):

`unison {{path/to/directory_1}} {{path/to/directory_2}} -auto`

- Игнорирует файлы, подходящие под указанный шаблон:

`unison {{path/to/directory_1}} {{path/to/directory_2}} -ignore {{pattern}}`

- Показать документацию:

`unison -doc {{topics}}`
