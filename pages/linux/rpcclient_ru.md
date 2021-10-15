# rpcclient

> Клиентская утилита для работы с протоколом MS-RPC (часть оснастки `samba`).

- Присоединиться к удалённому хосту:

`rpcclient --user {{domain}}\{{username}}%{{password}} {{ip}}`

- Присоединиться к удалённому хосту в домен без пароля:

`rpcclient --user {{username}} --workgroup {{domain}} --no-pass {{ip}}`

- Присоединиться к удалённому хосту, передам хеш пароля:

`rpcclient --user {{domain}}\{{username}} --pw-nt-hash {{ip}}`

- Выполнить команду оболочки командной строки на удалённом хосте:

`rpcclient --user {{domain}}\{{username}}%{{password}} --command {{semicolon_separated_commands}} {{ip}}`

- Вывести список пользователей домена:

`rpcclient $> enumdomusers`

- Вывести привелегии:

`rpcclient $> enumprivs`

- Вывести информацию об указанном пользователе:

`rpcclient $> queryuser {{username|rid}}`

- Создать нового пользователя в домене:

`rpcclient $> createdomuser {{username}}`
