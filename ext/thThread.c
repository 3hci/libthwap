#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <pthread.h>
#include <unistd.h>

#define MAX_THREAD 1000

typedef struct {
	int id;
} parm;

void default_callback(void *arg) {
	parm *p=(parm *)arg;
	printf("Hello from the default callback %d\n", p->id);
	sleep(p->id);
	printf("Goodbye from the default callback %d\n", p->id);
	return;
}

void spawn_thread(void *callback, void *arg) {
	pthread_t *threads;
	pthread_attr_t *attr;
	pthread_attr_init(attr);
	threads = (pthread_t *)malloc(sizeof(*threads));

	pthread_create(threads, attr, (void *)callback, (void *)arg);
	pthread_join((int)threads, (void *)NULL);
	return;
}


int test_threads(void) {
	int i;
	int n=5;
	pthread_t *threads;
	pthread_attr_t pthread_custom_attr;
	parm *p;
	
	threads=(pthread_t *)malloc(n*sizeof(*threads));
	pthread_attr_init(&pthread_custom_attr);

	p=(parm *)malloc(sizeof(parm)*n);

	for (i=0; i<n; i++) {
		p[i].id=i;
		pthread_create(&threads[i], &pthread_custom_attr, (void *)default_callback, (void *)(p+i));
	}

	for (i=0; i<n; i++) {
		pthread_join(threads[i],NULL);
	}
	// free(p);
	return 0;
}
