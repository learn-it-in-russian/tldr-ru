# avrdude

> Программатор для микроконтроллеров Atmel AVR.

- Прочитать AVR микроконтроллер:

`avrdude -p {{AVR_device}} -c {{programmer}} -U flash:r:{{file.hex}}:i`

- Записать AVR микроконтроллер:

`avrdude -p {{AVR_device}} -c {{programmer}} -U flash:w:{{file.hex}}`

- Список всех доступных AVR devices:

`avrdude -p \?`

- Список доступных AVR программаторов:

`avrdude -c \?`
