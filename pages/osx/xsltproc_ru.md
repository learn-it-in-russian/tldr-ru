# xsltproc

> Преобразует XML файл с помощью XSLT для вывода данных (обычно HTML или XML).

- Преобразовать XML файл с определённой таблицей стилей XSLT:

`xsltproc --output {{output.html}} {{stylesheet.xslt}} {{xmlfile.xml}}`

- Передать значение параметру в таблице стилей:

`xsltproc --output {{output.html}} --stringparam {{name}} {{value}} {{stylesheet.xslt}} {{xmlfile.xml}}`
