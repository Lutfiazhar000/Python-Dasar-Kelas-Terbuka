# type hint pada function

# penggunaan type hint
def funsi_dengan_hint(argument:int) -> int: # ini type hint
    output = 10**argument
    return output

HASIL = funsi_dengan_hint(12)
print(HASIL)

def display(argument):
    print(argument)

display("upi")