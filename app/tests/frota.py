import pandas as pd

class VerificadorFrota:
    def __init__(self, dataframe):
        self.df = pd.read_csv(dataframe)
        self.campos_obrigatorios = ["Id_veiculo", "Tipo veiculo", "Chassi", "Potencia", "ID da operadora", "Nome da operadora"]
        self.campos_nao_obrigatorios = ["obs", "Capacidade sentado", "Capacidade em pe", "Capacidade total", "Ano chassi", "Ano modelo", "Ar-condicionado"]

    def verificar_campos_obrigatorios(self):
        campos_obrig = []
        campos_faltantes = [campo for campo in self.campos_obrigatorios if campo not in self.df.columns]
        campos_obrig.append(campos_faltantes)
        return campos_faltantes

    def verificar_formato_datas(self):
        erros = []
        if "Ano chassi" in self.df.columns and not self.df["Ano chassi"].str.match(r"^\d{4}$").all():
            erros.append("Ano chassi com formato inválido")

        if "Ano modelo" in self.df.columns and not self.df["Ano modelo"].str.match(r"^\d{4}$").all():
            erros.append("Ano modelo com formato inválido")

        return erros

    def verificar_ar_condicionado(self):
        if "Ar-condicionado" in self.df.columns and not self.df["Ar-condicionado"].isin(["Sim", "Nao"]).all():
            return "Campo Ar-condicionado com valor inválido"
        return None

    def verificar_tipo_veiculo(self):
        tipos_validos = ["micro", "convencional", "articulado"]
        if "Tipo veiculo" in self.df.columns and not self.df["Tipo veiculo"].isin(tipos_validos).all():
            return "Campo Tipo veiculo com valor inválido"
        return None

    def verificar_capacidade_total(self):
        if "Capacidade sentado" in self.df.columns and "Capacidade em pe" in self.df.columns and "Capacidade total" in self.df.columns:
            total_esperado = self.df["Capacidade sentado"] + self.df["Capacidade em pe"]
            if not (total_esperado == self.df["Capacidade total"]).all():
                return "A soma de Capacidade sentado e Capacidade em pe não é igual a Capacidade total"
        return None

    def verificar_dataframe(self):
        erros = []
        erros.extend(self.verificar_campos_obrigatorios())
        erros.extend(self.verificar_formato_datas())
        ar_condicionado_erro = self.verificar_ar_condicionado()
        if ar_condicionado_erro:
            erros.append(ar_condicionado_erro)
        tipo_veiculo_erro = self.verificar_tipo_veiculo()
        if tipo_veiculo_erro:
            erros.append(tipo_veiculo_erro)
        capacidade_total_erro = self.verificar_capacidade_total()
        if capacidade_total_erro:
            erros.append(capacidade_total_erro)
        return erros
