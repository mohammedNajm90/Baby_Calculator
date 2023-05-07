from scipy import integrate
from math import cos, sin
import subprocess
s = ''
def function(x):
    global s
    return eval(s)

# Define the command to run
command = ["nc", "20.169.252.240", "4200"]
# Spawn a new process to run the command and connect to the server
process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# read "Welcome to the Baby Calculator! Answer 40 questions in a minute to get the flag."
s = process.stdout.readline().decode()
print("Server response:", s)
# read "Server response: The difference between your input and the correct answer must be less than 1e-6."
s = process.stdout.readline().decode()
print("Server response:", s)
while(True):
    # read "[+] Question 1:"
    s = process.stdout.readline().decode()
    print("Server response:", s)
    # read "ex:  Evaluate the integral of: -8*sin(x) from 1 to 10."
    s = process.stdout.readline().decode()
    print("Server response:", s)
    # stop condition
    if s.find('from') == -1:
        break
    s = s[s.index(':') + 1:]
    # Lower bound(from):
    lower_limit = int(s[s.index('from') + 5:s.index('to')])
    print('lower_limit:  ', lower_limit)
    # Upper bound(to):
    upper_limit = int(s[s.index('to') + 2: s.index('.')])
    print('upper_limit:  ', upper_limit)
    s = s[:s.index('from')]
    print("equation:  ", s)
    # Calculate the Integral of equation
    integral, error = integrate.quad(function, int(lower_limit), int(upper_limit), epsabs=1e-3)
    print("The value of the integral is:", round(integral, 4))
    message = str(round(integral, 4)) + '\n'
    # send answer to server
    process.stdin.write(message.encode())
    process.stdin.flush()
process.wait()
process.stdin.close()
process.stdout.close()
print("****************End Script****************")





