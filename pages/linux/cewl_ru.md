# cewl

> URL парсер сайтов для получения списка слов, специфичных для данного сайта.

- Записать список слов в файл, используя переданный URL, углубляяся не более чем на 2 ссылки в глубину:

`cewl --depth {{2}} --write {{path/to/wordlist.txt}} {{url}}`

- Вывести с количеством включений список слов длинны не менее указанной (минимум 5 символов):

`cewl --with-numbers --min_word_length {{5}} {{url}}`

- Вывести список слов по данному url в режиме отладки, также выводить найденные email адреса:

`cewl --debug --email {{url}}`

- Использовать HTTP Basic или Digest аутентификацию:

`cewl --auth_type {{basic|digest}} --auth_user {{username}} --auth_pass {{password}} {{url}}`

- Использовать прокси:

`cewl --proxy_host {{host}} --proxy_port {{port}} {{url}}`
