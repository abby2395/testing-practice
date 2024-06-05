def add(num1, num2) -> int:
    try:
        if num1 > 0 and num2 > 0:
            return num1 + num2
        else:
            return "Error"
    except ValueError as err:
        return err