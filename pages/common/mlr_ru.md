# mlr

> Miller – утилита, подобная `awk`, `sed`, `cut`, `join` и `sort` для форматов данных, таких как CSV, TSV 
> и отформатированного tab-ами JSON.

- Вывести в удобочитаемом формате CSV файл, отформатированный tab-ами:

`mlr --icsv --opprint cat {{example.csv}}`

- Получить данные JSON в удобном виде и вывести на терминал (stdout):

`echo '{"hello":"world"}' | mlr --ijson --opprint cat`

- Отсортировать строки / объекты по имени для указанного поля:

`mlr --icsv --opprint sort -f {{field}} {{example.csv}}`

- Отсортировать в обратном числовом порядке строки / объекты для указанного поля:

`mlr --icsv --opprint sort -nr {{field}} {{example.csv}}`

- Сконвертировать CSV в JSON, предварительно произведя вычисления, и вывести их результат:

`mlr --icsv --ojson put '${{newField1}} = ${{oldFieldA}}/${{oldFieldB}}' {{example.csv}}`

- Из входного JSON вывести вертикально-форматированный JSON:

`echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat`

- Получить заархивированный CSV файл, отфильтровать строки по регулярному выражению и вывести:

`mlr --prepipe 'gunzip' --csv filter -S '${{fieldName}} =~ "{{regular_expression}}"' {{example.csv.gz}}`
