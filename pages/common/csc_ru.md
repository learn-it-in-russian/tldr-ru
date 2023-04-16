# csc

> Компилятор для Microsoft C#.

- Собрать один или более C# файлов в запускаемый CIL файл:

`csc {{path/to/input_file_a.cs}} {{path/to/input_file_b.cs}}`

- Установить имя результирующего файла:

`csc /out:{{path/to/filename}} {{path/to/input_file.cs}}`

- Скомпилировать `.dll` файл: `.dll`-библиотеку вместо запускаемого:

`csc /target:library {{path/to/input_file.cs}}`

- Прикрепить ссылку к другой сборке:

`csc /reference:{{path/to/library.dll}} {{path/to/input_file.cs}}`

- Встроить ресурс (файл данных):

`csc /resource:{{path/to/resource_file}} {{path/to/input_file.cs}}`

- Автоматически сгенерировать XML документацию:

`csc /doc:{{path/to/output.xml}} {{path/to/input_file.cs}}`

- Указать иконку приложения:

`csc /win32icon:{{path/to/icon.ico}} {{path/to/input_file.cs}}`

- Указать строго указанный результирующий файл сборки (keyfile):

`csc /keyfile:{{path/to/keyfile}} {{path/to/input_file.cs}}`
