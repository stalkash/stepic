import socket

def myreceive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        buf = sock.recv(msglen - len(msg))
        if buf == '':
            raise RuntimeError('broken')
        msg += buf
    return msg

def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError('broken')
        totalsent += s

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    conn, addr = s.accept()
    while True:
        data = myreceive(conn, 1024)
        if data == b'close':
            conn.close()
            break
        mysend(conn, data)
    conn.close()
