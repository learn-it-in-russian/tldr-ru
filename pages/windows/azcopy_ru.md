# azcopy

> Утилита для передачи файлов в Azure Cloud Storage Accounts.

- Войти в Azure Tenant:

`azopy login`

- Загрузить локальный файл:

`azcopy copy '{{path/to/source/file}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}/{{blob_name}}'`

- Загрузить файлы с расширениями `.txt` и `.jpg`:

`azcopy copy '{{path/to/source}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --include-pattern '{{*.txt;*.jpg}}'`

- Копировать контейнер напрямую между двумя Azure Storage Account:

`azcopy copy 'https://{{source_storage_account_name}}.blob.core.windows.net/{{container_name}}' 'https://{{destination_storage_account_name}}.blob.core.windows.net/{{container_name}}'`

- Синхронизировать локальную директорию с удалённой, удаляя файлы, которые отсутствуют в исходной (локальной):

`azcopy sync '{{path/to/source}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --recursive --delete-destination=true`

- Отобразить детализированную информацию о данной утилите:

`azcopy --help`
