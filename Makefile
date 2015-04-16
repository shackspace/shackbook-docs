all: build/readme.html build/shack.png

build:
	mkdir -p build

build/readme.html: build build.py readme.md template.html
	python build.py

build/shack.png: build
	cp shack.png build

clean:
	rm -rf readme.html