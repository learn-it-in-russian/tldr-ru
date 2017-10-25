# ssh-copy-id

> Прописывает ваш публичный ключ в файл authorized_keys удаленной машины.

- Скопировать ваши ключи на удаленную машину:

`ssh-copy-id {{username@remote_host}}`

- Скопировать заданый публичный ключ на удаленную машину:

`ssh-copy-id -i {{path/to/certificate}} {{username}}@{{remote_host}}`

- Скопировать заданый публичный ключ на удаленную машину с заданым портом ssh:

`ssh-copy-id -i {{path/to/certificate}} -p {{port}} {{username}}@{{remote_host}}`
