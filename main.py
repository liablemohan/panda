import pandas as pd

# Load the first CSV file
file_path_1 = 'samkSepa-rAmayana-rows - Sheet1.csv'  # Update the path
data_1 = pd.read_csv(file_path_1)

# Load the second CSV file
file_path_2 = 'samkSepa-rAmayana-rows - kAraka-sambamXa.csv'  # Update the path
data_2 = pd.read_csv(file_path_2)

# Reset index to ensure proper alignment
data_1.reset_index(drop=True, inplace=True)
data_2.reset_index(drop=True, inplace=True)

# Create a new list to store the output data
output_data = []

# Iterate through Document 1 and handle rows with hyphens in 'संस्कृतम्'
for index, row in data_1.iterrows():
    # Add two empty rows before the current row from Document 1
    output_data.append({
        'Index': '',
        'संस्कृतम्': '',
        'हिन्दी अर्ध': '',
        'English Meaning': '',
        'word': '',
        'sandhied_word': '',
        'kaaraka_sambandha': '',
        'hindi_meaning': '',
    })
    output_data.append({
        'Index': '',
        'संस्कृतम्': '',
        'हिन्दी अर्ध': '',
        'English Meaning': '',
        'word': '',
        'sandhied_word': '',
        'kaaraka_sambandha': '',
        'hindi_meaning': '',
    })
    
    # Add the current row from Document 1
    output_data.append({
        'Index': row['Index'],  # Add the "Index" from Document 1
        'संस्कृतम्': row['संस्कृतम्'],
        'हिन्दी अर्ध': row['हिन्दी अर्ध'],
        'English Meaning': row['English Meaning'],
        'word': '',  # Initially empty, will be filled by Document 2
        'sandhied_word': '',  # Initially empty, will be filled by Document 2
        'kaaraka_sambandha': '',  # Initially empty, will be filled by Document 2
        'hindi_meaning': '',  # Initially empty, will be filled by Document 2
    })
    
    # Check if there's a hyphen in 'संस्कृतम्' and handle the extra rows
    if '-' in row['संस्कृतम्']:
        # Count the number of hyphens
        num_hyphens = row['संस्कृतम्'].count('-')
        
        # Add that many empty rows below the current one
        for _ in range(num_hyphens):
            output_data.append({
                'Index': '',  # No index for extra rows
                'संस्कृतम्': '',  # Empty 'संस्कृतम्' for extra rows
                'हिन्दी अर्ध': '',
                'English Meaning': '',
                'word': '',  # Initially empty, will be filled by Document 2
                'sandhied_word': '',  # Initially empty, will be filled by Document 2
                'kaaraka_sambandha': '',  # Initially empty, will be filled by Document 2
                'hindi_meaning': '',  # Initially empty, will be filled by Document 2
            })

# Now, process Document 2 and add rows
data_2_index = 0  # Start from the first row in Document 2
for index, row in enumerate(output_data):
    # If we haven't reached the end of Document 2
    if data_2_index < len(data_2):
        # Only update rows with an empty 'word' field
        if row['word'] == '':
            output_data[index]['word'] = data_2.at[data_2_index, 'word']
            output_data[index]['sandhied_word'] = data_2.at[data_2_index, 'sandhied_word']
            output_data[index]['kaaraka_sambandha'] = data_2.at[data_2_index, 'kaaraka_sambandha']
            output_data[index]['hindi_meaning'] = data_2.at[data_2_index, 'hindi_meaning']
            data_2_index += 1  # Move to the next row in Document 2

# Convert the list of dictionaries to a DataFrame
output_df = pd.DataFrame(output_data)

# Save the final combined DataFrame to a new CSV file
output_file_path = 'rAmA5.csv'  # Update the path
output_df.to_csv(output_file_path, index=False)

print("Data analysis complete. The output CSV file has been created at:", output_file_path)
