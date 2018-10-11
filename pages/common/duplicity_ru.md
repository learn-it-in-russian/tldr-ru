# duplicity

> Создает инкрементальные, сжатые, зашифрованные и версируемые резервные копии.
> Также может заливать резервные копии на различные сервисы.

- Делает зашифрованную с помощью пароля резервную копию локальной папки, сохраняя ее на удаленной машине через FTPS:

`FTP_PASSWORD={{ftp_login_password}} PASSPHRASE={{encryption_password}} duplicity {{path/to/source/directory}} {{ftps://user@hostname/target/directory/path/}}`

- Делает резерную копию папки, сохраняя на Amazon S3, делая полную резервную копию каждый месяц:

`duplicity --full-if-older-than {{1M}} --use-new-style s3://{{bucket_name[/prefix]}}`

- Удаляет версии старше 1 года из резервного хранилища на WebDAV:

`FTP_PASSWORD={{webdav_login_password}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://user@hostname[:port]/some_dir}}`

- Список доступных резервных копий:

`duplicity collection-status "file://{{absolute/path/to/backup/folder}}"`

- Список файлов в резервной копии, сохраненной на удаленной машине через SSH:

`duplicity list-current-files --time {{YYYY-MM-DD}} scp://{{user@hostname}}/path/to/backup/dir`

- Восстанавливает подкаталог из локальной резервной копии, зашифрованной с помощью GnuPG, в заданное место:

`PASSPHRASE={{gpg_key_password}} duplicity restore --encrypt-key {{gpg_key_id}} --file-to-restore {{relative/path/restorefolder}} file://{{absolute/path/to/backup/folder}} {{path/to/directory/to/restore/to}}`
