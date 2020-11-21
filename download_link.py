import pandas as pd
import base64

# currently there is no way to download data from streamlit, so Marc Skov
# Madsen <https://github.com/MarcSkovMadsen> elaborated the workaround below


def get_table_download_link(df):

    csv = df.to_csv(index=False)
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">download do arquivo csv</a>'
    return href
