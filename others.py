import pandas as pd
import base64
import streamlit as st

# currently there is no way to download data from streamlit, so Marc Skov
# Madsen <https://github.com/MarcSkovMadsen> created the workaround below
def get_table_download_link(df):

    csv = df.to_csv(index=False)
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">download do arquivo csv</a>'
    return href

# Since the tutorial is only some long markdown text, it has been moved here to
# unclog the main function.
def tutorial():
    text = ('''
            ### para que serve:
            até o presente momento, a ferramenta dedicada a aplicar avaliações
            do Teams (Micrososft) tem como única opção de visualização a lista
            de alunos orgazniza em ordem alfabética com base no segundo
            sobrenome. assim, este aplicativo tem como função principal *gerar
            uma planilha de notas ordenada a partir do primeiro nome dos
            alunos*.

            ainda, ele atende segunda demanda mais específica: *ler duas ou
            mais planilhas e mesclá-las em uma única*. esta função se mostrou
            particularmente útil nos casos onde uma mesma avaliação foi
            aplicada para duas turmas distintas.

            ### como utilizar:
            1. item
            2. item
            3. item

            ### alguns cuidados:

            ---
            ''')
    return st.markdown(text)
