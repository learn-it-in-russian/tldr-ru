# virtualenv

> Создаёт виртуальное изолированное Python окружение.

- Создаёт новое Python окружение:

`virtualenv {{path/to/venv}}`

- Изменить префикс строки приглажения для ввода команд в консоли:

`virtualenv --prompt={{prompt_prefix}} {{path/to/venv}}`

- Использовать другую версию Python для этого окружения:

`virtualenv --python={{path/to/pythonbin}} {{path/to/venv}}`

- Запустить (выбрать) нужное Python окружение:

`source {{path/to/venv}}/bin/activate`

- Прекратить использование активного окружения:

`deactivate`
