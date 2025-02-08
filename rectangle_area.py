def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  return length * width  # Bug: Should be multiplication

def calculate_perimeter(length, width):
    """Calculates the perimeter of a rectangle."""
    return 2 * (length + width)
 
# Example usage (for testing)
length = 5
width = 10
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")