SHELL = /usr/bin/bash
COUNT=10000

test:
	@for i in {1..100}; do bash -c "ab -c $$i -n $(COUNT) http://127.0.0.1:9000/ 2>/dev/null | grep 'Requests per second' | tr -s ' ' | cut -d' ' -f4"; done

python3-aiohttp:
	python3 aiohttp_hello.py

python3-asyncio:
	python3 asyncio_hello.py

python2-trollius:
	python2 asyncio_hello.py

python3-asyncore:
	python3 asyncore_hello.py

python2-asyncore:
	python2 asyncore_hello.py

pypy-trollius:
	pypy asyncio_hello.py

pypy-asyncore:
	pypy asyncore_hello.py

pypy3-asyncore:
	pypy3 asyncore_hello.py

python-uvloop:
	python uvloop_hello.py

go:
	go run http.go

node:
	node http-hello.js

erlang:
	echo "c(hello). hello:start()." | erl

