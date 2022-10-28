# snmpwalk

> Утилита для для отправки SNMP запросов.

- Запросить системную информацию с сетевого узла, используя протокол SNMPv1:

`snmpwalk -v1 -c {{community}} {{ip}}`

- Запросить системную информацию с сетевого узла по OID, используя SNMPv2, на указанном порту:

`snmpwalk -v2c -c {{community}} {{ip}}:{{port}} {{oid}}`

- Запрос по OID через SNMPv3 с аутентификацией без шифрования:

`snmpwalk -v3 -l {{authNoPriv}} -u {{username}} -a {{MD5|SHA}} -A {{passphrase}} {{ip}} {{oid}}`

- Аналогичный вызов по OID протоколом SNMPv3, логин/пароль, но с шифрованием:

`snmpwalk -v3 -l {{authPriv}} -u {{username}} -a {{MD5|SHA}} -A {{auth_passphrase}} -x {{DES|AES}} -X {{enc_passphrase}} {{ip}} {{oid}}`

- SNMPv3 на OID без логина и шифрования:

`snmpwalk -v3 -l {{noAuthNoPriv}} -u {{username}} {{ip}} {{oid}}`
