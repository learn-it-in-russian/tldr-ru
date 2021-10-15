# uncrustify

> Форматтер кода для языков программирования C, C++, C#, D, Java и Pawn.

- Отформатировать один файл:

`uncrustify -f {{path/to/file.cpp}} -o {{path/to/output.cpp}}`

- Читает имена файлов со стандартного ввода (stdin), и создаёт файлы бекапов перед записью результата на место оригинальных файлов:

`find . -name "*.cpp" | uncrustify -F - --replace`

- Не создаёт файлы бекапов (полезно, если файлы отслеживаются системой контроля версий):

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- Использовать свой конфигурационный файл и вывести результат форматирования на стандартный поток вывода (stdout):

`uncrustify -c {{path/to/uncrustify.cfg}} -f {{path/to/file.cpp}}`

- Задаёт явно значение переменной конфигурации:

`uncrustify --set {{option}}={{value}}`

- Генерирует новый конфигурационный файл:

`uncrustify --update-config -o {{path/to/new.cfg}}`
