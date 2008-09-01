#include <Python.h>

static PyObject *
thSpawnThread(PyObject *self, PyObject *callback, PyObject *args) {
	return Py_BuildValue("i", 0);
}

static PyObject *
thCreateThread(PyObject *self, PyObject *callback, PyObject *args) {
	return Py_BuildValue("i", 0);
}

static PyObject *
thJoinThread(PyObject *self, PyObject *arg) {
	return Py_BuildValue("i", 0);
}

static PyMethodDef thThreadMethods[] = {
	{"thSpawnThread", thSpawnThread, METH_VARARGS | METH_KEYWORDS, "Spawn a thread"},
	{"thCreateThread", thCreateThread, METH_VARARGS | METH_KEYWORDS, "Create a thread"},
	{"thJoinThread", thJoinThread, METH_VARARGS | METH_KEYWORDS, "Join a thread"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initthThread(void) {
	(void) Py_InitModule("thThread", thThreadMethods);
}
