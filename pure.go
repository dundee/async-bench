package main

import (
    "log"
    "net"
    "strings"
)

func httpServer(c net.Conn) {
    for {
        buf := make([]byte, 512)
        nr, err := c.Read(buf)
        if err != nil {
            return
        }

        data := buf[0:nr]
	if strings.Contains(string(data), "\r\n\r\n") { 
        	_, err := c.Write([]byte("HTTP/1.1 200 OK\n\nHello world!"))
	        if err != nil {
	            log.Fatal("Write: ", err)
	        }
		c.Close()
		return
	}
    }
}

func main() {
    l, err := net.Listen("tcp", "localhost:9000")
    if err != nil {
        log.Fatal("listen error:", err)
    }

    for {
        fd, err := l.Accept()
        if err != nil {
            log.Fatal("accept error:", err)
        }

        go httpServer(fd)
    }
}
