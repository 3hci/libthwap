all:
	@echo "Do nothing"

build:
	make -C python/ build
	make -C ruby/ build

install:
	make -C python/ install
	make -C ruby/ install
