# logwatch

> Сводит в единый отчёт разноформатные протокольные файлы нескольких сервисов (например apache, pam_unix, sshd, и т.д.).

- Просканировать логи в указанном диапазоне дат с заданным уровнем детализации:

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}'`

- Вывести в отчёте информацию лишь по заданному сервису:

`logwatch --range {{all}} --service {{apache|pam_unix|etc}}`
