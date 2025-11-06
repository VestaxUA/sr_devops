import socket

HOST = "127.0.0.1"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP StatsD-сервер запущено на {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"[StatsD] Отримано повідомлення від {addr}: {data.decode()}")