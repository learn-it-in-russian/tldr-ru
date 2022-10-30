# go build

> Собрать исходники на Go.

- Собрать файл 'пакета main' (вывод будет лежать в файле с тем же именем, но без расширения):

`go build {{path/to/main.go}}`

- Скомпилировать файл, положить результат в указанный файл:

`go build -o {{path/to/binary}} {{path/to/source.go}}`

- Скомпилировать пакет:

`go build -o {{path/to/binary}} {{path/to/package}}`

- Скомпилировать пакет в исполняемый файл, с включённой проверкой состояния гонки:

`go build -race -o {{path/to/executable}} {{path/to/main/package}}`
