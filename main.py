def greet(name):
    """Simple function that returns a greeting message."""

    if not isinstance(name, str):
        raise ValueError("Input must be a string.")
    
    return f"Hello, {name}!"


def main():
    """Main function that calls greet and prints success."""
    result = greet("World")
    print(result)
    print("Success!")


if __name__ == "__main__":
    main()
