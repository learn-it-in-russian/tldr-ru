# certbot

> Let's Encrypt агент для автоматического получения и обновления TLS сертификатов.
> Преемник старой утилиты `letsencrypt`.

- Получить новый сертификат через webroot авторизацию, но не устанавливать его автоматически:

`sudo certbot certonly --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}}`

- Получить новый сертификат через nginx авторизацию, установить новый сертификат автоматически:

`sudo certbot --nginx --domain {{subdomain.example.com}}`

- Получить новый сертификат через apache авторизацию, установить новый сертификат автоматически:

`sudo certbot --apache --domain {{subdomain.example.com}}`

- Обновить все Let's Encrypt сертификаты, которые истекают через 30 дней или меньше (не забудьте перезапустить сервисы, которые могут использовать их):

`sudo certbot renew`

- Симулировать получение нового сертификата, но не сохранять новые сетрификаты на диск (работа в режиме "dry-run" - для проверки работоспособности):

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --dry-run`

- Получить недоверенный тестовый сертификат:

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --test-cert`
