# rpmbuild

> Утилита для сборки RPM-пакетов.

- Собрать бинарный пакет и пакет с исходниками:

`rpmbuild -ba {{path/to/spec_file}}`

- Сборка бинарного пакета без исходников:

`rpmbuild -bb {{path/to/spec_file}}`

- Указать дополнительные переменные для сборки пакта:

`rpmbuild -bb {{path/to/spec_file}} --define "{{variable1}} {{value1}}" --define "{{variable2}} {{value2}}"`
