# wrk

> Программа для тестирования нагрузки HTTP серверов.

- Запустить тестирование нагрузки на `30` секунд, используя `12` потоков исполнения, и держать `400` открытых HTTP соединений:

`wrk -t{{12}} -c{{400}} -d{{30s}} "{{http://127.0.0.1:8080/index.html}}"`

- Запустить нагрузочное тестирование с дополнительным указанным HTTP заголовком:

`wrk -t{{2}} -c{{5}} -d{{5s}} -H "{{Host: example.com}}" "{{http://example.com/index.html}}"`

- Запустить нагрузочное тестирование с таймаутом на ответ в `2` секунды:

`wrk -t{{2}} -c{{5}} -d{{5s}} --timeout {{2s}} "{{http://example.com/index.html}}"`
