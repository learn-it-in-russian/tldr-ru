# ab

> Средства тестирования Apache (Apache Benchmark). Простейшая утилита для проведения нагрузочных тестов.

- Сделать 100 HTTP GET запросов на данный URL:

`ab -n 100 {{url}}`

- Сделать 100 HTTP GET запросов, выполняющихся до 10 запросов одновременно, на данный URL Execute 100 HTTP GET requests, processing up to 10 requests concurrently, to given URL:

`ab -n 100 -c 10 {{url}}`
