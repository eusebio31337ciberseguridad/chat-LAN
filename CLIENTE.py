"""CLIENTE"""
el_host = "192.168.0.0"
el_puerto = 1337
import socket
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.connect((el_host, el_puerto))
servidor.send("TEXTO EJEMPLO")
