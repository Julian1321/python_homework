# Write your code here.
def hello():
    return "Hello!"
def greet(name):
    return f"Hello, {name}!"
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError, ZeroDivisionError):
        return "Invalid data was provided."
def repeat(string, count):
    result = ""

    for i in range(count):
        result += string
    
    return result
def student_scores(option, **kwargs):
    if option == "best":
        return max(kwargs, key=kwargs.get)
    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs)
def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words= title.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return " ".join(result)
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if word[0] in vowels:
            new_word = word + "ay"
        else:
            index = 0 

            while index < len(word):
                if word[index] in vowels:
                    break
                if word[index:index + 2] == "qu":
                    index += 2
                    break
                index += 1
            
            new_word = word[index:] + word[:index] + "ay"
        result.append(new_word)
    return " ".join(result)