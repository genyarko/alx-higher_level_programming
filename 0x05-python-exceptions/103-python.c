#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to a PyObject
 *
 * Description: A C function that print some basic info about Python lists
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int size, i;
	PyListObject *list;
	PyObject *element;
	PyBytesObject *byte;

	setbuf(stdout, NULL);
	if (!PyList_Check(p))
	{
		printf("Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = Py_SIZE(list);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %lu\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		element = list->ob_item[i];
		printf("Element %d: %s\n", i, element->ob_type->tp_name);
		if (PyBytes_Check(element))
		{
			byte = (PyBytesObject *)element;
			printf("%d: %s\n", i, PyBytes_AsString(byte));
		}
	}
	fflush(stdout);
}

/**
 * print_python_bytes - prints basic info of a Python bytes object
 * @p: pointer to a Python bytes object
 *
 * This function prints some basic info of a Python bytes object.
 * If p is not a valid PyBytesObject, an error message is printed.
 * A maximum of 10 bytes will be printed in the line “first X bytes”.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *str;
	int i;

	setbuf(stdout, NULL);

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Error: object is not a PyBytesObject\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);

	if (size > 10)
		printf("  first 10 bytes: ");
	else
		printf("  first %zd bytes: ", size);

	for (i = 0; i < (size > 10 ? 10 : size); i++)
		printf("%02hhx%s", str[i], i + 1 == size || i + 1 == 10 ? "\n" : " ");
}

/*
 * print_python_float - prints basic info about Python float object
 * @p: PyObject pointer to a Python float object
 *
 * Description: This prints general information about a Python float object
 * such as its address in memory, its size, and its value. 
 * If p is not a valid float object, an error message is printed.
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Error: p is not a valid float object\n");
		return;
	}
	float_obj = (PyFloatObject *)p;
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	printf("  address: %p\n", float_obj);
	printf("  size: %ld\n", sizeof(PyFloatObject));
	printf("  value: %f\n", float_obj->ob_fval);
}
