import os

folder = '/home/khal/AIDS/Projekt2/AiDS-2/data/benchmark_with_spaces2'

# Iterate over the files in the folder
for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder, filename)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Split the third line into numbers
        numbers = lines[2].split()

        # Remove the first number
        numbers.pop(0)

        # Join the numbers back into a string and replace the third line
        lines[2] = ' '.join(numbers) + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)