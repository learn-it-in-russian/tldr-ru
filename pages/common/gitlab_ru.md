# gitlab

> Консольная обёртка, написанная на Ruby для GitLab API.

- Создать новый проект:

`gitlab create_project {{project_name}}`

- Получить информацию об указанном коммите:

`gitlab commit {{project_name}} {{commit_hash}}`

- Получить информацию о job-ах в указанном пайплайне CI (Continuous Integration - подсистема GitLab для непрерывной интеграции):

`gitlab pipeline_jobs {{project_name}} {{pipeline_id}}`

- Запустить указанный CI job:

`gitlab job_play {{project_name}} {{job_id}}`
