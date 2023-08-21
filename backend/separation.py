import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = 'translated_nepali_captions.txt'  # Replace with the actual path to your text file

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()  # Remove leading and trailing whitespace
        if line:  # Check if the line is not empty
            parts = line.split(',')
            if len(parts) >= 2:
                image_id = parts[0]
                description = '\t'.join(parts[1:])
                print("Image ID:", image_id)
                print("Description:", description)
                print()  # Print an empty line for separation
            else:
                print("Invalid line format:", line)
