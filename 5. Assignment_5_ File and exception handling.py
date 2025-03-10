Assignment_5

# Exercise 1

filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


# Exercise 2

def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src_file:
            content = src_file.read()

        with open(destination_file, 'w') as dest_file:
            dest_file.write(content)

        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")

    except FileNotFoundError:
        print(f"The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = "C:/users/Neethu sethuraj/Documents/Source file.txt"
destination_file = "C:/Users/Neethu sethuraj/Documents/Destination file.txt"
copy_file_contents(source_file, destination_file)



# Exercise 3

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return "The file does not exist."

file_path = "C:/Users/Neethu sethuraj/Documents/D46_Sample_write.txt"
word_count = count_words_in_file(file_path)
print(f"Total number of words in the file: {word_count}")



# Exercise 4

def convert_to_integer():
    user_input = input("Please enter a number: ")

    try:
        number = int(user_input)
        print(f"The number you entered is: {number}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

convert_to_integer()



# Exercise 5

def check_negative_integers():
    user_input = input("Please enter a list of integers separated by spaces: ")

    try:
        integer_list = [int(i) for i in user_input.split()]

        for num in integer_list:
            if num < 0:
                raise ValueError(f"Negative integer found: {num}")

        print("All integers are non-negative.")

    except ValueError as e:
        print(f"Error: {e}")

check_negative_integers()



# Exercise 6

def compute_average():
    try:
        user_input = input("Please enter a list of integers separated by spaces: ")

        integer_list = [int(i) for i in user_input.split()]

        if len(integer_list) == 0:
            raise ValueError("The list is empty, cannot compute the average.")

        # Compute the average of the integers
        average = sum(integer_list) / len(integer_list)
        print(f"The average of the integers is: {average}")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        # Print a message indicating that the program has finished running
        print("The program has finished running.")

compute_average()


# Exercise 7

def write_to_file():
    try:
        filename = input("Please enter the filename: ")
        with open(filename, 'w') as file:
            file.write("Hello, welcome to the file!")

        print("The string has been written to the file successfully. Welcome!")

    except Exception as e:
        print(f"An error occurred: {e}")

write_to_file()

