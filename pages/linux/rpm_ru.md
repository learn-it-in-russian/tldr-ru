# rpm

> Менеджер пакетов RPM.

- Вывести версию пакета httpd:

`rpm -q {{httpd}}`

- Вывести версии пакетов, подходящих заданной маске:

`rpm -qa '{{mariadb*}}'`

- Определить пакет, который предоставляет данный файл, и вывести версию этого пакета:

`rpm -qf {{/etc/postfix/main.cf}}`

- Вывести список файлов, которые предоставляются пакетом:

`rpm -ql {{kernel}}`

- Вывести скриптлеты(управляющие процессом установки и удаления пакета) для заданного файла:

`rpm -qp --scripts {{some.rpm}}`

- Показать отличающиеся, недостающие и/или некорректно установленные файлы пакетов, подходящих заданной маске:

`rpm -Va '{{php-*}}'`