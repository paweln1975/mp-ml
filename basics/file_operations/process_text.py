def count_word_occurrences(filename: str, word:str) -> int:
    """
    Count the occurrences of a specific word in a text file.

    :param filename: The name of the file to read.
    :param word: The word to count in the file.
    :return: The number of occurrences of the word.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content.lower().split().count(word.strip().lower())

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

def is_numeric(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def sum_numbers_from_file(filename: str) -> float:
    """
    Sum all numbers in a text file.

    :param filename: The name of the file to read.
    :return: The sum of all numbers in the file.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            numbers = [float(num) for num in content.split() if is_numeric(num)]
            return sum(numbers)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

def count_words_in_files_and_save_to_file(input_file_name: str, output_file_name: str):
    """
    Count the occurrences of each word in a text file and save the results to another file.

    :param input_file_name: The name of the input file to read.
    :param output_file_name: The name of the output file to write the results.
    """
    try:
        with open(input_file_name, 'r') as infile:
            content = infile.read()
            words = content.lower().split()
            word_count = {}
            for word in words:
                word = word.strip('.,!?;"\'()[]{}')  # Remove punctuation
                if word:
                    word_count[word] = word_count.get(word, 0) + 1

        with open(output_file_name, 'w') as outfile:
            outfile.write(str(word_count))

        print(f"Word counts saved to '{output_file_name}'.")

    except FileNotFoundError:
        print(f"File '{input_file_name}' not found.")

if __name__ == "__main__":
    # Example usage
    file_name = "file_operations/text_data.txt"  # Replace with your file name
    word_to_count = "and"  # Replace with the word you want to count
    occurrences = count_word_occurrences(file_name, word_to_count)
    print(f"The word '{word_to_count}' occurs {occurrences} times in the file '{file_name}'.")

    file_name = "file_operations/numerical_data.txt"
    total_sum = sum_numbers_from_file(file_name)
    print(f"The sum of all numbers in the file '{file_name}' is {total_sum}.")

    file_name = "file_operations/text_data.txt"
    output_file = "word_count_output.txt"
    count_words_in_files_and_save_to_file(file_name, output_file)