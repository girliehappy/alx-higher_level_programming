#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - A program that prints bytes information
 * @p: The python Object
 * Return: return nothing
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, h, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (h = 0; h < limit; h++)
		if (string[h] >= 0)
			printf(" %02x", string[h]);
		else
			printf(" %02x", 256 + string[h]);

	printf("\n");
}

/**
 * print_python_list - A program that prints list information
 * @p: The Python Object
 * Return: doesn't return anything
 */
void print_python_list(PyObject *p)
{
	long int size, h;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (h = 0; h < size; h++)
	{
		obj = ((PyListObject *)p)->ob_item[h];
		printf("Element %ld: %s\n", h, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
