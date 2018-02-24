# consul-kv

> Распределенное key-value хранилище с проверкой здоровья и обнаружение сервисов.

- Читает значение из key-value хранилища:

`consul kv get {{key}}`

- Сохраняет новую пару key-value:

`consul kv put {{key}} {{value}}`

- Удаляет пару key-value:

`consul kv delete {{key}}`
