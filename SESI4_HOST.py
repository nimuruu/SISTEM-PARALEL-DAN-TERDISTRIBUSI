import socket

#socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#IP localhost sama port
HOST = '127.0.0.1'
PORT = 5000

#bind IP sama port ke server
server_socket.bind((HOST, PORT))

#maksimum 1 client
server_socket.listen(1)
print(f"Server berjalan di {HOST}:{PORT}")
print("Menunggu koneksi dari client...")

#nerima koneksi dari client
conn, addr = server_socket.accept()
print(f"Terhubung dengan client: {addr}")

#nerima pesan dari client
data = conn.recv(1024).decode()
print(f"Pesan dari client: {data}")

#kirim balasan ke client
balasan = "Pesan telah diterima oleh server."
conn.sendall(balasan.encode())

#buat tutup koneksi
conn.close()
server_socket.close()
