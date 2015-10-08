SHELL = /usr/bin/bash

test:
	@for i in {1..100}; do bash -c "ab -c $$i -n 1000 http://127.0.0.1:9000/ 2>/dev/null | grep 'Requests per second' | tr -s ' ' | cut -d' ' -f4"; done

python3-aiohttp:
	python3 aiohttp_hello.py

python3-asyncio:
	python3 asyncio_hello.py

python2-trollius:
	python2 asyncio_hello.py

pypy:
	pypy asyncio_hello.py

pypy3:
	pypy3 asyncio_hello.py

nuitka:
	nuitka --recurse-all asyncio_hello.py
	./asyncio_hello.exe

cython2:
	cythonize -bi asyncio_hello.py
	python2 -c "import asyncio_hello"

cython3:
	cythonize -3 -bi asyncio_hello.py
	python3 -c "import asyncio_hello"

go:
	go run http.go

node:
	node http-hello.js

