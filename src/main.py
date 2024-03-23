def create_file(file_name):
    try:
        with open("sketches/" + file_name + ".ino", 'w') as file:
            file.write("//" + file_name + "\n")
            file.write("void setup() {}" + "\n")
            file.write("void loop() {" + "\n")
    except IOError:
        print("Error writing to file", file_name)

def if_statement(file_name, condition):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("if (" + condition + ") {\n")
    except IOError:
        print("Error writing to file", file_name)

def else_statement(file_name):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("} else {\n")
    except IOError:
        print("Error writing to file", file_name)

def elif_statement(file_name, condition):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("} else if (" + condition + ") {\n")
    except IOError:
        print("Error writing to file", file_name)

def end_statement(file_name):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("}\n")
    except IOError:
        print("Error writing to file", file_name)

def delay_statement(file_name, amount):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("delay(" + amount + ");\n")
    except IOError:
        print("Error writing to file", file_name)

def for_loop(file_name, amount):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("for (int i = 0; i < "+ amount + "; i++) {\n")
    except IOError:
        print("Error writing to file", file_name)

# reads in the file and handles the keywords
def read_file(file_name):
    out_name = ""
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.rstrip('\n')

                # handle the keyword
                if "PROGRAM" in line:
                    line = line.replace("PROGRAM ", "")
                    out_name = line
                    create_file(line)
                elif "ELSE IF" in line:
                    elif_statement(out_name, "idk")
                elif "IF" in line:
                    if_statement(out_name, "idk")
                elif "ELSE" in line:
                    else_statement(out_name)
                elif "END" in line:
                    end_statement(out_name)
                elif "DELAY" in line:
                    line = line.replace("DELAY", "")
                    line = line.strip()
                    delay_statement(out_name, line)
                elif "DO" in line and "TIMES" in line:
                    line = line.replace("DO", "")
                    line = line.replace("TIMES", "")
                    line = line.strip()
                    for_loop(out_name, line)
    except FileNotFoundError:
        print("File not found. Please make sure the file name is correct.")


def main():
    file_name = input("Enter the name of the input file: ")
    read_file(file_name)


if __name__ == "__main__":
    main()
