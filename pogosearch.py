def option_1():
    return "shiny"

def option_2():
    return "!shiny"

def option_3():
    return "legendary"

def option_4():
    return "!legendary"

def option_5():
    return "costume"

def option_6():
    return "!costume"

def option_7():
    return "mythical"

def option_8():
    return "!mythical"

def option_9():
    return "ultra beasts"

def option_10():
    return "!ultra beasts"

def option_11():
    return "traded"

def option_12():
    return "!traded"

def option_13():
    return "shadow"

def option_14():
    return "!shadow"

def option_15():
    return "purified"
    
def option_16():
    return "!purified"
    
def option_17():
    return "kanto"
    
def option_18():
    return "!kanto"
    
def option_19():
    return "johto"
    
def option_20():
    return "!johto"
    
def option_21():
    return "hoenn"
    
def option_22():
    return "!hoenn"
    
def option_23():
    return "sinnoh"
    
def option_24():
    return "!sinnoh"
    
def option_25():
    return "unova"
    
def option_26():
    return "!unova"
    
def option_27():
    return "alola"
    
def option_28():
    return "!alola"
    
def option_28():
    return "galar"
    
def option_29():
    return "!galar"
    
def option_30():
    return "paldea"
    
def option_31():
    return "!paldea"
    
def option_32():
    return "0*"
    
def option_33():
    return "1*"
    
def option_34():
    return "2*"
    
def option_35():
    return "3*"
    
def option_36():
    return "4*"
    
def option_37():
    return "!0*"
    
def option_38():
    return "!1*"
    
def option_39():
    return "!2*"
    
def option_40():
    return "!3*"
    
def option_41():
    return "!4*"

options = {
    '1': option_1,
    '2': option_2,
    '3': option_3,
    '4': option_4,
    '5': option_5,
    '6': option_6,
    '7': option_7,
    '8': option_8,
    '9': option_9,
    '10': option_10,
    '11': option_11,
    '12': option_12,
    '13': option_13,
    '14': option_14,
    '15': option_15,
    '16': option_16,
    '17': option_17,
    '18': option_18,
    '19': option_19,
    '20': option_20,
    '21': option_21,
    '22': option_22,
    '23': option_23,
    '24': option_24,
    '25': option_25,
    '26': option_26,
    '27': option_27,
    '28': option_28,
    '29': option_29,
    '30': option_30,
    '31': option_31,
    '32': option_32,
    '33': option_33,
    '34': option_34,
    '35': option_35,
    '36': option_36,
    '37': option_37,
    '38': option_38,
    '39': option_39,
    '40': option_40,
    '41': option_41,
}

print("Available Options:")
for key, value in options.items():
    print(f"{key}: {value()}")

print("\nSelect options (comma-separated, e.g., 1,2,3):")
selected_options = input().split(',')

output_text = ""
for i, option in enumerate(selected_options):
    if option.strip() in options:
        output_text += options[option.strip()]()
        if i != len(selected_options) - 1:
            output_text += "|"

print("\nGenerated Text:")
print(output_text)
