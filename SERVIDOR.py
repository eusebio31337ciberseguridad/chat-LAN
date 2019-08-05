"""SERVIDOR"""
el_host = ""
el_puerto = 1337
import socket
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((el_host, el_puerto))
servidor.listen(1)
conn, addr = servidor.accept()
conn.recv(1024)
