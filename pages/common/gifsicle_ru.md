# gifsicle

> Создает GIF-файлы.

- Делает GIF-анимацию с помощью gifsicle:

`gifsicle --delay={{10}} --loop *.gif > {{anim.gif}}`

- Извлекает кадры из анимации:

`gifsicle {{anim.gif}} '#0' > {{firstframe.gif}}`

- Также Вы можете редактировать анимацию посредством замены, удаления или вставки кадров:

`gifsicle -b {{anim.gif}} --replace '#0' {{new.gif}}`
