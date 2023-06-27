def calculate_box_id_checksum():
    """
    Calculates the checksum for a list of box IDs based on the number of IDs that contain exactly
    two or three repeated letters. The checksum is obtained by multiplying the counts together.
    Reads the list of box IDs from a file and writes the checksum to an output file.
    """

    input_file_path = 'aoc-day2-input.txt'  # File path of the input containing box IDs
    output_file_path = 'aoc-day2.1-output.txt'  # File path to write the calculated checksum

    print("Reading box IDs from input file:", input_file_path)

    with open(input_file_path, 'r') as input_file:
        box_ids = input_file.read().split('\n')  # Read the list of box IDs from the input file

        two_letter_count = 0  # Counter for box IDs with exactly two repeated letters
        three_letter_count = 0  # Counter for box IDs with exactly three repeated letters

        for box_id in box_ids:
            print("Processing box ID:", box_id)

            letter_counts = {}  # Dictionary to store the counts of each letter in the box ID

            for letter in box_id:
                letter_counts[letter] = letter_counts.get(letter, 0) + 1

            if 2 in letter_counts.values():  # Check if any letter appears exactly twice in the box ID
                two_letter_count += 1
                print(" - Contains exactly two repeated letters")

            if 3 in letter_counts.values():  # Check if any letter appears exactly three times in the box ID
                three_letter_count += 1
                print(" - Contains exactly three repeated letters")

    checksum = two_letter_count * three_letter_count  # Calculate the final checksum

    print("Calculation complete.")
    print("Number of box IDs with exactly two repeated letters:", two_letter_count)
    print("Number of box IDs with exactly three repeated letters:", three_letter_count)
    print("Checksum:", checksum)  # Print the calculated checksum

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(checksum))  # Write the checksum to the output file
        print("Checksum written to output file:", output_file_path)
