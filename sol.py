from scipy import integrate
from math import cos, sin
import subprocess

equation = ''
# execute equation
def function(x):
    global equation
    return eval(equation)

# Define the command to run
command = ["nc", "20.169.252.240", "4200"]
# Spawn a new process to run the command and connect to the server
process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# read "Welcome to the Baby Calculator! Answer 40 questions in a minute to get the flag."
question = process.stdout.readline().decode()
print("Server response:", question)
# read "Server response: The difference between your input and the correct answer must be less than 1e-6."
question = process.stdout.readline().decode()
print("Server response:", question)
while(True):
    # read "[+] Question number:"
    question = process.stdout.readline().decode()
    print("Server response:", question)
    # read "ex:  Evaluate the integral of: -8*sin(x) from 1 to 10."
    equation = process.stdout.readline().decode()
    print("Server response:", equation)
    # stop condition
    if equation.find('from') == -1:
        break
    equation = equation[equation.index(':') + 1:]
    # Lower bound(from):
    lower_limit = int(equation[equation.index('from') + 5 : equation.index('to')])
    print('lower_limit:  ', lower_limit)
    # Upper bound(to):
    upper_limit = int(equation[equation.index('to') + 2 : equation.index('.')])
    print('upper_limit:  ', upper_limit)
    equation = equation[:equation.index('from')]
    print("equation:  ", equation)
    # Calculate the Integral of equation
    integral, error = integrate.quad(function, int(lower_limit), int(upper_limit), epsabs=1e-3)
    print("The value of the integral is:", round(integral, 4))
    answer = str(round(integral, 4)) + '\n'
    # send answer to server
    process.stdin.write(answer.encode())
    process.stdin.flush()
process.wait()
process.stdin.close()
process.stdout.close()
print("****************End Script****************")