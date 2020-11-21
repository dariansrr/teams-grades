import streamlit as st
import pandas as pd
import numpy as np
from download_link import get_table_download_link

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
        # grade, sorts them alphabetically
        df = df.groupby('Nome').max().reset_index()
        df.sort_values('Nome', inplace = True)
        # make the indexes start at 1 for better visualization in streamlit
        df.index = np.arange(1, len(df) + 1)

    except:
        st.write('Insira um arquivo do tipo .csv')
        break

    # start visualization options
    if st.checkbox('tabela (melhor para copiar e colar)'):
        st.table(df)
    if st.checkbox('planilha (melhor para visualizar)'):
        st.dataframe(df)
    if st.checkbox('link para download'):
        st.markdown('''clique no link abaixo para fazer o download da planilha.
        note que é preciso adicionar **.csv** no final do arquivo para que ele
        funcione. ainda, caso tenha problemas para visualizar o arquivo no excel
        verifique suas configurações do excel para leitura de arquivos de CSV
        ''')
        st.markdown(get_table_download_link(df), unsafe_allow_html=True)

    break
#
