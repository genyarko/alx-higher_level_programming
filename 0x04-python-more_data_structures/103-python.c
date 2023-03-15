#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    if (!p || !PyBytes_Check(p))
    {
        printf("Error: Invalid PyObject passed to print_python_bytes\n");
        return;
    }
    int size = (int)PyBytes_Size(p);
    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python bytes = %d\n", size);
    printf("[*] Trying string: %s\n", PyBytes_AsString(p));
    if (size > 10)
    {
        printf("[*] First 10 bytes: ");
        int i;
        for (i = 0; i < 10; i++)
            printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
        printf("\n");
    }
    else
        printf("[*] First %d bytes: %s\n", size, PyBytes_AsString(p));
}


void print_python_list(PyObject *p)
{
    if (!p || !PyList_Check(p))
    {
        printf("Error: Invalid PyObject passed to print_python_list\n");
        return;
    }
    int size = (int)PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject*)p)->allocated);
    int i;
    for (i = 0; i < size; i++)
    {
        printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}
