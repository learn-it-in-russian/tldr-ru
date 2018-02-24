# host

> Поиск доменного имени сервера.

- Поиск A, AAAA, и MX записей указанного домена:

`host {{domain}}`

- Поиск записи (CNAME, TXT,...) для домена:

`host -t {{field}} {{domain}}`

- Обратный поиск имени по IP:

`host {{ip_address}}`
