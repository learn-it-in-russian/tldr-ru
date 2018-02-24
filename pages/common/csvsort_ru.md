# csvsort

> Сортирует CSV-файлы.
> Входит в csvkit.

- Сортирует CSV-файл по 9-ой колонке:

`csvsort -c {{9}} {{data.csv}}`

- Сортирует CSV-файл по колонке с именем "name" по убыванию:

`csvsort -r -c {{name}} {{data.csv}}`

- Сортирует CSV-файл по колонке 2, затем по колонке 4:

`csvsort -c {{2,4}} {{data.csv}}`

- Сортирует CSV-файл без предположений о типах данных:

`csvsort --no-inference -c {{columns}} {{data.csv}}`
