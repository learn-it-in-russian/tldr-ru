# choco new

> Генеирует файлы спецификации для нового пакета Chocolatey.

- Создаёт шаблон для нового пакета:

`choco new {{package_name}}`

- Создаёт скелет проекта с указанной версией:

`choco new {{package_name}} --version {{version}}`

- Указываем имя ответственного за сборку для нового пакета:

`choco new {{package_name}} --maintainer {{maintainer_name}}`

- Создаём новый пакет в указанной директории:

`choco new {{package_name}} --output-directory {{path/to/directory}}`

- Создаём новый пакет с разными url для 32-bit и 64-bit версий:

`choco new {{package_name}} url="{{url}}" url64="{{url}}"`
