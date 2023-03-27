/*
 * print_python_list - print basic info about Python lists
 * @p: Pointer to PyObject object
 *
 * Description: This function prints basic info about Python lists,
 * including the type, size, and first and last items of the list.
 *
 * Return: Void
 */
void print_python_list(PyObject *p)
{
	int i;
	PyListObject *list;
	PyObject *first;
	PyObject *last;

	setbuf(stdout, NULL);
	if (!PyList_Check(p))
	{
		printf("Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", list->ob_size);
	printf("[*] Allocated = %lu\n", list->allocated);
	if (list->ob_size > 0)
	{
		first = list->ob_item[0];
		printf("[*] First item of the List at address %p: %s\n", list->ob_item[0],
		       first->ob_type->tp_name);
		last = list->ob_item[list->ob_size - 1];
		printf("[*] Last item of the List at address %p: %s\n", list->ob_item[list->ob_size - 1],
		       last->ob_type->tp_name);
	}
}

/*
 * print_python_bytes - print basic info about Python bytes
 * @p: Pointer to PyObject object
 *
 * Description: This function prints basic info about Python bytes,
 * including the type, size, and first 10 bytes of the bytes object.
 *
 * Return: Void
 */
void print_python_bytes(PyObject *p)
{
	int i;
	PyBytesObject *bytes;
	char *str;

	setbuf(stdout, NULL);
	if (!PyBytes_Check(p))
	{
		printf("Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	str = bytes->ob_sval;
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", bytes->ob_base.ob_base.ob_size);
	printf("  trying string: %s\n", str);
	printf("  first %d bytes:", (int)bytes->ob_base.ob_base.ob_size);
	for (i = 0; i < (int)bytes->ob_base.ob_base.ob_size && i < 10; i++)
		printf(" %02x", str[i] & 0xff);
	printf("\n");
}

/*
 * print_python_float - print basic info about Python floats
 * @p: Pointer to PyObject object
 *
 * Description: This function prints basic info about Python floats,
 * including the type and value of the float object.
 *
 * Return: Void
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float;
	double val;

	setbuf(stdout, NULL);
	if (!PyFloat_Check(p))
	{
		printf("Invalid Float Object\n");
		return;
	}
	float = (PyFloatObject *)p;
	val = float->ob_fval;
	printf("[.] float object info\n");
	printf("  value: %.16g\n", val);
}
