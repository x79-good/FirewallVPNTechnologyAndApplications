import socket
import time
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = int(os.environ.get('LAB4_PORT', 38090))

# 创建客户端socket
print("socket created")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 发起连接
print("calling connect()")
connect_start = time.time()
client_socket.connect((SERVER_HOST, SERVER_PORT))
connect_end = time.time()
print(f"connect() returned, took {connect_end - connect_start:.3f}s")

# 连接成功后再获取本地地址
local_addr = client_socket.getsockname()
print(f"local socket = {local_addr}")

# 停顿2秒，方便截图ESTABLISHED
time.sleep(2)

# 发送200000字节大数据
print("sendall() start, request bytes=200000")
request_data = b'a' * 200000
send_start = time.time()
client_socket.sendall(request_data)
print("sendall() done")

# 等待接收响应
print("calling recv() and waiting for response")
recv_start = time.time()
response = client_socket.recv(1024)
recv_end = time.time()
wait_time = recv_end - recv_start
print(f"first recv() returned after {wait_time:.3f}s")
print(f"recv data: {response.decode()}")

# 关闭
time.sleep(1)
client_socket.close()
print("client closed")