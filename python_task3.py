import re

from pythonping import ping


def validate_ip(ip_add):
    pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
    return re.match(pattern,ip_add)

def write_valid_ip(ip_add):
    with open('vaild_ip.txt', 'a') as vaild_ip:
        vaild_ip.write(ip_add + '\n')

def write_invalid_ip(ip_add):
    with open('invaild_ip.txt', 'a') as invaild_ip:
        invaild_ip.write(ip_add + '\n')



def read_valid_ip():
    with open('vaild_ip.txt', 'r') as read_ip:
        ip = read_ip.read().splitlines()
        return ip
    
def read_invalid_ip():
    with open('invaild_ip.txt', 'r') as read_ip:
        ip = read_ip.read().splitlines()
        return ip

def ip_func():
    while True:
        while True:
            user_ip = input("Enter IP (Yes or No) : ").lower()
            if user_ip == 'no' or user_ip == 'yes':
                print(f"You Enter : {user_ip}")
                break
            else:
                print('Please Enter Only Yes or No')

        if user_ip == 'no':

            while True:
                ip_file = input("Read Valid or invalid file : ").lower()
                if ip_file == 'valid' or ip_file == 'invalid':
                    print(f"You Enter : {ip_file}")
                    break
                else:
                    print('Please Enter Only Valid or Invalid')
            
            if ip_file == 'invalid':
                read_file = read_invalid_ip()
                print("Invalid ip addresses : ")
                for i in read_file:
                    print(i, end='\n')
            else:
                read_file = read_valid_ip()
                print("valid ip addresses : ")
                for i in read_file:
                    print(i, end='\n')
                
            break
        elif user_ip == 'yes':
            Ip_address = input("Enter IP Address : ")
            if validate_ip(Ip_address):
                try:
                    result = ping(Ip_address, verbose=False)
                    list_result = list(result)
                    print("Ping results:")
                    if "Request timed out" in str(list_result[0]):
                        print("Request timed out")
                        write_invalid_ip(Ip_address)
                    else:
                        print(result)
                        write_valid_ip(Ip_address)
                except Exception as e:
                    print("An error occurred:", e)
                
            else:
                print('Enter a Vaild IP Address')
                


# list1 = ['86.222.110.189','24.12.86.216','37.6.121.237','24.37.195.158','181.216.58.239','194.193.242.252','48.203.155.209','100.230.2.246','122.7.93.150','201.140.182.111']
# for i in list1:
#    print(validate_ip(i))
#    write_ip(i)

ip_func()