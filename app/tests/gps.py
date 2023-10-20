import pandas as pd
import re

class VerificadorGPS:
    def __init__(self, dataframe):
        self.df = pd.read_csv(dataframe)
        self.campos_obrigatorios = ["DataHora", "Id_veículo", "Linha", "Latitude", "Longitude"]
        self.campos_nao_obrigatorios = ["Velocidade", "Id_viagem", "Sentido", "Código da operadora"]

    def verificar_campos_obrigatorios(self):
        campos_obrig = []
        campos_faltantes = [campo for campo in self.campos_obrigatorios if campo not in self.df.columns]
        campos_obrig.append(campos_faltantes)
        return campos_obrig

    def verificar_formato_datas(self):
        erros = []
        if "DataHora" in self.df.columns and not pd.to_datetime(self.df["DataHora"], errors="coerce").notna().all():
            erros.append("DataHora com formato inválido")

        return erros

    def verificar_sentido(self):
        if "Sentido" in self.df.columns and not self.df["Sentido"].isin(["I", "V"]).all():
            return "Campo Sentido com valor inválido"
        return None

    def verificar_formato_gps(self):
        erros = []
        if "Latitude" in self.df.columns and not self.df["Latitude"].apply(lambda x: bool(re.match(r'^[-+]?[0-9]*\.?[0-9]+$', str(x)))).all():
            erros.append("Latitude com formato inválido")

        if "Longitude" in self.df.columns and not self.df["Longitude"].apply(lambda x: bool(re.match(r'^[-+]?[0-9]*\.?[0-9]+$', str(x)))).all():
            erros.append("Longitude com formato inválido")

        return erros

    def verificar_dataframe(self):
        erros = []
        erros.extend(self.verificar_campos_obrigatorios())
        erros.extend(self.verificar_formato_datas())
        erros.extend(self.verificar_formato_gps())
        sentido_erro = self.verificar_sentido()
        if sentido_erro:
            erros.append(sentido_erro)
        return erros