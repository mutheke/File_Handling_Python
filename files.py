def read_and_modify_file():
    # Ask user for the input filename
    input_filename = input("Please enter the filename to read: ")
    output_filename = input("Please enter the filename to write the modified content: ")

    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as file:
            content = file.read()  # Read the file content

        # Modify the content (For example, convert text to uppercase)
        modified_content = content.upper()

        # Try to write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)  # Write to the new file

        print(f"Content successfully written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading the file '{input_filename}' or writing to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
