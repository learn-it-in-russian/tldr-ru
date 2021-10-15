# elm

> Собрать и запустить исходный код на языке программирования Elm.

- Инициализирует проект Elm, генерирует файл elm.json:

`elm init`

- Запустить интерактивную оболочку Elm:

`elm repl`

- Собрать Elm файл, вывод записывается в файл `index.html`:

`elm make {{source}}`

- Собрать Elm файл, вывести результат в JavaScript файл:

`elm make {{source}} --output={{destination}}.js`

- Запустить локальный веб-сервер, который компилирует Elm файлы при перезапуске страницы:

`elm reactor`

- Установить Elm пакет с https://package.elm-lang.org:

`elm install {{author}}/{{package}}`
