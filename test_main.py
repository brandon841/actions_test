import main


def test_greet():
    """Test the greet function with different inputs."""
    # Test case 1
    result = main.greet("Alice")
    assert result == "Hello, Alice!", f"Expected 'Hello, Alice!' but got '{result}'"
    print(f"✓ Test 1 passed: {result}")
    
    # Test case 2
    result = main.greet("Bob")
    assert result == "Hello, Bob!", f"Expected 'Hello, Bob!' but got '{result}'"
    print(f"✓ Test 2 passed: {result}")
    
    # Test case 3
    result = main.greet("GitHub Actions")
    assert result == "Hello, GitHub Actions!", f"Expected 'Hello, GitHub Actions!' but got '{result}'"
    print(f"✓ Test 3 passed: {result}")
    
    # Test case 3
    result = main.greet(123) #should raise ValueError
    assert result == "Hello, 123!", f"Expected 'Hello, GitHub Actions!' but got '{result}'"
    print(f"✓ Test 3 passed: {result}")
    
    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    test_greet()
