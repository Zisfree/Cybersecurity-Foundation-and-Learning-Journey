while True:
    try:
        x = int(input("Enter a number: "))
        break
    except Exception:
        print(f"Invalid input")
