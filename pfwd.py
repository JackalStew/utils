"""
A script to temporarliy forward TCP ports.
"""
from os import getpid
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, SHUT_RD, SHUT_WR, SHUT_RDWR
from sys import argv
from threading import Thread

max_listen = 7
recv_size = 1024


def safe_close_a(sock, shut=SHUT_RDWR):
    try:
        sock.shutdown(shut)
    except:
        pass
    try:
        sock.close()
    except:
        pass


def safe_close_b(sock, shut=SHUT_RDWR):
    try:
        sock.shutdown(shut)
    except:
        try:
            sock.close()
        except:
            pass


def start_thread(target, args):
    t = Thread(target=target, args=args)
    t.daemon = True
    t.start()
    return t


def forward(src_sock, dst_sock):
    try:
        buf = src_sock.recv(recv_size)
        while buf:
            dst_sock.sendall(buf)
            buf = src_sock.recv(recv_size)
    except:
        pass
    safe_close_b(src_sock, SHUT_RD)
    safe_close_b(dst_sock, SHUT_WR)


def listener(bind_addr, bind_port, fwd_addr, fwd_port):
    bind_sock = socket(AF_INET, SOCK_STREAM)
    bind_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    bind_sock.bind((bind_addr, bind_port))
    bind_sock.listen(max_listen)
    print("Now forwarding: %s:%d --> %s:%d" %
          (bind_addr, bind_port, fwd_addr, fwd_port))
    while True:
        try:
            in_sock, in_addr = bind_sock.accept()
            print("Accepted new connection from %s:%d --> %s:%d" %
                  (in_addr[0], in_addr[1], fwd_addr, fwd_port))
            out_sock = socket(AF_INET, SOCK_STREAM)
            out_sock.connect((fwd_addr, fwd_port))
            start_thread(forward, (in_sock, out_sock))
            start_thread(forward, (out_sock, in_sock))
        except:
            safe_close_a(in_sock)
            safe_close_a(out_sock)


def start_listener(arg_group):
    args = arg_group.split(':')    
    bind_addr = ''
    if len(args) == 4:
        bind_addr = args[0]
        args = args[1:]
    if len(args) != 3:
        print("Unable to process %s" % arg_group)
        return False
    bind_port, fwd_addr, fwd_port = int(args[0]), args[1], int(args[2])
    start_thread(listener, (bind_addr, bind_port, fwd_addr, fwd_port))
    return True


def main(args):
    print("Hit ENTER to stop")
    print("Or kill the PID %d" % getpid())

    cont_flag = False
    for arg_group in args:
        cont_flag = start_listener(arg_group) or cont_flag

    if cont_flag:
        # Python 2/3 compat mess:
        try:
            raw_input()
        except NameError:
            input()


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1:])
    else:
        print("Usage: " + argv[0] + " [bind_addr:]bind_port:connect_addr:connectport "
              "[[bind_addr:]bind_port:connect_addr:connectport]...")
