def create_file(file_name):
    try:
        with open("sketches/" + file_name + ".ino", 'w') as file:
            file.write("//" + file_name + "\n")
            file.write("#define RED 4\n#define YELLOW 5\n#define GREEN 2\n#define BLUE 3\n#define BUZZER 6\n#define BUTTON1 7\n#define BUTTON2 8\n#define BUTTON3 9\n")
            file.write("#include <LiquidCrystal_I2C.h>\nLiquidCrystal_I2C lcd(0x27, 16, 2);\n")
            file.write("void setup() {\npinMode(RED, OUTPUT);\npinMode(YELLOW, OUTPUT);\npinMode(GREEN, OUTPUT);\npinMode(BLUE, OUTPUT);\npinMode(BUZZER, OUTPUT);\npinMode(BUTTON1, INPUT_PULLUP);\npinMode(BUTTON2, INPUT_PULLUP);\npinMode(BUTTON3, INPUT_PULLUP);\n")
            file.write("digitalWrite(BUZZER, HIGH);\nlcd.init();\nlcd.backlight();\nlcd.setCursor(0, 0);\n}\n")
            file.write("void loop() {" + "\n")
    except IOError:
        print("Error writing to file", file_name)

def if_statement(file_name, condition):
    if condition == "BUTTON1":
        condition = "digitalRead(BUTTON1)"
    elif condition == "BUTTON2":
        condition = "digitalRead(BUTTON2)"
    else:
        condition = "digitalRead(BUTTON3)"

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
    if condition == "BUTTON1":
        condition = "digitalRead(BUTTON1)"
    elif condition == "BUTTON2":
        condition = "digitalRead(BUTTON2)"
    else:
        condition = "digitalRead(BUTTON3)"

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

def digital_write(file_name, pin, state):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("digitalWrite(" + pin + ", " + state + ");\n")
    except IOError:
        print("Error writing to file", file_name)

def buzzer(file_name, freq):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("tone(BUZZER, " + freq + ");\n")
    except IOError:
        print("Error writing to file", file_name)

def no_tone(file_name):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("digitalWrite(BUZZER, HIGH);\n")
    except IOError:
        print("Error writing to file", file_name)

def print_statement(file_name, text):
    try:
        with open("sketches/" + file_name + ".ino", 'a') as file:
            file.write("lcd.clear();\nlcd.setCursor(0,0)\nlcd.print(\""+text+"\");\n")
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
                    line = line.replace("ELSE", "")
                    line = line.replace("IF", "")
                    line = line.strip()
                    elif_statement(out_name, line)
                elif "IF" in line:
                    line = line.replace("IF", "")
                    line = line.strip()
                    if_statement(out_name, line)
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
                elif "GREEN_ON" in line:
                    digital_write(out_name, "GREEN", "HIGH")
                elif "GREEN_OFF" in line: 
                    digital_write(out_name, "GREEN", "LOW")
                elif "RED_ON" in line:
                    digital_write(out_name, "RED", "HIGH")
                elif "RED_OFF" in line: 
                    digital_write(out_name, "RED", "LOW")
                elif "BLUE_ON" in line:
                    digital_write(out_name, "BLUE", "HIGH")
                elif "BLUE_OFF" in line: 
                    digital_write(out_name, "BLUE", "LOW")
                elif "YELLOW_ON" in line:
                    digital_write(out_name, "YELLOW", "HIGH")
                elif "YELLOW_OFF" in line: 
                    digital_write(out_name, "YELLOW", "LOW")
                elif "BUZZER_OFF" in line:
                    no_tone(out_name)
                elif "BUZZER" in line:
                    line = line.replace("BUZZER", "")
                    line = line.strip()
                    buzzer(out_name, line)
                elif "PRINT" in line:
                    line = line.replace("PRINT", "")
                    line = line.lstrip()
                    print_statement(out_name, line)
                
    except FileNotFoundError:
        print("File not found. Please make sure the file name is correct.")


def main():
    file_name = input("Enter the name of the input file: ")
    read_file(file_name)


if __name__ == "__main__":
    main()
