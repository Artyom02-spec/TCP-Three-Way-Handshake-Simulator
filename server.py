import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 5555))
    server_socket.listen(1)

    print("[1] Server dinleniyor... (SYN bekleniyor)")
    conn, addr = server_socket.accept()
    print(f"[2] SYN alindi. Bağlanti {addr} tarafindan başlatildi.")

    print("[3] SYN-ACK gönderiliyor...")

    print("[4] ACK bekleniyor...")
    print("[5] Üçlü el sıkışma tamamlandi. Bağlanti kuruldu!")
    
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
