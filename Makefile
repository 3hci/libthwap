all:
	@echo "Do nothing"
	make -C python all
	make -C ruby all
	make -C tests all

build:
	make -C python/ build
	make -C ruby/ build

install:
	make -C python/ install
	make -C ruby/ install

clean:
	make -C python/ clean
	make -C ruby/ clean
	@find ./ -type f -name ".*.sw*" | xargs rm -fv

test:
	make -C tests/ test 

syntax:
	make -C python/ syntax
	make -C ruby/ syntax
