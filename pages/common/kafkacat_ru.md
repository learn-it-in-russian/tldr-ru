# kafkacat

> Инструменты Apache Kafka для отправки и получения сообщений.

- Получить сообщения, начиная с новейшего отступа (оффсета):

`kafkacat -C -t {{topic}} -b {{brokers}}`

- Получить сообщения, начиная со старейшего отступа и выйти после последнего полученного сообщения:

`kafkacat -C -t {{topic}} -b {{brokers}} -o beginning -e`

- Получить сообщения от имени группы получателей Kafka:

`kafkacat -G {{group_id}} {{topic}} -b {{brokers}}`

- Опубликовать сообщение, полученное со стандартного потока ввода (stdin):

` echo {{message}} | kafkacat -P -t {{topic}} -b {{brokers}}`

- Опубликовать сообщения, полученные из файла:

`kafkacat -P -t {{topic}} -b {{brokers}} {{path/to/file}}`

- Вывести мета-данные для всех топиков и брокеров:

`kafkacat -L -b {{brokers}}`

- Вывести мета-данные для указанного топика:

`kafkacat -L -t {{topic}} -b {{brokers}}`

- Получить отступ для топика/партиции для указанной точки во времени:

`kafkacat -Q -t {{topic}}:{{partition}}:{{unix_timestamp}} -b {{brokers}}`
