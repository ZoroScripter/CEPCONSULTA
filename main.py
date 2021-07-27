#####################
import requests    #
import os         #
import time      #
##################

os.system("clear")
os.system("pkg install figlet")
os.system("pip install requests")
os.system("clear")
print("\033[1;34m")
os.system("figlet ConsultaCEPv1")
print("""\033[1;36m
===========================
### Consulta de Cep!!   ###
===========================
""")
cep_input = input("\033[1;37mDigite o Cep para Ser Consultado\n>>>")

if len(cep_input) !=9:
    print("Quantidade de numeros INVALIDA!!")
    print("Volte ao Inicio!!")
    time.sleep(5)
    os.system("clear")
    os.system("python3 main.py")

requests = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))

address_data = requests.json()

if "erro" not in address_data:
    os.system("clear")
    print("\033[1;31m")
    print("======================================")
    print("===> CEP ENCONTRADO!! <===")
    print("CEP: {}".format(address_data["cep"]))
    print("BAIRRO: {}".format(address_data["bairro"]))
    print("CIDADE: {}".format(address_data["localidade"]))
    print("ESTADO: {}".format(address_data["uf"]))
    print("GIA: {}".format(address_data["gia"]))
    print("======================================")
    print("""
    Vc deseja fzr uma nova consulta??
    1 Sim
    2 Não
    ===================================
    """)
    op = input(">>> ")
    
    if op == "1":
        os.system("python3 main.py")
    elif op == "2":
        exit()
    else:
        os.system("python3 main.py")
else:
    print("\033[1;32m")
    os.system("figlet Zoro")
    print("""\033[1;31m
    =-=-=-=-=-=-=-=-=-=
    =  ERROR    ERROR =
    ===================
    Volte ao inicio!!
    """)
    time.sleep(4)
    os.system("python3 main.py")