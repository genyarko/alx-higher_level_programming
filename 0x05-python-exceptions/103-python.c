#include <Python.h>
/**
 * print_python_list - Function to print info about Python list objects
 * @p: PyObject pointer
 *
 * Description: This function takes a PyObject pointer and prints information
 * about the Python list object.
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	/* Check if p is a valid PyListObject */
	if (!PyList_Check(p))
	{
		printf("Error: Object is not a Python list\n");
		return;
	}

	/* Print info about list */
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	/* Flush stdout */
	fflush(stdout);
}

/**
 * print_python_bytes - Function to print info about Python bytes objects
 * @p: PyObject pointer
 *
 * Description: This function takes a PyObject pointer and prints information
 * about the Python bytes object.
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	/* Check if p is a valid PyBytesObject */
	if (!PyBytes_Check(p))
	{
		printf("Error: Object is not a Python bytes\n");
		return;
	}

	/* Print info about bytes */
	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python Bytes = %ld\n", PyBytes_Size(p));
	printf("[*] First 10 bytes: %10.10s\n", PyBytes_AsString(p));

	/* Flush stdout */
	fflush(stdout);
}

/**
 * print_python_float - Function to print info about Python float objects
 * @p: PyObject pointer
 *
 * Description: This function takes a PyObject pointer and prints information
 * about the Python float object.
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	/* Check if p is a valid PyFloatObject */
	if (!PyFloat_Check(p))
	{
		printf("Error: Object is not a Python float\n");
		return;
	}

	/* Print info about float */
	printf("[*] Python float info\n");
	printf("[*] Value: %f\n", PyFloat_AsDouble(p));

	/* Flush stdout */
	fflush(stdout);
}
