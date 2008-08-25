all:
	@echo "Do more nothing"

build:
	@python setup.py build

install:
	@python setup.py install

clean:
	@find ./ -type f -name *.pyc | xargs rm -vf
	@find ./ -type f -name *.pyo | xargs rm -vf
	@rm -rf build
