CC=gcc
CFLAGS=-std=c99 -g -O3 -Wall -Wstrict-prototypes -fPIC -I/usr/lib/ruby/1.8/i686-linux -I/usr/include -I/usr/include/python2.5
LDFLAGS=-L/usr/lib -L/usr/lib/python2.5 -L/usr/lib/ -lpython2.5 -lruby

all:
	@echo "Do more nothing">/dev/null

build:
	$(CC) $(CFLAGS) -c thThread.c -o thThread.o
	$(CC) $(CFLAGS) -c python.c -o python.o
	$(CC) $(CFLAGS) -c ruby.c -o ruby.o
	$(CC) $(LDFLAGS) -shared thThread.o python.o ruby.o -o thThread.so

install:
	@echo "Nothing to do."

clean:
	rm -f a.out *.o *.so 
