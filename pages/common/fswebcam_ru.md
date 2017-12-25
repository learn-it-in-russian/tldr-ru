# fswebcam

> Маленькая простая веб-камера для *nix.

- Сделать фотографию:

`fswebcam {{filename}}`

- Сделать фотографию с заданным разрешением:

`fswebcam -r {{width}}x{{height}} {{filename}}`

- Сделать фотографию с помощью заданного устройства (по-умолчанию, /dev/video0):

`fswebcam -d {{device}} {{filename}}`

- Сделать фотографию с меткой времени (timestamp - формат для strftime):

`fswebcam --timestamp {{timestamp}} {{filename}}`
