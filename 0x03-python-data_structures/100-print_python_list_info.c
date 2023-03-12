void print_python_list_info(PyObject *p) 
{ 
    if (!PyList_Check(p)) 
    { 
        PyErr_Format(PyExc_TypeError, 
                     "Expected a Python list"); 
        return; 
    } 
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p)); 
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated); 
    printf("[*] Elements: \n"); 
    for (int i = 0; i < PyList_Size(p); i++) 
    { 
        PyObject *item = PyList_GetItem(p, i); 
        printf("    Item %d: %s\n", i, Py_TYPE(item)->tp_name); 
    } 
}
