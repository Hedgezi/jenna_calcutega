all:
	pip install -r requirements.txt

pack:
	mkdir -p ../../$(ARCHIVE)/doc
	mkdir -p ../../$(ARCHIVE)/install
	mkdir -p ../../$(ARCHIVE)/repo
	cp -a ../doc/* ../../$(ARCHIVE)/doc
	cp -a ../calcutega-installer/* ../../$(ARCHIVE)/install
	cp -a ../profiler-installer/* ../../$(ARCHIVE)/install
	cp -a ../* ../../$(ARCHIVE)/repo
	rm -rf ../../$(ARCHIVE)/repo/doc
	rm -rf ../../$(ARCHIVE)/repo/installer
	cd ../.. && zip -r $(ARCHIVE).zip $(ARCHIVE)

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
