# bibliotecas necessárias para a ferramenta
import argparse
import pyfiglet
import socket
import time

# descrição da ferramenta
parse = argparse.ArgumentParser(description="Descobertas de endereços IP pelo dominio")
title = pyfiglet.Figlet()

#função principal
def get_ips(): 
    #titulo/nome da ferramenta
    print(title.renderText("IP FINDER"))
    #adicionando argumentos
    parse.add_argument("-d", "--dominio", help="Domínio a ser pesquisado", type=str, required=True)
    args = parse.parse_args()

    #tentativa de buscar o endereço IP
    try:
     domain = socket.gethostbyname(args.dominio)
     print("Buscando o endereço IP...")
     time.sleep(2)
     print(f"Endereço ip encontrado: {domain}")
    except socket.gaierror as error:
     print(error)
    
get_ips()
