# lvextend

> Увеличить размер логического тома.
> 
> Смотри также: [lvm](https://900913.ru/tldr/linux/ru/lvm/).

- Увеличивает размер тома до 120 GB:

`lvextend --size {{120G}} {{logical_volume}}`

- Увеличивает размер тома на 40 GB:

`lvextend --size +{{40G}} -r {{logical_volume}}`

- Расширить размер тома до 100% свободного места раздела физического диска:

`lvextend --size {{100}}%FREE {{logical_volume}}`
