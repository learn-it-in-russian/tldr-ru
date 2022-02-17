# ajson

> Выполняет JSONPath на JSON объектах.

- Прочитать JSON из файла и выполнить указанное JSONPath выражение:

`ajson '{{$..json[?(@.path)]}}' {{path/to/file.json}}`

- Читает JSON со стандартного потока ввода (stdin) и выполняет определённое JSONPath выражение:

`cat {{path/to/file.json}} | ajson '{{$..json[?(@.path)]}}'`

- Читаем JSON с URL и выполняем JSONPath:

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- Читаем переданный JSON и вычисляем значение:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
