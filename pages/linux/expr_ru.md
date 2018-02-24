# expr

> Утилита для работы с выражениями и строками.

- Получить длину строки:

`expr length {{string}}`

- Обработать логическое или математическое выражение с операторами ('+', '-', '*', '&', '|', и т.д.). Специальные символы должный быть экранированы:

`expr {{first_argument}} {{operator}} {{second_argument}}`

- Получить позицию первого вхождения подстроки в строку:

`echo $(expr index {{string}} {{substring}})`

- Извлечь часть строки:

`echo $(expr substr {{string}} {{position_to_start}} {{number_of_characters}}`

- Извлечь часть строки, которая соответствует регулярному выражению:

`echo $(expr {{string}} : '\({{regular_expression}}\)')`
