# composer

> Пакетно-ориентированная система управления зависимостями для проектов на PHP.

- Добавляет пакет в качестве зависимости данного проекта, добавляя соответствующую запись в `composer.json`:

`composer require {{user/package-name}}`

- Устанавливает все зависимости из `composer.json` данного проекта:

`composer install`

- Деинсталлирует пакета из данного проекта, удаляя зависимость из `composer.json`:

`composer remove {{user/package-name}}`

- Обновляет все зависимости из `composer.json` данного проекта:

`composer update`

- Обновляет `composer` до новейшей версии:

`composer self-update`
