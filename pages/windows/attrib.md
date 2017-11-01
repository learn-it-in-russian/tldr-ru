# attrib

> Displays, sets, or removes attributes assigned to files or directories. If use it without parameters, attrib displays attributes of all files in the current directory.
> List of attributes:
> r - read-only; a - archive; s - system; h - hidden.

- Display the attributes of a `[[filename]]` located on the current drive:

`attrib {{filename}}`

- Assign the read-only attribute to `{{filename}}`:

`attrib +r {{filename}}`

- Remove the archive attribute from files in the `{{foldername}}` and from files in any subdirectories of `{{foldername}}`:

`attrib -a {{foldername}}\*.* /s`
