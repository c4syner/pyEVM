"""
Designed by Cliff Syner
ENS: AlpineDev.eth
Twitter: @alpineeth
Discord: AlpineDev.eth#3596
"""
import colorama
import web3
import base_profiles.eth_profile as eth
import base_profiles.poly_mumbai_profile as polyTest
import base_profiles.poly_profile as poly
import copy
import json
from web3 import Web3
from colorama import Fore, Back, Style
import colorama

def select_profile(key: int):
    if(key == 1):
        return eth.Profile
    if(key == 2):
        return poly.Profile
    if(key == 3):
        return polyTest.Profile

def clear_screen():
    print("\n"*100, end="")
    
def main():
    #Get user info
    colorama.init()
    print("pyEVM\n\nSelect Network: ")
    this_profile = select_profile(int(input("1. Ethereum Mainnet\n2. Polygon Mainnet\n3. Polygon Mumbai Testnet\n: ")))
    p_key = input("Private Key (Press Enter if only reading contracts)\n: ")
    contract_address = input("Contract Address\n: ")
    print('Loading ABI from "abi.json"')
    contract_abi = json.load(open("abi.json", "r"))

    #Initialize 
    w3 = Web3(Web3.HTTPProvider(this_profile.RPC_URL))
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    clear_screen()
    
    #Begin contract loop
    while(True):
        action = 0
        if(not len(p_key)):
            #read
            action = 1
        else:
            state = input("1. Read Contract\n2. Write Contract\n: ")
            if(state == 1):
                #read
                action = 1
            else:
                #write  
                action = 2
        s = ""
        if(action == 1):
            #Read Logic
            j = 0
            for x in contract_abi:
                if(x["stateMutability"] == "pure" or x["stateMutability"] == "view"):
                    j += 1
                    print("{i}. {R}{a}{E}(".format(i=j,R=Fore.RED,a=x["name"], E=Style.RESET_ALL), end="")
                    for d, i in enumerate(x["inputs"]):
                        if(d == len(x["inputs"])-1):
                            print("{G}{a} {B}{b}{E})".format(G=Fore.GREEN,a=i["type"],b=i["name"], B=Fore.BLUE, E=Style.RESET_ALL), end="")
                        else:
                            print("{G}{a} {B}{b}{E},".format(G=Fore.GREEN,a=i["type"],b=i["name"], B=Fore.BLUE, E=Style.RESET_ALL), end="")
                    print()
            if(j == 0):
                s = "No read functions."
            indice = int(input(": "))-1
            ds = contract_abi[j]
            for item in 
            break
        if(action == 2):
            #Write Logic
            #pass
        if(s):
            print('{r}{m}{a}'.format(r=Fore.RED,m=s, a=Style.RESET_ALL))
        clear_screen()
    

if(__name__ == "__main__"):
    main()