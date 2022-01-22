# ceph

> Единая система хранения.

- Проверить работоспособность кластера:

`ceph status`

- Показать статус использования кластера:

`ceph df`

- Получить статистику использования групп хранения кластера:

`ceph pg dump --format {{plain}}`

- Создать пул хранения:

`ceph osd pool create {{pool_name}} {{page_number}}`

- Удалить пул хранилища:

`ceph osd pool delete {{pool_name}}`

- Переименовать пул хранилища:

`ceph osd pool rename {{current_name}} {{new_name}}`

- Починить пул хранилища:

`ceph pg repair {{pool_name}}`
