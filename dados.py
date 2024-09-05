import pandas as pd
import os

print("Script iniciado")

# # Define o caminho do arquivo
# caminho_arquivo = r'C:\Users\Estante Magica\Desktop\DADOS\MICRODADOS_ENEM_2021.csv'
# print(f"Tentando carregar o arquivo: {caminho_arquivo}")

# Caminho relativo ao diretório do script
caminho_arquivo = os.path.join('MICRODADOS_ENEM_2021.csv')

# Carrega o CSV com pandas
df = pd.read_csv(caminho_arquivo, encoding='latin1')

# Exibe as primeiras linhas do dataframe
print(df.head())


# Verifica se o arquivo existe
if not os.path.exists(caminho_arquivo):
    print(f"O arquivo não foi encontrado em: {caminho_arquivo}")
else:
    # Carrega o arquivo CSV
    df = pd.read_csv(caminho_arquivo, sep=';', encoding='ISO-8859-1', low_memory=False)
    print("Arquivo carregado com sucesso")

    if df.empty:
        print("O DataFrame está vazio.")
    else:
        print("DataFrame não está vazio")
        print(df.head())
        print(df.info())
        print(df.describe())

        # Contar o número de participantes F ou M
        conteo_sexo = df['TP_SEXO'].value_counts()
        print("\nNúmero de participantes por gênero:")
        print(conteo_sexo)

        # Calcular a média da nota de redação F e M 
        media_redacao_por_genero = df.groupby('TP_SEXO')['NU_NOTA_REDACAO'].mean()
        print("\nMédia da nota de redação por gênero:")
        print(media_redacao_por_genero)

        # Nota mais alta por estado 
        estado_mais_alta_nota = df.groupby('SG_UF_PROVA')['NU_NOTA_REDACAO'].max()
        estado_max_nota = estado_mais_alta_nota.idxmax()
        nota_max = estado_mais_alta_nota.max()
        print(f"\nEstado com a nota do ENEM mais alta: {estado_max_nota} : {nota_max}")

        # Número de participantes masculinos e femininos
        num_masculinos = conteo_sexo.get('M', 0)
        num_femininos = conteo_sexo.get('F', 0)
        print(f"\nNúmero de participantes masculinos: {num_masculinos}")
        print(f"Número de participantes femininos: {num_femininos}")

        # Estado ou região com as melhores notas de redacao.
        estado_melhor_redacao = df.groupby('SG_UF_PROVA')['NU_NOTA_REDACAO'].mean()
        estado_max_redacao = estado_melhor_redacao.idxmax()
        nota_max_redacao = estado_melhor_redacao.max()
        print(f"\nEstado ou região com as melhores notas de redação: {estado_max_redacao}")

        # Contar o número de alunos por estado.
        contagem_por_estado = df['SG_UF_PROVA'].value_counts()
        print("\nNúmero de alunos por estado:")
        print(contagem_por_estado)

        # Adicionando cálculo de média, desvio padrão e mediana das notas por estado
        colunas_interesse = ['NU_NOTA_REDACAO', 'NU_NOTA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC'] 

        # Calcula a média, desvio padrão e mediana das notas por estado
        estatisticas_estado = df.groupby('SG_UF_PROVA').agg({c: ['mean', 'std', 'median'] for c in colunas_interesse})

        print("\nEstatísticas (média, desvio padrão e mediana) das notas por estado:")
        print(estatisticas_estado)

        # porcentagem de alunos por estado

        porcentagem_por_estado = ('SG_UF_PROVA' / df.shape[0]) * 100
        print("\nPorcentagem de alunos por estado:")
        print(porcentagem_por_estado)

print("Script finalizado")



