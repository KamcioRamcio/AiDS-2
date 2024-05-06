import os

input_folder = '/home/khal/AIDS/Projekt2/AiDS-2/data/benchmark'
output_folder = '/home/khal/AIDS/Projekt2/AiDS-2/data/benchmark_with_spaces2'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over the files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)

        with open(input_file, 'r') as file:
            numbers = file.read().splitlines()

        numbers_with_spaces = ' '.join(numbers)

        with open(output_file, 'w') as file:
            file.write('insert\n')  # write 'insert' at the beginning of the file
            file.write(str(numbers[0]) + '\n')  # write the number of nodes
            file.write(numbers_with_spaces + '\n')  # write the numbers divided by spaces
            #file.write('minmax\n')  # write the numbers divided by spaces
            #file.write('print\n')
            file.write('exit\n')  # write 'exit' at the end of the file