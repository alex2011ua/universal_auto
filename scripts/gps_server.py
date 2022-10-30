import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
from socket import * 
from threading import Thread
from time import sleep


UDP_IP = "fly-global-services"
UDP_PORT = 44300

def tcp_function():
    sockfd = socket(AF_INET, SOCK_STREAM)
    sockfd.bind(("0.0.0.0", UDP_PORT))
    logging.info(msg="Hello TCP THREAD on Fly.io!")
    sockfd.listen() 
    while True:
        newsockfd, address = sockfd.accept() 
        data = newsockfd.recv(1024)
        logging.info(msg=data)
        message = "TCP OK"
        logging.info(msg=message)
        newsockfd.send(message.encode())
        newsockfd.close()

def run():
    thread = Thread(target = tcp_function)
    thread.start()

    sockfd = socket(AF_INET, SOCK_DGRAM)
    sockfd.bind((UDP_IP, UDP_PORT))
    logging.info(msg="Hello UDP on Fly.io!")
    while True:
        data, client_addr = sockfd.recvfrom(1024)
        message = "UDP OK"
        logging.info(msg=data)
        logging.info(msg=message)
        sockfd.sendto(message.encode(), client_addr)