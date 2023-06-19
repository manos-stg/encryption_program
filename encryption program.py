import pyperclip

def encrypt(text):
    text = text.lower()
    text_list = []
    for x in range(len(text)):
        text_list.append(text[x])
        dict = {
            " ": "000000",
            "e": "000001",
            "t": "000010",
            "a": "000011",
            "o": "000100",
            "i": "000101",
            "n": "000110",
            "s": "000111",
            "h": "001000",
            "r": "001001",
            "d": "001010",
            "l": "001011",
            "u": "001100",
            "c": "001101",
            "m": "001110",
            "w": "001111",
            "f": "010000",
            "g": "010001",
            "y": "010010",
            "p": "010011",
            "b": "010100",
            "v": "010101",
            "k": "010110",
            "j": "010111",
            "x": "011000",
            "q": "011001",
            "z": "011010",
            ".": "011011",
            ",": "011100",
            "?": "011101",
            "0": "011110",
            "1": "011111",
            "2": "100000",
            "3": "100001",
            "4": "100010",
            "5": "100011",
            "6": "100100",
            "7": "100101",
            "8": "100110",
            "9": "100111",
            "!": "101000",
            "'": "101001",
            "’": "101001"
        }
    # add a limitation about what will happen if a character is not in the dict
    result_list = [dict.get(char, char) for char in text]
    result = "".join(result_list)
    return result


def translate(text):
    text_list = []
    for i in range(0, len(text), 6):
        piece = text[i:i + 6]
        text_list.append(piece)

    dictionary = {
        "000000": " ",
        "000001": "e",
        "000010": "t",
        "000011": "a",
        "000100": "o",
        "000101": "i",
        "000110": "n",
        "000111": "s",
        "001000": "h",
        "001001": "r",
        "001010": "d",
        "001011": "l",
        "001100": "u",
        "001101": "c",
        "001110": "m",
        "001111": "w",
        "010000": "f",
        "010001": "g",
        "010010": "y",
        "010011": "p",
        "010100": "b",
        "010101": "v",
        "010110": "k",
        "010111": "j",
        "011000": "x",
        "011001": "q",
        "011010": "z",
        "011011": ".",
        "011100": ",",
        "011101": "?",
        "011110": "0",
        "011111": "1",
        "100000": "2",
        "100001": "3",
        "100010": "4",
        "100011": "5",
        "100100": "6",
        "100101": "7",
        "100110": "8",
        "100111": "9",
        "101000": "!",
        "101001": "'"
    }
    result_list = []
    for piece in text_list:
        if piece not in dictionary:
            result_list.append("[UNKNOWN]")  # Handle unknown byte
        else:
            result_list.append(dictionary[piece])

    result = "".join(result_list)
    return result



def allowed_encrypt(text, alwd_chrts, false_chrts):
    text = text.lower()
    for x in text:
        if x not in alwd_chrts:
            false_chrts.append(x)

    if false_chrts:
        return False
    else:
        return True


def allowed_translate(text, binary):
    if len(text) % 6 != 0:
        return False
    for x in text:
        if x not in binary:
            return False
    return True

alwd_chrts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '?', ',','.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', "'", '’']
binary = ['0', '1']

print("ENCRYPTOR - TRANSLATOR\nWith this program, you can choose either to translate an encrypted text or encrypt a given text (there are limitations).")
while True:
    print("Choose:\n1. Translate encrypted text\n2. Encrypt a given text\n3. See limitations\n4. Exit")
    while True:
        choice = input("Enter 1, 2, 3 or 4: ").strip()
        if choice in ["1","2","3","4"]:
            break

    if choice == "3":
        print("This encryption method is limited to the following characters:\n", alwd_chrts)
        print("")
    elif choice == "2":
        while True:
            print("Paste/write your text below:")
            false_chrts = []
            text = input()
            if allowed_encrypt(text, alwd_chrts, false_chrts):
                break
            else:
                print("Error - Not allowed characters found: ", false_chrts)
        result = encrypt(text)
        print("Result:\n", result)
        while True:
            choice = input("Copy to clipboard? (y/n): ").lower().strip()
            if choice in ["y", "n"]:
                if choice == "y":
                    pyperclip.copy(result)
                else:
                    pass
                break
        print("")
    elif choice == "1":
        while True:
            print("Paste your encrypted text below:")
            text = input()
            if "[UNKNOWN]" in translate(text):
                print("Error - Wrong input")
            else:
                result = translate(text)
                print("Result:\n", result)
                break
        print("")
    elif choice == "4":
        break
