#!/bin/bash

# Directory containing the text files
dir="/home/khal/AIDS/Projekt2/AiDS-2/data/benchmark_with_spaces2"

# Iterate over the text files in the directory
for file in "$dir"/*.txt
do
    # Run the Python script with the -bst option and the text file as input
    python3 /home/khal/AIDS/Projekt2/AiDS-2/main.py -avl < "$file"
done