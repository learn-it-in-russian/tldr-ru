# assoc

> Displays or modifies file name extension associations. If use it without parameters, assoc displays a list of all extension associations.

- View association for entered extension (for example `.txt`):

`assoc .txt`

- Remove the file type association for the file name extension `.bak`:

`assoc .bak= `

- View the output of assoc one screen at a time:

`assoc | more`

- Send the output of assoc to the file `assoc.txt`:

`assoc>assoc.txt`
