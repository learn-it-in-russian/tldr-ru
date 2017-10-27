# firewall-cmd

> Терминальный клиент для службы firewalld.

- Отобразить все доступные зоны брандмауэра:

`firewall-cmd --get-active-zones`

- Отобразить все правила, которые используются в данный момент:

`firewall-cmd --list-all`

- Навсегда открыть порт для службы в указанной зоне(например, порт `443` в зоне `public`):

`firewall-cmd --permanent --zone={{public}} --add-service={{https}}`

- Навсегда закрыть порт для службы в указанной зоне (например порт `80` в зоне `public`):

`firewall-cmd --permanent --zone={{public}} --remove-service={{http}}`

- Перезапустить firewalld для применения изменений в правилах:

`firewall-cmd --reload`
