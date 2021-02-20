# ufraw-batch

> Конвертирует сырые файлы с камеры в стандартные файлы изображений.

- Простая конвертация RAW файлов в jpg:

`ufraw-batch --out-type=jpg {{input_file(s)}}`

- Простая конвертация RAW файлов в png:

`ufraw-batch --out-type=png {{input_file(s)}}`

- Создаёт изображения для предпросмотра файлов из исходных файлов камеры:

`ufraw-batch --embedded-image {{input_file(s)}}`

- Сохраняет файл с размерами уменьшенными, до указанных максимумов MAX1 и MAX2:

`ufraw-batch --size=MAX1,MAX2 {{input_file(s)}}`
