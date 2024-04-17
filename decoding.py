# Description: This program reads an encoded message from a text file and decodes it to reveal the original message.

def decode(message_file):
    # Initialise the required variables.
    pyramid = []
    decoded_message = ""

    # Read the Input File:
    # Open the given text file (coding_qual_input.txt) containing the encoded message.
    # Read each line from the file.
    # Parse Each Line:
    # Split each line into two parts: the number and the corresponding word.
    # Store the words in a data structure (e.g., a list).
    # Construct the Pyramid:
    # Arrange the words based on the ascending order of the numbers.
    # Form a pyramid structure where each line has one more word than the line above it.
    # Extract the Message Words:
    # Take the last word from each line of the pyramid.
    # Ignore all other words.
    # Join the Message Words:
    # Combine the extracted words to form the decoded message.
    # Return the Decoded Message:
    # Return the decoded message as a string.

    return decoded_message


# Test the decode function
message_file = "coding_qual_input.txt"
results = decode(message_file)
print(results)
