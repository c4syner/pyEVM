"""
Designed by Cliff Syner
ENS: AlpineDev.eth
Twitter: @alpineeth
Discord: AlpineDev.eth#3596
"""
import colorama
import web3
from web3.method import Munger
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
            m_index = 0
            m_list = []
            j = 0

            for x in contract_abi:
                if(x["stateMutability"] == "pure" or x["stateMutability"] == "view"):
                    j += 1
                    m_list.append(m_index)
                    print("{i}. {R}{a}{E}(".format(i=j,R=Fore.RED,a=x["name"], E=Style.RESET_ALL), end="")
                    for d, i in enumerate(x["inputs"]):
                        if(d == len(x["inputs"])-1):
                            print("{G}{a} {B}{b}{E})".format(G=Fore.GREEN,a=i["type"],b=i["name"], B=Fore.BLUE, E=Style.RESET_ALL), end="")
                        else:
                            print("{G}{a} {B}{b}{E},".format(G=Fore.GREEN,a=i["type"],b=i["name"], B=Fore.BLUE, E=Style.RESET_ALL), end="")
                    print()
                m_index += 1

            if(j == 0):
                s = "No read functions."
            indice = int(input(": "))-1
            clear_screen()
            ds = contract_abi[m_list[indice]]
            print("{R}{a}{E}".format(R=Fore.RED,a=ds["name"], E=Style.RESET_ALL), end="\n")
            t_inputs = []
            for d, i in enumerate(ds["inputs"]):
                ti = input("{G}{a} {B}{b}{E}: ".format(G=Fore.GREEN,a=i["type"],b=i["name"], B=Fore.BLUE, E=Style.RESET_ALL))
                if(i["type"] == "string"):
                    t_inputs.append(ti)
                elif(i["type"] == "bytes"):
                    t_inputs.append(w3.toBytes(text=ti))
                elif(i["type"][:4] == "uint" and "[" not in i["type"]):
                    t_inputs.append(w3.toInt(text=ti))
                elif("[" in i["type"]):
                    #handle list
                    if(i["type"][:6] == "string"):
                        func = str
                    elif(i["type"][:5] == "bytes"):
                        func = w3.toBytes
                    elif(i["type"][:4] == "uint"):
                        func = w3.toInt

                    tl = json.loads(ti)
                    t_inputs.append([func(text=m) for m in tl])
                else:
                    s = ("Custom structs are not yet supported!")
                    break 
            #WORK BEGINS BACK HERE: PUT THIS IN THE CONTRACT
            break
        if(action == 2):
            #Write Logic
            pass

        if(s):
            print('{r}{m}{a}'.format(r=Fore.RED,m=s, a=Style.RESET_ALL))
        clear_screen()
    

if(__name__ == "__main__"):
    main()