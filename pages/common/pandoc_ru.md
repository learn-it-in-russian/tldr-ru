# pandoc

> Конвертирует документы из одного формата в другой.

- Сконвертировать файл в PDF (формат результирующего файла определяется по расширению файла):

`pandoc {{input.md}} -o {{output.pdf}}`

- Конвертация с явно указанным форматом файл:

`pandoc {{input.docx}} --to {{gfm}} -o {{output.md}}`

- Преобразовывает в отдельный файл с соответствующими заголовками / футерами (для LaTeX, HTML, и т.д.):

`pandoc {{input.md}} -s -o {{output.tex}}`

- Вывести список всех поддерживаемых входных форматов:

`pandoc --list-input-formats`

- Вывести список всех поддерживаемых форматов результирующих файлов:

`pandoc --list-output-formats`
