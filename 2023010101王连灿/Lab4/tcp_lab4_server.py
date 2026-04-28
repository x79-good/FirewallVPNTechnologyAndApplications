import socket
import time
import os

HOST = '0.0.0.0'
PORT = int(os.environ.get('LAB4_PORT', 38090))

# 创建监听套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"server listening on {HOST}:{PORT}")

# 等待客户端连接
conn, addr = server_socket.accept()
print(f"connected by {addr}")

# 停顿2秒，方便观察ESTABLISHED状态
time.sleep(2)

# 接收数据
data = conn.recv(204800)
print(f"server recv {len(data)} bytes")

# 发送响应
response = b"Hello TCP Lab4! This is server response."
conn.sendall(response)
print(f"server sent response: {response.decode()}")

# 停顿后关闭
time.sleep(3)
conn.close()
print("connection closed")

# 停留10秒，方便观察TIME-WAIT
time.sleep(10)
server_socket.close()