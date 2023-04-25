all:
	pip install -r requirements.txt

# pack:
# 	zip -r

clean:
	rm -rf ../src/__pycache__

test: tests.py
	python3 tests.py

doc:
	doxygen Doxyfile

run: main.py
	python3 main.py

profile: profiling.py
	python3 profiling.py
