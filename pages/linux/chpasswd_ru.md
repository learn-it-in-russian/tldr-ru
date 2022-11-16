# chpasswd

> Изменяет пароли для множества пользователей, используя стандартный поток ввода (stdin).

- Изменить пароль для указанного пользователя:

`printf "{{username}}:{{new_password}}" | sudo chpasswd`

- Изменить пароль для нескольких пользователей. Ввод не должен содержать пробельных символов:

`printf "{{username_1}}:{{new_password_1}}\n{{username_2}}:{{new_password_2}}" | sudo chpasswd`

- Изменить пароль для указанного пользователя и зашифровать пароли:

`printf "{{username}}:{{new_encrypted_password}}" | sudo chpasswd --encrypted`

- Изменить пароль, указав алгоритм шифрования:

`printf "{{username}}:{{new_password}}" | sudo chpasswd --crypt-method {{NONE|DES|MD5|SHA256|SHA512}}`
