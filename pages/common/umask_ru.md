# umask

> Управляет правами на чтение/запись/исполнение для новых созданных пользователем файлов.

- Выводит текущую маску в восьмеричном виде:

`umask`

- Вывести текущую маску в виде символов (в человеко-читаемом виде):

`umask -S`

- Сменить маску, указывая новую в виде символов, чтобы дать возможность всем пользователям правам на чтение (остальная часть маски остаётся неизменённой):

`umask {{a+r}}`

- Установить маску, указывая новую в виде восьмеричных цифр, чтобы оставить права владельцу, но забрать все права у остальных пользователей:

`umask {{077}}`
