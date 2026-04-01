import random
import csv
import time
import pandas as pd
from datetime import datetime
import math
import re



def respond(result_str, method, lang_if_unsure="EN"):
    Response = [
        "Sure! Here's the result: ",
        "Got it! Calculating now...🤖\n",
        "Easy peasy! Here's the answer\n",
        "Alright! Let's do the math🧠\n",
        "Done!✨ Here's the total: "
    ]
    if 'can' in method or 'help' in method:
        print(f"\n(Zero)\n{random.choice(Response)}{result_str}")
        return "EN"
    elif 'boleh' in method or 'tolong' in method:
        print(f"\n(Zero)\nMesti boleh mah! {result_str}")
        return "MY"
    else:
        print(f"\n(Zero)\n{result_str}")
        return lang_if_unsure


def extract_numbers(method, keyword):
    parts = method.split(keyword)
    numbers = []
    for part in parts:
        try:
            num = float(part.strip(" ?!.").split()[-1])
            numbers.append(num)
        except:
            pass
    return numbers

def Invalid_input(reason=""):
    if reason:
        print(f"\n(Zero)\n{reason}")
    else:
        print("\n(Zero)\n ⚠️ Input not recognized. Try again with valid math operation ⚠️")
    return "EN"



#--- Advanced Operations(√, %, **, !) ---
def square_root(method):
    for keyword in ['√', 'square root of', 'square root', 'square of', 'square', 'punca kuasa dua']:
        if keyword in method:
            parts = method.split(keyword)
            try:
                if len(parts) > 1 and parts[1].strip():
                    num_str = parts[1].strip(" ?!.").split()[0]
                elif parts[0].strip():
                    num_str = parts[0].strip(" ?!.").split()[-1]
                else:
                    return Invalid_input("Invalid square root input")

                number = float(num_str)
                result = math.sqrt(number)
                user_input = f"√{number} ="
                today = datetime.now().strftime("%#m/%#d/%Y")
                with open('CSV/calculate_history.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    csv.writer(file).writerow([user_input, result, today])
                if 'punca kuasa dua' in keyword:
                    return respond(f"Punca kuasa dua bagi {number} ialah {result:.4f}", method, "MY")
                else:
                    return respond(f"√{number} = {result:.4f}", method, "EN")
            
            except:
                return Invalid_input("Invalid square root input")
    return None



def percentage(method):
    for keyword in ['%', 'percent', 'percentage', 'peratus', 'peratusan', 'daripada']:
        if keyword in method:
            try:
                method_clean = method.replace('%', '').replace('percent', '').replace('peratus', '')
                num = next(float(p.strip(" ?!.")) for p in method_clean.split() if p.replace('.', '', 1).isdigit())
                result = num / 100
                user_input = f"{num}% ="
                today = datetime.now().strftime("%#m/%#d/%Y")
                with open('CSV/calculate_history.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    csv.writer(file).writerow([user_input, result, today])
                if keyword in ['peratus', 'peratusan', 'daripada']:
                    return respond(f"Peratusan {num} ialah {result:.4f}", method, "MY")
                else:
                    return respond(f"{num}% = {result}", method, "EN")
            except:
                return Invalid_input("Invalid percentage format")
    return None


def exponentiation(method):
    for keyword in ['**', 'power of', 'raised to', 'kuasa', 'berpangkat']:
        if keyword in method:
            try:
                parts = method.split(keyword)
                num1 = float(parts[0].split()[-1])
                num2 = float(parts[1].strip(" ?!."))
                result = num1 ** num2
                user_input = f"{num1} ^ {num2} ="
                today = datetime.now().strftime("%#m/%#d/%Y")
                with open('CSV/calculate_history.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    csv.writer(file).writerow([user_input, result, today])
                if keyword in ['kuasa', 'berpangkat']:
                    return respond(f"{num1} dipangkatkan dengan {num2} = {result:.4f}", method, "MY")
                else:
                    return respond(f"{num1} ^ {num2} = {result}", method, "EN")
            except:
                return Invalid_input("Invalid exponent format")
    return None

def factorial(method):
    for keyword in ['!', 'factorial', 'faktorial', 'bang', 'silang']:
        if keyword in method:
            try:
                if '!' in method:
                    math_match = re.search(r'(\d+)\s*!', method)

                    if not math_match:
                        continue
                    num = int(math_match.group(1))

                else:
                    num_str = ''.join(filter(str.isdigit, method))
                    if not num_str:
                        return Invalid_input("Invalid input for factorial. Must be non-negative integer")
                    num = int(num_str)

                result = math.factorial(num)
                user_input = f"{num}!"
                today = datetime.now().strftime("%#m/%#d/%Y")
                with open('CSV/calculate_history.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    csv.writer(file).writerow([user_input, result, today])
                if keyword in ['faktorial', 'bang', 'silang']:
                    return respond(f"Faktorial {num} ialah {result}", method, "MY")
                else:
                    return respond(f"{num}! = {result}", method, "EN")
            except:
                return Invalid_input("Invalid input for factorial. Must be non-negative integer")
    return None



#--- Basic Operations (+, -, *, /) ---
def addition(method):
    for keyword in ['+', 'plus', 'add', 'tambah']:
        if keyword in method.lower():
            numbers = [int(n) for n in re.findall(r'\d+', method)]

            if not numbers:
                return respond("I couldn't find any numbers to add!", method, "EN")
            
            result = sum(numbers)
            user_input = " + ".join(map(str, numbers)) + " ="
            today = datetime.now().strftime("%#m/%#d/%Y")

            with open('CSV/calculate_history.csv', 'a', newline='', encoding='utf-8-sig') as file:
                csv.writer(file).writerow([user_input, result, today])

            return respond(f"{user_input} {result}", method, "MY" if keyword == "tambah" else "EN")
    return None


def subtraction(method):
    for keyword in ['-', 'minus', 'subtract', 'tolak', 'kurang']:
        if keyword in method.lower():

            numbers = [int(n) for n in re.findall(r'\d+', method)]

            if not numbers:
                return respond("I couldn't find any numbers to subtract!", method, "EN")

            result = numbers[0]
            for num in numbers[1:]:
                result -= num
                
            user_input = " - ".join(map(str, numbers)) + " ="
            today = datetime.now().strftime("%#m/%#d/%Y")
            
            with open('CSV/calculate_history.csv', 'a', newline='', encoding='utf-8-sig') as file:
                csv.writer(file).writerow([user_input, result, today])
            
            return respond(f"{user_input} {result}", method, "MY" if keyword in ['tolak', 'kurang'] else "EN")
    return None


def multiplication(method):
    for keyword in ['*', 'times', 'multiply', 'darab', 'kali']:
        if keyword in method.lower():
            numbers = [int(n) for n in re.findall(r'\d+', method)]

            if not numbers:
                return respond("I couldn't find any numbers to multiply!", method, "EN")
            result = 1
            for num in numbers:
                result *= num

            user_input = " * ".join(map(str, numbers)) + " ="
            today = datetime.now().strftime("%#m/%#d/%Y")

            with open('CSV/calculate_history.csv', 'a', newline='', encoding='utf-8-sig') as file:
                csv.writer(file).writerow([user_input, result, today])
            
            return respond(f"{user_input} {result:.2f}", method, "MY" if keyword in ['darab', 'kali'] else "EN")
    return None


def division(method):
    for keyword in ['/', 'divide', 'bahagi', 'bagi']:
        if keyword in method.lower():
            numbers = [int(n) for n in re.findall(r'\d+', method)]

            if not numbers:
                return respond("I couldn't find any numbers to divide!", method, "EN")
            
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    print("\n(Zero)\n❌ Cannot divide by zero ❌")
                    return "EN"
                result /= num

            user_input = " ÷ ".join(map(str, numbers)) + " ="
            today = datetime.now().strftime("%#m/%#d/%Y")

            with open('CSV/calculate_history.csv', 'a', newline='', encoding='utf-8-sig') as file:
                csv.writer(file).writerow([user_input, result, today])

            return respond(f"{user_input} {result:.2f}", method, "MY" if keyword == 'bahagi' else "EN")
    return None


def ZeroCalculator(method):
    method = method.lower()

    if re.fullmatch(r"[+\-*/^%! ]+", method):
        return Invalid_input("⚠️  Invalid input, please try again ⚠️")



    corrections = {
        'squar': 'square',  'squer': 'square', 'squaroot': 'square root', 'sqrt': 'square root',
        'factori': 'factorial', 'factrial': 'factorial',
        'percen': 'percent', 'percantage': 'percentage', 
        'powr': 'power of', 'raisd': 'raised to', 'rasied': 'raised to',
        'pls': 'plus', 'plss': 'plus', 'pluss': 'plus', 'plu': 'plus',
        'minu': 'minus', 'minss': 'minus', 'minss': 'minus',
        'subtrac': 'subtract', 'substract': 'subtract', 'subtrakt': 'subtract', 'subtractt': 'subtract',
        'time': 'times', 'timss': 'times', 'timess': 'times',
        'multipli': 'multiply', 'multipy': 'multiply', 'multipyli': 'multiply',
        'divit': 'divide', 'divid': 'divide', 'divde': 'divide', 'devid': 'divide',
        'b': 'by', 'bu': 'by',

        'puncakuasadu': 'punca kuasa dua', 'faktoriall': 'faktorial',
        'peratusn': 'peratus', 'daripda': 'daripada', 'daripda': 'daripada', 
        'kuas': 'kuasa', 'berpangakt': 'berpangkat',
        'bangg': 'bang', 'silangg': 'silang',
        'tamba': 'tambah', 'tambak': 'tambah',
        'tola': 'tolak', 'tolah': 'tolak',
        'kurag': 'kurang', 'kuragng': 'kurang', 'kuran': 'kurang',
        'darap': 'darab', 'darat': 'darab',
        'bahgi': 'bahagi', 'bahaghi': 'bahagi', 'bahagik': 'bahagi'
    }

    # --- spelling corrections ---
    words = method.split()
    for wrong_word, correct_word in corrections.items():
        if wrong_word in words:
            is_malay = correct_word in [
                'punca kuasa dua', 'peratusan', 'daripada', 'kuasa', 'berpangkat', 'bang', 
                'silang' 'tambah', 'tolak', 'kurang', 'darab', 'bahagi', 'bagi', 'faktorial'
                ]
            if is_malay:
                print(f"\n(Zero)\nMaksud anda '{correct_word}', betul?")
                if input("\n(Anda)\n").lower() not in ['ya', 'yes']:
                    print("\n(Zero)\nAduh! Cuba lagi ya.")
                    return "MY"                    
            else:
                print(f"\n(Zero)\nYou meant '{correct_word}', right?")
                if input("\n(You)\n").lower() not in ['yes', 'ya']:
                    print("\n(Zero)\nOops! Try again.")
                    return "EN"
            if 'yes' in method:                
                method = method.replace(wrong_word, correct_word)
                break
            else:
                method = method.replace(wrong_word, correct_word)
                break

    # --- Thanks message ---
    if any(kw in method for kw in ['thank', 'terima kasih', 'tq']):
        if 'thank' in method or 'tq' in method:
            print("\n(Zero)\nYou're welcome. Glad I could help! 😎")
        else:
            print("\n(Zero)\nSama-sama! Gembira dapat membantu! 😎")

        if lang == "MY":
            continuee = input("\n(Zero)\nAda lagi nak kira? (Tekan Enter atau taip 'Exit')\n\n(Anda)\n").strip().lower()
        else:
            continuee = input("\n(Zero)\nOne more? (Hit Enter or type 'Exit')\n\n(You)\n").strip().lower()
        
        if continuee == "exit":
            return "EXIT" 
        else:
            return "NORMAL"
        
    # --- All functions call ---
    for function in [square_root, percentage, exponentiation, factorial, addition, subtraction, multiplication, division]:
        lang_result = function(method)
        if lang_result:
            return lang_result

    # --- History ---
    if any(kw in method for kw in ['open', 'calculate history', 'buka', 'pengiraan sejarah']):
        try:
            try:
                history = pd.read_csv('CSV/calculate_history.csv', encoding='utf-8')
            except:
                history = pd.read_csv('CSV/calculate_history.csv', encoding='latin-1')

            pd.set_option('display.max_row', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.colheader_justify', 'center')
            if 'calculate' in method or 'history' in method:
                print("\n(Zero)\nSure! Here's your full calculation history:\n")
                print("    ----- Calculate History -----\n", history)
                return "EN"
            else:
                print("\n(Zero)\nBaik! Ini semua sejarah pengiraan anda:\n")
                print("    ----- Sejarah Pengiraan -----\n", history)
                return "MY"
        except :
            print("\n(Zero)\nNo calculation history found.")
        return "NORMAL"
    
    if any(kw in method for kw in ['clear', 'delete', 'history', 'bersihkan','hapus', 'sejarah']):
        try:
            with open('CSV/calculate_history.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(["User Input", "Result", "Date"])
            if any(kw in method for kw in ['bersihkan', 'hapus', 'sejarah']):
                print("\n(Zero)\nSejarah pengiraan telah berjaya dibersihkan! 🧹")
                return "MY"
            else:
                print("\n(Zero)\nHistory cleared successfully! 🧹")
                return "EN"
        except :
            print("\n(Zero)\nNo history file found to clear.")
        return "NORMAL"
        
    


print("---------------------------------------------\n")
print("   █████████╗ ███████╗██████╗  ██████╗")
print("    ╚═══████║ ██╔════╝██╔══██╗██╔═████╗")
print("      ████╔═╝ █████╗  ██████╔╝██║██ ██║")
print("    ████ ╔╝   ██╔══╝  ██╔══██╗████  ██║")
print("   █████████║ ███████╗██║  ██║╚██████╔╝")
print("   ╚════════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ \n\n")

print(" Hi! I'm Zero, your intelligent calculator 🤖")
print(" I can help with +, -, *, /, ^, sqrt, %, !")
print(" (Type 'Exit' to quit)")
print("---------------------------------------------")

lang = "NORMAL"

while True:
    if lang == "EN":
        user_input = input("\n(Zero)\nAnything else to calculate?\n\n(You)\n")
    elif lang == "MY":
        user_input = input("\n(Zero)\nAda lagi nak kira?\n\n(You)\n")
    else:
        user_input = input("\n(Zero)\nHow can I help you?\n\n(You)\n")

    user_input_lower = user_input.lower().strip()
    if any(phrase in user_input_lower for phrase in ["change to m","switch to m", "tukar ke b", "tukar ke m"]):
        lang = "MY"
        print("\n(Zero)\n✅ Bahasa Melayu diaktifkan!")
        continue
    elif any(phrase in user_input_lower for phrase in ["change to e", "switch to e", "tukar ke bahasa inggeris", "tukar ke e"]):
        lang = "EN"
        print("\n(Zero)\n✅ English language activated!")
        continue
    if user_input_lower == 'exit':
        print("\n(Zero)\nThis project is being closed...")
        time.sleep(2)
        print("Program close...\n")
        break

    # String Validation Layer
    math_keywords = ['add', 'plus', 'tambah', 'minus', 'tolak', 'darab', 'bahagi', 'punca', 'kuasa', 'square', 'root']
    greet_keywords = ["hello", "hi", "hey", "hallo", "halo", "apa khabar"]
    friendly_keywords = ["nice to meet you", "gembira berjumpa", "senang jumpa"]
    casual_keywords = ["what's up", "whatsapp", "sup", "wassup"]
    
    has_math_intent = any(word in user_input_lower for word in math_keywords) or any(op in user_input_lower for op in ['+', '-', '*', '/', '^'])

    if not has_math_intent:
        if user_input_lower.isdigit():
            msg = "Sorry, do you need to calculate something?" if lang != "MY" else "Maaf, anda mahu kira sesuatu ke? (contoh: tambah 10 dan 5)"
            print(f"\n(Zero)\n{msg}")
            continue
        elif any(phrase in user_input_lower for phrase in friendly_keywords):
            msg = "It's a pleasure to meet you! I'd willing to help anytime. 🧮" if lang != "MY" else "Saya pun gembira berjumpa anda! Saya sedia membantu kira-kira bila-bila masa. 🧮"
            print(f"\n(Zero)\n{msg}")
            continue
        elif any(phrase in user_input_lower for phrase in casual_keywords):
            msg = "What's up man!! I've been waiting for you for a long time"
            print(f"\n(Zero)\n{msg}")
            continue
        elif any(greet in user_input_lower for greet in greet_keywords):
            msg = "Hello! I'm Zero, your math assistant" if lang != "MY" else "Hai! Saya Zero, pembantu matematik anda."
            print(f"\n(Zero)\n{msg}")
            continue
        else:
            msg = "Sorry, I don't understand the Martian language 🤣" if lang != "MY" else "Maaf, saya tak faham bahasa Marikh ni 🤣"
            print(f"\n(Zero)\n{msg}")
            continue

    result_lang = ZeroCalculator(user_input)

    if result_lang in ["MY", "EN", "NORMAL"]:
        lang = result_lang
   
