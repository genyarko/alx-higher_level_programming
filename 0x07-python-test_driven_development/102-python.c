#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
void print_python_string(PyObject *p)
{
if (!PyUnicode_Check(p))
{
printf("Error: PyObject is not a valid string\n");
return;
}
Py_ssize_t length = PyUnicode_GET_LENGTH(p);
Py_UCS4* data = PyUnicode_AsUCS4(p);
printf("'");
for (Py_ssize_t i = 0; i < length; i++) {
Py_UCS4 ch = data[i];
if (ch == '\'') {
printf("\\'");
}
else if (ch == '\n')
{
printf("\\n");
}
else if (ch == '\t') {
printf("\\t");
}
else if (ch == '\r')
{
printf("\\r");
}
else if (ch < 32 || ch >= 127) {
printf("\\x%02x", (int) ch);
}
else
{
printf("%lc", ch);
}
}
printf("'\n");
PyMem_Free(data);
}
