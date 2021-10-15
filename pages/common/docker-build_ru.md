# docker build

> Собирает docker образ из Dockerfile.

- Собрать docker образ, используя Dockerfile из текущей директории:

`docker build .`

- Собрать docker образ из файла Dockerfile по указанному URL:

`docker build {{github.com/creack/docker-firefox}}`

- Собрать docker образ и задать метку (`-t` -- короткая версия ключа):

`docker build --tag {{name:tag}} .`

- Построить docker образ из переданного файла:

`docker build --tag {{name:tag}} - < {{Dockerfile}}`

- Не использовать кеш при сборке образа:

`docker build --no-cache --tag {{name:tag}} .`

- Построить docker образ, используя указанный файл Dockerfile:

`docker build --file {{Dockerfile}} .`

- Собрать с указанными переменными сборки:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
