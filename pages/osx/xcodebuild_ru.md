# xcodebuild

> Сборка проектов Xcode.

- Собрать рабочее пространство:

`xcodebuild -workspace {{workspace_name.workspace}} -scheme {{scheme_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- Собрать проект:

`xcodebuild -target {{target_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- Показать все SDK:

`xcodebuild -showsdks`
