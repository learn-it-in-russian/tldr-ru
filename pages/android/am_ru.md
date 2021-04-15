# am

> Управляет активностями в Android.

- Запустить указанную активность:

`am start -n {{com.android.settings/.Settings}}`

- Запустить активность и передать данные в неё:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Запустить активность, подходящую указанной активности и категории:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Конвертировать задачу в URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
