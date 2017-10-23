# mkfs.exfat

> Создает файловую систему exFAT на разделе.

- Создать файловую систему exFAT на разделе `1` устройства `b` (`sdb1`):

`mkfs.exfat {{/dev/sdb1}}`

- Создать файловую систему exFAT и задать метку тома:

`mkfs.exfat -n {{volume_name}} {{/dev/sdb1}}`

- Создать файловую систему exFAT и задать идентификатор раздела:

`mkfs.exfat -i {{volume_id}} {{/dev/sdb1}}`
