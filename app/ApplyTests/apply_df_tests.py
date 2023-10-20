from streamlit import st

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

# Exemplo de uso:
# Carregue o DataFrame a partir de algum arquivo ou fonte de dados
df = pd.read_csv("seuarquivo.csv")

# Escolha o bucket apropriado
bucket_selecionado = "Monitoramento"  # Substitua pelo nome do bucket desejado

aplicar_verificacoes(bucket_selecionado, df)
