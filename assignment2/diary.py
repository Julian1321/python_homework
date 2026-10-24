import traceback

try:
    with open("diary.txt", "a") as file:
        first_entry = True

        while True:
            if first_entry:
                entry = input("What happened today? ")
                first_entry = False
            
            else:
                entry = input("what else? ")

            file.write(entry + "\n")

            if entry == "done for now":
                break

except Exception as e:
    print("An exception occurred.")
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    traceback.print_exc()