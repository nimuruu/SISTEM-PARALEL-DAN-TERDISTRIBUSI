import socket
import threading

# Menyimpan semua client yang terhubung
clients = []

# Fungsi untuk broadcast pesan ke semua client
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Jika error, hapus client dari list
                clients.remove(client)

# Fungsi untuk menangani setiap client
def handle_client(client_socket, address):
    print(f"[TERHUBUNG] {address} terhubung ke server.")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"[PESAN dari {address}] {message.decode()}")
            broadcast(message, client_socket)
        except:
            break

    # Jika koneksi terputus
    print(f"[TERPUTUS] {address} keluar dari server.")
    clients.remove(client_socket)
    client_socket.close()

# Fungsi utama server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))  # alamat dan port server
    server.listen()
    print("[MENUNGGU KONEKSI] Server berjalan di 127.0.0.1:5555")

    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()
