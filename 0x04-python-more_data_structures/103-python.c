#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	if (!p || !PyBytes_Check(p))
	{
		fprintf(stderr, "Error: Invalid Bytes Object\n");
		return;
	}
	
	int size = PyBytes_Size(p);
	fprintf(stdout, "[.] Bytes object info\n");
	fprintf(stdout, "  size: %d\n", size);
	fprintf(stdout, "  trying string: %s\n", PyBytes_AsString(p));
	
	if (size > 10)
	{
		fprintf(stdout, "  first 10 bytes: ");
		for (int i = 0; i < 10; i++)
			fprintf(stdout, "%02x ", (unsigned char)PyBytes_AsString(p)[i]);
		fprintf(stdout, "\n");
	}
	else
	{
		fprintf(stdout, "  first %d bytes: ", size);
		for (int i = 0; i < size; i++)
			fprintf(stdout, "%02x ", (unsigned char)PyBytes_AsString(p)[i]);
		fprintf(stdout, "\n");
	}
}

void print_python_list(PyObject *p)
{
	if (!p || !PyList_Check(p))
	{
		fprintf(stderr, "Error: Invalid List Object\n");
		return;
	}
	
	int size = PyList_Size(p);
	fprintf(stdout, "[*] Size of the Python List = %d\n", size);
	
	fprintf(stdout, "[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	
	for (int i = 0; i < size; i++)
	{
		fprintf(stdout, "[*] Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
