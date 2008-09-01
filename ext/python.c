#include <Python.h>

static PyObject *
thSpawnThread(PyObject *self, PyObject *callback, PyObject *args) {
	return Py_BuildValue("i", 0);
}

static PyMethodDef thThreadMethods[] = {
	{"thSpawnThread", thSpawnThread, METH_VARARGS | METH_KEYWORDS, "Spawn a thread"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initthThread(void) {
	(void) Py_InitModule("thThread", thThreadMethods);
}
