def decode(message_file_path):
  # Open the file and read its content.
  with open(message_file_path, "r") as file:
    lines = file.read().strip().split("\n")

  # Create a dictionary to store number-word pairs.
  num_word_dict = {}
  # Then populate the dictionary using the lines.
  for line in lines:
    num, word = line.split(maxsplit=1)
    num_word_dict[int(num)] = word

  # Calculate the height of the pyramid to determine the last number of each row.
  height = 1
  while sum(range(1, height + 1)) < len(num_word_dict):
    height += 1

  # Extract the last word of each row based on the pyramid structure.
  decoded_words = []
  last_num_in_row = 0
  for i in range(1, height + 1):
    last_num_in_row += i
    # Check if the last number is in the dictionary and add the word to the decoded message.
    if last_num_in_row in num_word_dict:
      decoded_words.append(num_word_dict[last_num_in_row])

  # Join and return the decoded message.
  return " ".join(decoded_words).lower()


# Test the decode function
message_file = "coding_qual_input.txt"
results = decode(message_file)
print(results)
