MAX_ELEMENTS = 100

def calculate_sum(elements: list[int]) -> int:
   return sum(elements)

def get_number_of_elements() -> int:
   while True:
      try:
         num_elements = int(input("Enter the number of elements (1-100): "))
         if 1 <= num_elements <= MAX_ELEMENTS:
            return num_elements
         else:
            print("Invalid input. Please provide a number ranging from 1 to 100.")
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def get_elements(num_elements: int) -> list[int]:
   elements = []
   print(f"Enter {num_elements} integers:")
   for _ in range(num_elements):
      while True:
         try:
            elements.append(int(input()))
            break
         except ValueError:
            print("Invalid input. Please enter a valid integer.")
   return elements

def main() -> None:
   try:
      num_elements = get_number_of_elements()
      elements = get_elements(num_elements)
      total_sum = calculate_sum(elements)
      print("Sum of the numbers:", total_sum)
   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
      exit(1)

if __name__ == "__main__":
   main()
