# cmark

> Конвертирует текст в формате CommonMark Markdown в другие форматы.

- Получить из файла CommonMark Markdown HTML-файл:

`cmark --to html {{filename.md}}`

- Получить со стандартного ввода данные и вывести в формате LaTeX:

`cmark --to latex`

- Конвертировать обычные кавычки в "умные" кавычки:

`cmark --smart --to html {{filename.md}}`

- Проверить файл на соответствие UTF-8:

`cmark --validate-utf8 {{filename.md}}`
