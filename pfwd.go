package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

func forwarder(readConn net.Conn, writeConn net.Conn) {
	defer readConn.Close()
	defer writeConn.Close()

	var err error
	var n int

	buf := make([]byte, 0xffff)

	for true {
		n, err = readConn.Read(buf)
		if err != nil {
			return
		}
		n, err = writeConn.Write(buf[:n])
		if err != nil {
			return
		}
	}
}

func listener(bindStr string, connStr string) {
	var ln net.Listener
	var inConn, outConn net.Conn
	var err error

	ln, err = net.Listen("tcp", bindStr)
	if err != nil {
		fmt.Println("Unable to bind on", bindStr)
		return
	}
	fmt.Println("Listeneing:", bindStr, "-->", connStr)

	for true {
		inConn, err = ln.Accept()
		if err != nil {
			fmt.Println("Error accepting connection on", bindStr)
		} else {
			fmt.Println("New connection:", inConn.RemoteAddr().String(), "-->", connStr)
			outConn, err = net.Dial("tcp", connStr)
			if err != nil {
				fmt.Println("Error connecting to", connStr)
				inConn.Close()
			} else {
				go forwarder(inConn, outConn)
				go forwarder(outConn, inConn)
			}
		}
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage:", os.Args[0], "[bind_addr:]bind_port:connect_addr:connectport [[bind_addr:]bind_port:connect_addr:connectport]...")
		return
	}

	fmt.Println("Enter to stop")
	fmt.Println("Or kill this PID:", os.Getpid())

	listenFlag := false

	for _, arg := range os.Args[1:] {
		argsplit := strings.Split(arg, ":")
		switch len(argsplit) {
		case 3:
			go listener(":"+argsplit[0], argsplit[1]+":"+argsplit[2])
			listenFlag = true
		case 4:
			go listener(argsplit[0]+":"+argsplit[1], argsplit[2]+":"+argsplit[3])
			listenFlag = true
		default:
			fmt.Println("Unable to process", arg)
		}
	}

	if listenFlag == true {
		input := bufio.NewScanner(os.Stdin)
		input.Scan()
	}

	return
}
