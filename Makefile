
.PHONY: test

test:
	PYTHONPATH=$(PWD) python -m unittest discover -s test

clean:
	find ./ -name "*~" -delete
	find ./ -name "*.pyc" -delete
	rm -rf dist build env
