# notify-send

> Выводит уведомление с использованием системы уведомлений текущей среды рабочего стола(DE).

- Вывести уведомление с заголовком "Test" и содержанием "This is a test":

`notify-send {{"Test"}} {{"This is a test"}}`

- Вывести уведомление с заданным значком:

`notify-send -i {{icon.png}} {{"Test"}} {{"This is a test"}}`

- Демонстрировать уведомление 5 секунд:

`notify-send -t 5000 {{"Test"}} {{"This is a test"}}`
