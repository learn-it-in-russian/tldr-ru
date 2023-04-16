# pip install

> Установщик пакетов Python.

- Установить пакет python:

`pip install {{package_name}}`

- Установить указанную (конкретную) версию пакета:

`pip install {{package_name}}=={{package_version}}`

- Установить список пакетов (возможно, с версиями) из файла:

`pip install --requirement {{path/to/requirements.txt}}`

- Установить пакеты из URL или локального файла архива (.tar.gz | .whl):

`pip install --find-links {{url|path/to/file}}`

- Установить локальный пакет в текущей директории для разработки - в редактируемом режиме:

`pip install --editable {{.}}`
