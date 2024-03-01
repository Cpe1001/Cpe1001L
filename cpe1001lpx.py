import sys
import string
from sense_hat import SenseHat

sense = SenseHat()

word_definitions = {
    "MOVE": "Move to a specified location",
    "ADD": "Addition operation",
    "SUBTRACT": "Subtraction operation",
    "DIVIDE": "Division operation",
    "MULTIPLY": "Multiplication operation",
    "R0": "Register 0",
    "R1": "Register 1",
    "R2": "Register 2",
    "R3": "Register 3",
    "R4": "Register 4",
    "D0": "Data Memory 0",
    "D1": "Data Memory 1",
    "D2": "Data Memory 2",
    "D3": "Data Memory 3",
    "D4": "Data Memory 4",
    "D5": "Data Memory 5",
    "D6": "Data Memory 6",
    "D7": "Data Memory 7",
    "D8": "Data Memory 8",
    "D9": "Data Memory 9",
}

registers = {
    "R0": 0,
    "R1": 0,
    "R2": 0,
    "R3": 0,
    "R4": 0,
}

data_memory = {
    "D0": 0,
    "D1": 0,
    "D2": 0,
    "D3": 0,
    "D4": 0,
    "D5": 0,
    "D6": 0,
    "D7": 0,
    "D8": 0,
    "D9": 0,
}

def registers_table(registers):
    registers_table = (
        "+-----------+\n"
        "| REGISTERS |\n"
        "+-----------+\n"
    )

    for register, value in registers.items():
        registers_table += f"| {register}: {value:<8} |\n"

    registers_table += "+-----------+"
    return registers_table

def data_memory_table(data_memory):
    data_memory_table = (
        "+-------------+\n"
        "| DATA MEMORY |\n"
        "+-------------+\n"
    )

    for slot, value in data_memory.items():
        data_memory_table += f"| {slot}: {value:<8} |\n"

    data_memory_table += "+-------------+"
    return data_memory_table

def move_command(destination, value):
    if destination in registers and value.isdigit():
        registers[destination] = int(value)

def store_command(register,destination):
    if register in registers and destination in data_memory:
        data_memory[destination] = registers[register]
        
def load_command(destination, value):
    if destination in registers and value in registers:
        registers[destination] = registers[value]

def display_green():
    sense.clear(0, 255, 0)
    
def display_red():
    sense.clear(255, 0, 0)

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        print("Command:", line)

        words = line.split()
        cleaned_words = []
        for word in words:
            if word.isdigit():
                cleaned_words.append(word)
            else:
                cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
                cleaned_words.append(cleaned_word)

        for i, cleaned_word in enumerate(cleaned_words):
            if cleaned_word in word_definitions:
                print(cleaned_word, "-", word_definitions[cleaned_word])
            else:
                if cleaned_word.isdigit():
                    print(cleaned_word, "-", cleaned_word)
                else:
                    print(cleaned_word)

        if len(cleaned_words) >= 3 and cleaned_words[0] == "MOVE":
            destination = cleaned_words[1]
            value = cleaned_words[2]
            move_command(destination, value)
        if len(cleaned_words) >= 3 and cleaned_words[0] == "STORE":
            register = cleaned_words[1]
            destination = cleaned_words[2]
            store_command(register, destination)
        if len(cleaned_words) >= 3 and cleaned_words[0] == "LOAD":
            destination = cleaned_words[1]
            value = cleaned_words[2]
            load_command(destination, value)
        
        print("\nRegister")
        print(registers_table(registers))
        
        print("\nData Memory")
        print(data_memory_table(data_memory))
        
        display_green()
    
except Exception as e:
display_red()