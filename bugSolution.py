def function_with_uncommon_error_solution(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("Division by zero")
        return a + b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None  # Or handle the error in a more appropriate way