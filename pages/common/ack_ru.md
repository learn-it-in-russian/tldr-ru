# ack

> Инструмент поиска, как grep, но оптимизированный для программистов.

- Найти файлы, содержащие "foo":

`ack {{foo}}`

- Найти файлы, написанные на определённом языке программирования:

`ack --ruby {{each_with_object}}`

- Посчитать общее число вхождений слова "foo":

`ack -ch {{foo}}`

- Показать имена файлов, содержащих "foo", и количество вхождений в каждом файле:

`ack -cl {{foo}}`
