# say

> Преобразование текста в голос.

- Озвучить введённый текст:

`say {{"I like to ride my bike."}}`

- Озвучить текстовый файл:

`say -f {{filename.txt}}`

- Озвучить введённый текст с выбранным голосом и скоростью речи:

`say -v {{voice}} -r {{words_per_minute}} {{"I'm sorry Dave, I can't let you do that."}}`

- Вывести список доступных голосов:

`say -v ?`

- Создать аудиофайл с озвученным введённым текстом:

`say -o {{filename.aiff}} {{"Here's to the Crazy Ones."}}`
