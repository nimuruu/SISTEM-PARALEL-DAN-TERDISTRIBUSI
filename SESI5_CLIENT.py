import socket
import threading

# Menerima pesan dari server
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Koneksi ke server terputus.")
            client.close()
            break

# Mengirim pesan ke server
def send_messages(client):
    while True:
        message = input("")
        try:
            client.send(message.encode())
        except:
            print("Gagal mengirim pesan.")
            client.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(("127.0.0.1", 5555))
    except:
        print("Tidak dapat terhubung ke server.")
        return

    print("Terhubung ke chat room! Ketik pesanmu dan tekan ENTER untuk mengirim.")

    # Jalankan dua thread untuk kirim dan terima pesan
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))

    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    start_client()
