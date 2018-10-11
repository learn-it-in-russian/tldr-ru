# electrum

> Удобный кошелек Bitcoin и управление личным ключом.

- Создает новый кошелек:

`electrum -w {{new_wallet.dat}} create`

- Восстанавливает существующий кошелек из seed оффлайн:

`electrum -w {{recovery_wallet.dat}} restore -o`

- Создает подписанную транзакцию оффлайн:

`electrum mktx {{recipient}} {{amount}} -f 0.0000001 -F {{from}} -o`

- Показывает все входящие адреса для кошелька:

`electrum listaddresses -a`

- Подписывает сообщение:

`electrum signmessage {{address}} {{message}}`

- Проверяет сообщение:

`electrum verifymessage {{address}} {{signature}} {{message}}`

- Подключается к заданному серверу electrum:

`electrum -p socks5:{{127.0.0.1}}:9050 -s {{56ckl5obj37gypcu.onion}}:50001:t -1`
