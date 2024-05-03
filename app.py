import streamlit as st
import pandas as pd

def process_file(input_file_path):
    # Read the file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove commas and convert to lowercase
    text = text.replace(',', '').lower()

    # Split the text into words and create a DataFrame
    words = text.split()
    df = pd.DataFrame(words, columns=['Words'])

    # Save the DataFrame to a new text file
    output_file_path = 'processed_file.txt'
    df.to_csv(output_file_path, index=False, header=False)

    return df, output_file_path

# Streamlit application
st.title('Text Processor')

# Assuming the file 'txt.txt' is in the same directory as the app
df, processed_file_path = process_file("txt.txt")

st.subheader("Processed Text")
st.dataframe(df)  # Display the DataFrame in a nice format


#with open(processed_file_path, "rb") as file:
#   st.download_button(
#        label="Download Processed File",
#        data=file,
#        file_name="processed_file.txt",
#        mime='text/plain'
#    )

