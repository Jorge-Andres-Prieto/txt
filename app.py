import streamlit as st
import pandas as pd


def process_file(content):
    # Convertir a minúsculas y eliminar comas
    text = content.replace(',', '').lower()

    # Separar el texto en palabras y crear un DataFrame
    words = text.split()
    df = pd.DataFrame(words, columns=['Words'])

    return df


# Aplicación Streamlit
st.title('Text Processor')

uploaded_file = st.file_uploader("Upload a text file (.txt)", type='txt')
if uploaded_file is not None:
    # Leer el contenido del archivo
    content = uploaded_file.getvalue().decode('utf-8')

    # Procesar el contenido del archivo
    df = process_file(content)

    # Mostrar el DataFrame procesado
    st.subheader("Processed Text")
    st.dataframe(df)

    # Preparar el archivo procesado para descargar
    processed_content = '\n'.join(df['Words'])
    st.download_button(
        label="Download Processed File",
        data=processed_content,
        file_name="processed_file.txt",
        mime='text/plain'
    )
