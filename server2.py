
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 2222))
server.listen(10)
close_msg = u'close'

def hh_read_from_socket(sock, max_len):

    cur_msg = ''

    while len(cur_msg) < max_len:
        data = sock.recv(max_len - len(cur_msg))

        if not data:
            # raise RuntimeError(u'empty data')
            break

        cur_msg = cur_msg + data

    return cur_msg

def hh_write_to_socket (sock, msg):

    totalsent = 0

    while totalsent < len(msg):

        sent = sock.send(msg[totalsent:])

        if sent == 0:
            # raise RuntimeError("broken")
            break

        totalsent = totalsent + sent


while True:
    conn, addr = server.accept()

    message = hh_read_from_socket(conn, 1024)

    hh_write_to_socket(server, message)

    if message == close_msg:
        conn.close()