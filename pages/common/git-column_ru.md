# git column

> Вывести данные в виде колонок.

- Отформатировать стандартный поток ввода (stdin) в виде нескольких колонок:

`ls | git column --mode={{column}}`

- Отформатировать стандартный поток ввода (stdin) в виде нескольких колонок, шириной не более `100`:

`ls | git column --mode=column --width={{100}}`

- Отформатировать стандартный поток ввода (stdin) в виде нескольких колонок, с отступом в `30` символов на колонку:

`ls | git column --mode=column --padding={{30}}`