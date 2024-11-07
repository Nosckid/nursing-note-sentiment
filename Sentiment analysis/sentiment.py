# Necessary library
import os # For handling file paths and interactions with the Operating System.
import pandas as pd # For data manipulation and analysis, especially using DataFrames.
from textblob import TextBlob # For performing text processing, including sentiment analysis
from textblob.sentiments import NaiveBayesAnalyzer # Sentiment analysis model in TextBlob

# Set the directory of the current script
script_dir = os.path.dirname(__file__) # Gets the directory where the script is located

# Define relative path to the nursing notes CSV file
rel_path = '~/path to project/Data/notes_df.csv' # File path using a home directory placeholder (will need to be adjusted)

# Construct absolute path by joining script directory with the relative path
abs_file_path = os.path.join(script_dir, rel_path) # Ensures portability by creating an absolute path

# Load the nursing notes data into a DataFrame
nursing_notes_df = pd.read_csv(abs_file_path, header=0) # Reads CSV with headers from the first row

# Initialize lists to store polarity and subjectivity scores
polarity_vals = [] # List to store polarity scores (sentiment: negative to positive)
subjectivity_vals = [] # List to score subjectivity scores (factual to opinion-based)

# Create a sample of the DataFrame (full data used here but could be limited)
nursing_notes_df_sample = nursing_notes_df # Placeholder for sampling if needed.

# Initialize a counter for progress tracking.
count = 1 # Starts counting at 1 for human-readable output.

# Process each nursing note in the 'text' column of the sample DataFrame.
for note in nursing_notes_df_sample['text']:
	tb = TextBlob(note) # Create a TextBlob object from the nursing note text.

	# Append the calculated polarity and subjectivity values to their respective lists.
	polarity_vals.append(tb.sentiment.polarity) # Extracts and appends polarity score.
	subjectivity_vals.append(tb.sentiment.subjectivity) # Extracts and appends subjectivity score.

	# Print progress every 1000 notes processed.
	if count % 1000 == 0:
		print("Processed note #" + str(count)) # Outputs progress to console.
	count += 1 # Increment counter.

# Add new columns for polarity and subjectivity to the DataFrame.
nursing_notes_df_sample['polarity'] = polarity_vals # Add polarity scores as a new column.
nursing_notes_df_sample['subjectivity'] = subjectivity_vals # Adds subjectivity scores as a new column.

# Save the updated DataFrame to a new CSV file with sentiment analysis results.
nursing_notes_df_sample.to_csv("~/path to project/Data/notes_df_sntmnt.csv") # Exports to specified path.
