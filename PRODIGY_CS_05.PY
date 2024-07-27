# In this file I can write my last program of the internship in the company PRODIGY INFOTECH.
#But this is not my last program of my life. I will continue to write programs in my life.
import os

def checknet():
    print("Welcome to network checker")
    print("Network checker is where you may utilize Busybox functionality")
    print()

def telnet(a, b):
    pass

def check_network(a, b):
    pass

def traceroute(a, b):
    pass

def main():
    print("Which tool do you want to use?")
    print("1. Telnet")
    print("2. Checknet")
    print("3. Traceroute")
    print("4. Exit")

checknet()
main()

while True:
    choice = input("Enter your choice: ").lower()
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice")
        continue

    if choice == '4':
        break

    num1 = input("Enter target IP address: ")
    num2 = input("Enter targeted port: ")

    if choice == '1':
        print(f"IP: {num1}, Port: {num2}")
        # Add telnet functionality here
    elif choice == '2':
        print(f"IP: {num1}, TCP Port: {num2}")
        os.system(f'nc -vz {num1} {num2}')
        print(f"IP: {num1}, UDP Port: {num2}")
        os.system(f'nc -vzu {num1} {num2}')
    elif choice == '3':
        print(f"IP: {num1}, Port: {num2}")
        os.system(f'traceroute {num1} {num2}')

    repeat_checknet = input("Do you want to check another network? (Yes/No): ").strip().lower()
    if repeat_checknet != 'yes':
        break
