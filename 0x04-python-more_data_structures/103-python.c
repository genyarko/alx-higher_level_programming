#include "/usr/include/python3.4/Python.h"
#include <stdio.h>


void print_python_bytes(PyObject *p)
{
    int i;
    PyBytesObject *bytes;
    if (!PyBytes_Check(p))
    {
        printf("Invalid Bytes Object\n");
        return;
    }
    bytes = (PyBytesObject *)p;
    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python Bytes = %ld\n", PyBytes_Size(p));
    printf("[*] Trying string: %s\n", bytes->ob_sval);
    printf("[*] First %d bytes: ", (int)PyBytes_Size(p) > 10 ? 10 : (int)PyBytes_Size(p));
    for (i = 0; i < (int)PyBytes_Size(p) && i < 10; i++)
    {
        printf("%02x ", (unsigned char)bytes->ob_sval[i]);
    }
    printf("\n");
}
void print_python_list(PyObject *p)
{
    int i;
    PyListObject *list;
    if (!PyList_Check(p))
    {
        printf("Invalid List Object\n");
        return;
    }
    list = (PyListObject *)p;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", list->allocated);
    for (i = 0; i < PyList_Size(p); i++)
    {
        printf("Element %d: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}
