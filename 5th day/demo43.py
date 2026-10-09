

try:
    n = input('Enter n Value:')
    if int(n) >100:
        raise ValueError("n value is above 100")
except Exception as e:
    print(e)
    
    
class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1500
try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insuffiient account balance")
except Exception as e:
    print(e)