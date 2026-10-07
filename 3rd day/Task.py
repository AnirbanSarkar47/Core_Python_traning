import sys
import time 

Log_file = "pin_history.log"
max_attempts = 3
correct_pin = "1234"

def log_to_file(message):
    current_time = time.ctime()
    log_entry = f"{message}<=== {current_time}\n"
    with open(Log_file, "a") as file:
        file.write(log_entry)


def modify_atm_pin():
    global correct_pin
    attempts = 0
    while attempts < max_attempts:
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            correct_pin = new_pin
            log_to_file("PIN changed successfully")
            print("PIN changed successfully")
            return
        else:
            attempts += 1
            log_to_file(f"Failed attempt {attempts} to change PIN")
            print(f"PINs do not match. Attempt {attempts} of {max_attempts}")
    print("Maximum attempts reached. PIN not changed.")

if __name__ == "__main__":
    modify_atm_pin()