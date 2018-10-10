# base64

> Encode and decode using Base64 representation.

- Зашифровать файл:

`base64 -i {{plain_file}}`

- Расшифровать файл:

`base64 -D -i {{base64_file}}`

- Зашифровать данные из потока stdin:

`echo {{plain_text}} | base64`

- Расшифровать данные из потока stdin:

`echo {{base64_text}} | base64 -D`
