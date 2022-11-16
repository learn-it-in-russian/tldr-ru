# ceph

> Единая система хранения данных.

- Проверка статуса работоспособности кластера:

`ceph status`

- Получение статистики использования кластера:

`ceph df`

- Получение статистики для групп размещения в кластере:

`ceph pg dump --format {{plain}}`

- Создание пула хранилища:

`ceph osd pool create {{pool_name}} {{page_number}}`

- Удалить пул хранилища:

`ceph osd pool delete {{pool_name}}`

- Переименование пула хранилища:

`ceph osd pool rename {{current_name}} {{new_name}}`

- Запуск починки пула хранилища:

`ceph pg repair {{pool_name}}`
