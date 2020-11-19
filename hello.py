import streamlit as st
import pandas as pd
import numpy as np #NOT BEING USED CAN BE REMOVED

st.title('notas em ordem alfabética')

# creates the file uploader
uploaded_files = st.file_uploader('''insira o(s) arquivo(s) gerados pelo Teams
                                  de extensão .csv''',
                                  accept_multiple_files=True)

# reads all the files in to a data frame, cleans it and merges all of them in
# to one
df = pd.DataFrame() # the final data frame to be output
for uploaded_file in uploaded_files:

    # cleaning
    temp_df = pd.read_csv(uploaded_file, skiprows=[0], header=None)
    temp_df[0] = temp_df[0] + ' ' + temp_df[1]
    temp_df    = temp_df[[0,3]]
    temp_df.dropna(subset=[0], inplace = True)
    temp_df.rename(columns={0: 'Nome', 3: 'Nota'}, inplace = True)

    # concatenates all the files in to one
    df = pd.concat([df, temp_df])

# this while loop keeps the program from raising an error in case that no .csv
# file is uploaded
while True:
    try:
        # gets groups multiple entrys for the same student chosing the highest
        # grade
        df = df.groupby('Nome').max().reset_index()
    except:
        st.write('Insira um arquivo do tipo .csv')
        break

    st.dataframe(df)
    #st.table(df)
    break
