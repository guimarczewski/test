import streamlit as st

from tests import VerificadorFrota
from tests import VerificadorGPS
from tests import VerificadorBilhetagem

def aplicar_verificacoes(bucket, dataframe):
    if bucket == "Frota":
        verificador = VerificadorFrota(dataframe)
    elif bucket == "Monitoramento":
        verificador = VerificadorGPS(dataframe)
    elif bucket == "Bilhetagem":
        verificador = VerificadorBilhetagem(dataframe)
    else:
        raise ValueError("Bucket desconhecido: escolha entre 'Frota', 'Monitoramento' ou 'Bilhetagem'.")

    erros = verificador.verificar_dataframe()

    if not erros:
        return True
    else:
        print(f"Erros encontrados no DataFrame do bucket '{bucket}':")
        for erro in erros:
            st.error(erro)