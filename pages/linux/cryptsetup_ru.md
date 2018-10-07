# cryptsetup

> Управление зашифрованными томами: чистый dm-crypt или LUKS (Linux Unified Key Setup).

- Инициализация тома LUKS (переписывает все данные на разделе!):

`cryptsetup luksFormat {{/dev/sda1}}`

- Открыть том LUKS и создать дешифрованный указатель в /dev/mapper/{{target}}:

`cryptsetup luksOpen {{/dev/sda1}} {{target}}`

- Удалить существующий указатель:

`cryptsetup luksClose {{target}}`
