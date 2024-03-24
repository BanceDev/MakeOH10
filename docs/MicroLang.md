# Scripting the MicroLab with MicroLang

MicroLang is an original programming language made for the MicroLab that helps to make it easier to write arduino code with little effort.
Using a set of intuitive keywords and a natural english control structure MircoLang can be picked up my a complete programming novice in no time.

## MicroLang Commands

### Creating a Program
In MicroLang the program must be enclosed in a program block that allows the wrapper to create an arduino file with the name specified.

```
PROGRAM HelloWorld
END
```

### Conditionals and Conditions

MicroLang is capable of simple if, else if, and else structures following the formatting shown in the following example code block.

```
IF BUTTON1
    GREEN_ON
    YELLOW_OFF
    RED_OFF
    BLUE_OFF
ELSE IF BUTTON2
    GREEN_OFF
    YELLOW_OFF
    RED_ON
    BLUE_OFF
ELSE
    GREEN_OFF
    YELLOW_ON
    RED_OFF
    BLUE_ON
END
```

As you can see in the code above we can also use the BUTTON1, BUTTON2, and BUTTON3 keywords as contitions. This model of the MicroLab only supports those three
conditions but more can easily become supported in the language.

### Loops

MicroLang has an easy to understand structure for loops, the language only includes iteration in set integer intervals to keep things simple but still making it possible to reduce code redundancy.

```
DO 10 TIMES
    GREEN_ON
    DELAY 500
    GREEN_OFF
    DELAY 500
END
```

### Printing on LCD

MicroLang prevents students from having to deal with the libraries and object oriented code needed in arduino to work with an LCD and simplifies it into a single 
command. Just write what you would like to show on the screen after the PRINT command.

```
PRINT Hello Make OH10!
```

### Creating Delays

Often times a functionality that will be wanted is delaying an action. In MicroLang the DELAY command can be used to pause the program for a number of milliseconds.
The example below would delay for one second.
```
DELAY 1000
```

### Command Keywords

In order to interact with the digital devices like the 4 LEDs and the Buzzer MicroLang has very intuitive commands for this. For LEDs just type the color with the 
state you want it in. EX: GREEN_ON and for the buzzer do likewise BUZZER_OFF

```
// All commands
GREEN_ON
GREEN_OFF
RED_ON
RED_OFF
YELLOW_ON
YELLOW_OFF
BLUE_ON
BLUE_OFF
BUZZER_ON
BUZZER_OFF
```