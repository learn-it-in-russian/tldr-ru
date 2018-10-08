# clang

> Компилятор для исходных файлов на C, C++ и Objective-C. Может использоваться как замена GCC.

- Компилировать файлы с исходным кодом в исполняемый файл:

`clang {{input_source.c}} -o {{output_executable}}`

- Включить печать всех ошибок и предупреждений:

`clang {{input_source.c}} -Wall -o {{output_executable}}`

- Подключить библиотеку, расположенную не в одном каталоге с файлом исходного кода:

`clang {{input_source.c}} -o {{output_executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`
