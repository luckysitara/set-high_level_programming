#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic info about a Python bytes object.
 * @p: The PyObject pointer to a bytes object.
 *
 * Prints the size, string content, and up to the first 10 bytes
 * (in hexadecimal) of a Python bytes object. If p does not point to
 * a valid PyBytesObject, prints an error message instead.
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!p || !PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyBytesObject *)p)->ob_base.ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		size = 10;
	else
		size += 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		printf("%s", (i == size - 1) ? "\n" : " ");
	}
}

/**
 * print_python_list - Prints basic info about a Python list object.
 * @p: The PyObject pointer to a list object.
 *
 * Prints the size and allocated capacity of a Python list, and for
 * each element, prints its index and its type name. If the element
 * is itself a bytes object, print_python_bytes is also called on it.
 */
void print_python_list(PyObject *p)
{
	long int size, alloc, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *obj;

	printf("[*] Python list info\n");

	if (!p || !PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = list->ob_base.ob_size;
	alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		obj = list->ob_item[i];
		printf("Element %ld: %s\n", i, obj->ob_type->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
