import socket

#socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#masuk ke server
HOST = '127.0.0.1'
PORT = 5000
client_socket.connect((HOST, PORT))
print(f"Terhubung ke server di {HOST}:{PORT}")

#ngirim ke server
pesan = input("Masukkan pesan untuk server: ")
client_socket.sendall(pesan.encode())

#nerima balasan dari server
data = client_socket.recv(1024).decode()
print(f"Balasan dari server: {data}")

#nutup koneksi
client_socket.close()
