'''
write a python program 
Demonstrate - ATM Pin Number validation.
initialize - pin number is 1234
use while loop 
   - limit is 3 attempts
   - read a input pin number from <STDIN>
   - test - if pin number is correct -> display "Pin Number is Valid" - display count
- if all 3 attempts are failed -> display "Pin is blocked"
'''
pin = 1234
count = 0
while(count < 3):
    user_pin = int(input("Enter your pin number: "))
    count += 1
    if(user_pin == pin):
        print(f"Pin Number is Valid - count is:{count}")
        break

if pin != user_pin:
    print("Pin is blocked")