import subprocess
import time
counter = 1
response = []

# Connect to the remote host using netcat
process = subprocess.Popen(['nc', '206.189.112.129', '31082'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

while True:
    # Read the response from the remote host
    response.append(process.stdout.readline().decode('ascii').strip())
    # Process the response
    if response:
        # Send the input to the remote host
        if counter == 1:
            process.stdin.write('1\n'.encode())
            process.stdin.flush()
            counter +=1
        else:
            if len(response) == 8:
                print(response[-1])
                response = response[-1]
                response = response[7:-4]
                try:
                    output = eval(str(response))
                    output = '%.2f' % output
                    if float(output) <= -1337.00 or float(output) >= 1337.00:
                        process.stdin.write("MEM_ERR\n".encode())
                        process.stdin.flush()
                        response = []
                        counter += 1
                    else:
                        process.stdin.write((str(output) + "\n").encode())
                        process.stdin.flush()
                        response = []
                        counter += 1
                except ZeroDivisionError as DIV0_ERR:
                    process.stdin.write("DIV0_ERR\n".encode())
                    process.stdin.flush()
                    response = []
                    counter += 1
                except SyntaxError as SYNTAX_ERR:
                    process.stdin.write("SYNTAX_ERR\n".encode())
                    process.stdin.flush()
                    response = []
                    counter += 1
                except BrokenPipeError as e:
                    continue
            elif counter == 3:
                response = response[-1]
                print(response)
                if len(response) > 8:
                    response = response[9:-4]
                    try:
                        output = eval(str(response))
                        output = '%.2f' % output
                        if float(output) <= -1337.00 or float(output) >= 1337.00:
                            process.stdin.write("MEM_ERR\n".encode())
                            process.stdin.flush()
                            response = []
                            counter += 1
                        else:
                            process.stdin.write((str(output) + "\n").encode())
                            process.stdin.flush()
                            response = []
                            counter += 1
                    except ZeroDivisionError as DIV0_ERR:
                        process.stdin.write("DIV0_ERR\n".encode())
                        process.stdin.flush()
                        response = []
                        counter += 1
                    except SyntaxError as SYNTAX_ERR:
                        process.stdin.write(("SYNTAX_ERR" + "\n").encode())
                        process.stdin.flush()
                        response = []
                        counter += 1
                    except BrokenPipeError as e:
                        process.stdin.write(("SYNTAX_ERR" + "\n").encode())
                        process.stdin.flush()
                        response = []
                        counter += 1
                else:
                    process.stdin.write(("SYNTAX_ERR" + "\n").encode())
                    process.stdin.flush()
                    response = []
                    counter += 1
            elif counter > 3:
                response = response[-1]
                print(response)
                if len(response) > 8:
                    response = response[9:-4]
                    try:
                        output = eval(str(response))
                        output = '%.2f' % output
                        if float(output) < -1337.0 or float(output) > 1337.0:
                            process.stdin.write(("MEM_ERR" + "\n").encode())
                            process.stdin.flush()
                            response = []
                            counter += 1
                        else:
                            process.stdin.write((str(output) + "\n").encode())
                            process.stdin.flush()
                            response = []
                            counter += 1
                    except ZeroDivisionError as DIV0_ERR:
                        process.stdin.write("DIV0_ERR\n".encode())
                        process.stdin.flush()
                        response = []
                        counter += 1
                    except SyntaxError as SYNTAX_ERR:
                        process.stdin.write(("SYNTAX_ERR" + "\n").encode())
                        process.stdin.flush()
                        response = []
                        counter += 1
                    except BrokenPipeError as e:
                        process.stdin.write(("SYNTAX_ERR" + "\n").encode())
                        process.stdin.flush()
                        response = []
                        counter += 1
                else:
                    process.stdin.write(("SYNTAX_ERR" + "\n").encode())
                    process.stdin.flush()
                    response = []
                    counter += 1
