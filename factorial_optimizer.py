import logging

# Configure basic logging to track execution
logging.basicConfig(level=logging.INFO)

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.
    Includes input validation and error handling for robustness.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        test_val = 10
        logging.info(f"Calculating factorial for: {test_val}")
        print(f"Result: {calculate_factorial(test_val)}")
    except (TypeError, ValueError) as e:
        logging.error(f"Calculation failed: {e}")
