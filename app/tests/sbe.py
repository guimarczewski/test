import pandas as pd
import re

class VerificadorBilhetagem:
    def __init__(self, dataframe):
        self.df = pd.read_csv(dataframe)
        self.campos_obrigatorios = ["Data da Utilização", "Hora da Utilização", "Cartão do Usuário", "Tipo do Cartão", "Linha", "Prefixo do Veículo", "Valor Débito"]
        self.campos_nao_obrigatorios = ["Matrícula do Motorista", "Sentido", "Flag de desconto", "operador", "Latitude", "Longitude", "Stop_id"]

    def verificar_campos_obrigatorios(self):
        campos_obrig = []
        campos_faltantes = [campo for campo in self.campos_obrigatorios if campo not in self.df.columns]
        campos_obrig.append(campos_faltantes)
        return campos_obrig

    def verificar_formato_data_hora(self):
        erros = []
        if "Data da Utilização" in self.df.columns and not pd.to_datetime(self.df["Data da Utilização"], errors="coerce").notna().all():
            erros.append("Data da Utilização com formato inválido")

        if "Hora da Utilização" in self.df.columns and not self.df["Hora da Utilização"].str.match(r'^\d{2}:\d{2}:\d{2}$').all():
            erros.append("Hora da Utilização com formato inválido (HH:MM:SS)")

        return erros

    def verificar_flag_de_desconto(self):
        if "Flag de desconto" in self.df.columns and not self.df["Flag de desconto"].isin(["Integração", "Desconto de passagem"]).all():
            return "Campo Flag de desconto com valor inválido"
        return None

    def verificar_tipo_do_cartao(self):
        tipos_validos = ["Tipo A", "Tipo B", "Tipo C"]
        if "Tipo do Cartão" in self.df.columns and not self.df["Tipo do Cartão"].isin(tipos_validos).all():
            return "Campo Tipo do Cartão com valor inválido"
        return None

    def verificar_dataframe(self):
        erros = []
        erros.extend(self.verificar_campos_obrigatorios())
        erros.extend(self.verificar_formato_data_hora())
        flag_de_desconto_erro = self.verificar_flag_de_desconto()
        if flag_de_desconto_erro:
            erros.append(flag_de_desconto_erro)
        tipo_do_cartao_erro = self.verificar_tipo_do_cartao()
        if tipo_do_cartao_erro:
            erros.append(tipo_do_cartao_erro)
        return erros