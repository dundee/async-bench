package main

import (
	"fmt"
	"log"
	"net/http"
)

type Hello struct{}

func (h Hello) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello world!")
}

func main() {
	var h Hello
	fmt.Println("Listening on port 9000")
	err := http.ListenAndServe("localhost:9000", h)
	if err != nil {
		log.Fatal(err)
	}
}

