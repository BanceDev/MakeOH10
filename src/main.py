def create_file(file_name):
    try:
        with open("sketches/" + file_name + ".ino", 'w') as file:
            pass # this will clear the file if it already exists
            file.write("//" + file_name + "\n")
            file.write("void setup() {}" + "\n")
            file.write("void loop() {" + "\n")
    except IOError:
        print("Error writing to file", file_name)

def if_statement(file_name, condition):
    try:
        with open("sketches/" + file_name + ".ino", 'w') as file:
            file.write("if (" + condition + ") {\n")
            file.write("void setup() {}" + "\n")
            file.write("void loop() {" + "\n")
    except IOError:
        print("Error writing to file", file_name)

# reads in the file and handles the keywords
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print("Contents of the file:")
            for line in lines:
                line = line.rstrip('\n')

                # handle the keyword
                if "PROGRAM" in line:
                    line = line.replace("PROGRAM ", "")
                    create_file(line)

                print(line)
    except FileNotFoundError:
        print("File not found. Please make sure the file name is correct.")


def main():
    file_name = input("Enter the name of the input file: ")
    read_file(file_name)


if __name__ == "__main__":
    main()
