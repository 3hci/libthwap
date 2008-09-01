#include <Python.h>

static PyObject *
thSpawnThread(PyObject *self, PyObject *args) {
	printf("we have spawned a thread from python!\n");
	return Py_BuildValue("i", 0);
}

static PyMethodDef thThreadMethods[] = {
	{"thSpawnThread", thSpawnThread, METH_VARARGS, "Spawn a thread"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initthThread(void) {
	(void) Py_InitModule("thThread", thThreadMethods);
}
