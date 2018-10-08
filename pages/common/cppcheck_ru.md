# cppcheck

> Программа статического анализа C/C++ кода.
> Вместо синтаксических ошибока, она нацелена на такие виды ошибок, которые компиляторы обычно не обнаруживают.

- Рекурсивно проверяет текущий каталог, отображая прогресс выполнения и записывать сообщения об ошибках в файл:

`cppcheck . 2> cppcheck.log`

- Рекурсивно проверяет заданный каталог без отображения прогресса выполения:

`cppcheck --quiet {{path/to/folder}}`

- Проверяет файл, выполняя заданные проверки (по-умолчанию ищутся только ошибки - error):

`cppcheck --enable={{error|warning|style|performance|portability|information|all}} {{path/to/file.cpp}}`

- Выводит список доступных тестов, отобранных по заданному шаблону:

`cppcheck --errorlist | grep "{{search pattern}}"`

- Проверяет файл, игнорируя заданные тесты:

`cppcheck --suppress={{test_id1}} --suppress={{test_id2}} {{path/to/file.cpp}}`

- Проверяет текущую папку, задав пути к заголовочным файлам, хранящимся отдельно (например, внешние библиотеки):

`cppcheck -I {{include/folder_1}} -I {{include/folder_2}} .`

- Проверяет проект (`*.vcxproj`) или решение (`*.sln`) Microsoft Visual Studio:

`cppcheck --project={{path/to/project.sln}}`
