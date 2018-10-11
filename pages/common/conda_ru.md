# conda

> Система управления пакетами, зависимостями и окружением для любых языков программирования.

- Создает новое окружение, устанавливая в него определенные пакеты:

`conda create --name {{environment_name}} {{python=2.7 matplotlib}}`

- Список всех окружений:

`conda info --envs`

- Загружает или выгружает окружение:

`source {{activate|deactivate}} {{environment_name}}`

- Удаляет окружение (удаляет все пакеты):

`conda remove --name {{environment_name}} --all`

- Ищет каналы conda для пакета с заданным именем:

`conda search {{package_name}}`

- Устанавливает пакеты в текущее окружение:

`conda install {{python=3.4 numpy}}`

- Выводит пакетов, установленных в текущее окружение:

`conda list`

- Удаляет неиспользуемые пакеты и кэш:

`conda clean --all`
