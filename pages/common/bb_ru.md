# bb

> Нативный интерпретатор Clojure для написания сценариев (скриптов).

- Выполнить ([e]valuate) выражение:

`bb -e "(+ 1 2 3)"`

- Выполнить файл сценария ([f]ile):

`bb -f {{path/to/script.clj}}`

- Привязать ввод последовательности строк из стандартного потока ввода (stdin):

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- Передать данные в расширенной нотации данных — EDN(Extensible Data Notation) на стандартный поток ввода (stdin):

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`
