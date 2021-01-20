import pandas as pd
import base64
import os
import streamlit as st
from PIL import Image

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
    # First part of the tutorial
    st.markdown('''
            ### para que serve
            até o presente momento, a ferramenta dedicada a aplicar avaliações
            do Teams (Micrososft) tem como única opção de visualização a lista
            de alunos orgaznizada em ordem alfabética com base no segundo
            sobrenome. assim, este aplicativo tem como função principal **gerar
            uma planilha de notas ordenada a partir do primeiro nome dos
            alunos**.

            ainda, ele atende segunda demanda mais específica: **ler duas ou
            mais planilhas e mesclá-las em uma única**. esta função se mostrou
            particularmente útil nos casos onde uma mesma avaliação foi
            aplicada para duas turmas distintas.

            ### como utilizar
            1. dentro do Teams, na avaliação em questão, exporte as notas para
            o excel. clickando nos três pontos no canto superior direito da
            tela:
            ''')

    # Pathing
    #print1 = os.path.join(os.path.abspath('images'), 'print1.jpg')

    # Print of the screen refered to
    image = Image.open('print1.jpg')
    st.image(image, use_column_width=True)

    # Second part of the tutorial
    st.markdown('''
            2. após clickar na opção de exportar, o arquivo será baixado para o
            seu computador (a opção padrão do Teams é a pasta padrão de
            Downloads de seu computador).
            3. caregue os arquivos no aplicativo arrastando os para o ícone
            abaixo ou, então, selecione os arquivos clickando em *Browse files*
            4. selecione uma (ou mais) das opções de visualização.

            ### alguns cuidados
            - em situações específicas, alguns alunos não são registrados no
            arquivo final. isto ocorre por conta da forma como o aluno se
            registrou/foi registrado no Teams e não por um erro de
            implementação deste aplicativo. nestes casos, o nome do aluno não
            será registrado na planilha final, não obstante se seu nome
            estiver lá a nota também estará. de todo modo, **é fortemente
            recomendando que confiram a planilha aqui gerada com suas
            respectivas listas de turma**.
            - ao mesclar planilhas, caso um mesmo aluno tenha duas ou mais
            notas distintas, o aplicativo privilegiará a maior.
            - a planilha final usará o termo *NaN* para indicar os casos onde o
            campo nota estiver em branco (o aluno não entregou a atividade).
            ---
            ''')
