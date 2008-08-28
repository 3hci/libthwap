all:
	@echo "" >/dev/null

build:
	make -C ext/ build
	make -C d/ build
	make -C python/ build
	make -C ruby/ build

install:
	make -C d/ install
	make -C ext/ install
	make -C python/ install
	make -C ruby/ install

clean:
	make -C d/ clean
	make -C ext/ clean
	make -C python/ clean
	make -C ruby/ clean
	@find ./ -type f -name ".*.sw*" | xargs rm -fv

test:
	make -C tests/ test 

syntax:
	make -C python/ syntax
	make -C ruby/ syntax
