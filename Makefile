all: train predict

install:
	python3 -m pip install -r requirement.txt

train:
	rm -rf img && mkdir -p img
	git restore theta.csv && ./linear_regression.py

predict:
	./predict.py

.PHONY:
	all install train predict
.SILENT:
