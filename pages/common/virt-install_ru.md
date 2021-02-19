# virt-install

> Создать виртуальную машину через *libvirt* и начать установку операционной системы.

- Создаёт виртуальную машину с 1 GiB RAM-памяти и 12 GiB постоянного хранилища, а также начать установку Debian из iso файла:

`virt-install --memory {{1024}} --disk path={{path/to/image.qcow2}},size={{12}} --cdrom {{path/to/debian.iso}}`
