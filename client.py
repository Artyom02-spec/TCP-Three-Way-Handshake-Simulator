import socket
import time

def start_client():
    time.sleep(1)
    print("[1] SYN gönderiliyor...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))

    print("[2] SYN-ACK alindi.")
    print("[3] ACK gönderildi.")
    print("[4] Üçlü el sıkışma tamamlandi. Server ile bağlanti kuruldu.")

    client_socket.close()

if __name__ == "__main__":
    start_client()
