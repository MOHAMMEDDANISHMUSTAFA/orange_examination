# Box ID Checksum Calculator

This code calculates the checksum for a list of box IDs based on the number of IDs that contain exactly two or three repeated letters. The checksum is obtained by multiplying the counts together.

## Problem Description

Late at night, you need to scan the boxes in a warehouse and produce a list of likely candidates. To ensure accuracy, you scan the candidate boxes again and count the number that have an ID containing exactly two of any letter and separately count those with exactly three of any letter. The checksum is calculated by multiplying these two counts together.

For example, if you have the following box IDs:
- abcdef (no letters appear exactly two or three times)
- bababc (two 'a' and three 'b', counts for both)
- abbcde (two 'b', but no letter appears exactly three times)
- abcccd (three 'c', but no letter appears exactly two times)
- aabcdd (two 'a' and two 'd', counts once)
- abcdee (two 'e', but no letter appears exactly three times)
- ababab (three 'a' and three 'b', counts once)

The checksum for these box IDs would be calculated as 4 (number of IDs with exactly two repeated letters) multiplied by 3 (number of IDs with exactly three repeated letters) resulting in a checksum of 12.

## Usage

1. Place the list of box IDs in a text file, with each ID on a separate line. Make sure to name the file `aoc-day2-input.txt`.

2. Run the `calculate_box_id_checksum()` function in the provided Python code.

3. The code will read the input file, perform the calculations, and generate an output file named `aoc-day2.1-output.txt` containing the calculated checksum.

## Requirements

- Python 3.x

## File Description

- `aoc-day2-input.txt`: Input file containing the list of box IDs.
- `aoc-day2.1-output.txt`: Output file where the calculated checksum will be written.
- `box_id_checksum.py`: Python script that calculates the checksum for the box IDs.

## License

This code is released under the [MIT License](LICENSE).
