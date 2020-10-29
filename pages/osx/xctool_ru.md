# xctool

> Инструмент для создания проектов Xcode.

- Собрать проект без указания рабочего пространства:

`xctool -project {{YourProject.xcodeproj}} -scheme {{YourScheme}} build`

- Собрать проект, который является частью существующего рабочего пространства:

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} build`

- Очистить рабочий каталог, собрать проект и выполнить все тесты:

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} clean build test`
