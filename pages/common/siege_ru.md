# siege

> Инструменты для нагрузочного HTTP тестирования.

- Проверить URL, используя настройки по умолчанию:

`siege {{https://example.com}}`

- Проверить список URL-ов:

`siege --file {{path/to/url_list.txt}}`

- Проверить список URL-ов в случайном порядке (Симулирует стандартный трафик):

`siege --internet --file {{path/to/url_list.txt}}`

- Проверяет производительность списка URL-ов (без ожидания между запросами):

`siege --benchmark --file {{path/to/url_list.txt}}`

- Устанавливает количество конкурентных соединений:

`siege --concurrent={{50}} --file {{path/to/url_list.txt}}`

- Устанавливает, как долго будет продолжаться тестирование (осада):

`siege --time={{30s}} --file {{path/to/url_list.txt}}`
