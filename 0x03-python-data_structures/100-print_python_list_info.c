#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - Print basic info about Python lists
 * @p: PyObject
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
PyObject *items;
PyListObject *list = (PyListObject *)p;
int item, size, alloc;

size = Py_SIZE(p);
alloc = list->allocated;
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (item = 0; item < size; item++)
{
items =  PyList_GetItem(p, item);
printf("Element %d: %s\n", item, Py_TYPE(items)->tp_name);
}
}
