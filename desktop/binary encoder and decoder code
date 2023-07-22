def string_to_binary(input_string):
    binary_message = " ".join(format(ord(char), '08b') for char in input_string)
    return binary_message

def binary_to_string(binary_message):
    binary_chunks = binary_message.split()
    text_message = "".join(chr(int(chunk, 2)) for chunk in binary_chunks)
    return text_message

print('epicboi55 made this fr')

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Encode text to binary")
    print("2. Decode binary to text")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        input_text = input("Enter a message: ")
        binary_result = string_to_binary(input_text)
        print("Binary representation of the message:")
        print(binary_result)
    elif choice == "2":
        binary_input = input("Enter binary message (space-separated 8-bit chunks): ")
        text_result = binary_to_string(binary_input)
        print("Decoded text message:")
        print(text_result)
    else:
        print("Invalid choice. Please enter either '1' or '2' to choose an option.")

input('press any button to close')
