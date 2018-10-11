# in2csv

> Преобразует данные из различных табличных форматов в CSV.
> Входит в состав csvkit.

- Преобразовать XLS файл в CSV:

`in2csv {{data.xls}}`

- Преобразовать DBF файл в CSV файл:

`in2csv {{data.dbf}} > {{data.csv}}`

- Преобразовать определенный лист из XLSX файла в CSV:

`in2csv --sheet={{sheet_name}} {{data.xlsx}}`

- Преобразовать JSON файл с помощью in2csv:

`cat {{data.json}} | in2csv -f json > {{data.csv}}`
