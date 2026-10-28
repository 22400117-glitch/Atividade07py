import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import streamlit as st

nome_aluno = "João Paulo Costa Souza"
numero_chamada = "22400117"
turma_aluno = "3B2"

azul = "#4f46e5"
laranja = "#d97706"
cores = ["#4f46e5", "#0d9488", "#d97706", "#e11d48", "#7c3aed"]
tamanho = (5.4, 3.9)

st.set_page_config(
    page_title="Atividade 06 - Gráficos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

sns.set_theme(
    style="whitegrid",
    rc={
        "figure.facecolor": "#ffffff",
        "axes.facecolor": "#ffffff",
        "axes.edgecolor": "#cbd5e1",
        "axes.labelcolor": "#475569",
        "axes.titlecolor": "#0f172a",
        "axes.titlesize": 13,
        "axes.labelsize": 10.5,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.titlepad": 14,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "grid.color": "#e2e8f0",
        "xtick.color": "#64748b",
        "ytick.color": "#64748b",
        "text.color": "#334155",
        "font.size": 10.5,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 9.5,
        "legend.frameon": False,
    },
)

estilo = """<style>
.stApp { background: #f3f5fa; }
.block-container { padding-top: 2.2rem; padding-bottom: 3rem; max-width: 1500px; }
footer { visibility: hidden; }
[data-testid="stSidebar"] { border-right: 1px solid #e2e8f0; }
.topo { background: linear-gradient(120deg, #4f46e5 0%, #7c3aed 100%); border-radius: 18px; padding: 1.7rem 2.1rem; margin-bottom: 0.6rem; box-shadow: 0 10px 30px rgba(79, 70, 229, 0.25); }
.topo-titulo { color: #ffffff; font-size: 1.9rem; font-weight: 700; line-height: 1.25; }
.topo-sub { color: #e0e7ff; font-size: 1rem; margin-top: 0.35rem; }
.secao { color: #6366f1; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; margin: 1.9rem 0 0.7rem 0.2rem; }
[data-testid="stImage"] img { background: #ffffff; border: 1px solid #e8ecf4; border-radius: 16px; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05), 0 8px 24px rgba(15, 23, 42, 0.06); }
.analise { background: #ffffff; border: 1px solid #e8ecf4; border-left: 5px solid #6366f1; border-radius: 16px; padding: 1.1rem 1.5rem 0.9rem 1.5rem; margin-top: 1rem; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05), 0 8px 24px rgba(15, 23, 42, 0.06); }
.analise-titulo { color: #0f172a; font-size: 1.05rem; font-weight: 700; margin-bottom: 0.4rem; }
.analise p { color: #334155; font-size: 0.95rem; line-height: 1.6; margin: 0.45rem 0; }
.tag { display: inline-block; background: #eef2ff; color: #4338ca; font-size: 0.78rem; font-weight: 700; padding: 0.08rem 0.65rem; border-radius: 999px; margin-right: 0.5rem; }
.aluno-titulo { color: #0f172a; font-size: 1.1rem; font-weight: 700; padding-bottom: 0.5rem; margin-bottom: 1.1rem; border-bottom: 3px solid #6366f1; display: inline-block; }
.aluno-campo { background: #f8fafc; border: 1px solid #e8ecf4; border-radius: 12px; padding: 0.7rem 0.95rem; margin-bottom: 0.75rem; }
.aluno-rotulo { color: #64748b; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }
.aluno-valor { color: #0f172a; font-size: 1.02rem; font-weight: 600; margin-top: 0.15rem; }
</style>"""

st.markdown(estilo, unsafe_allow_html=True)

dados_barras = pd.DataFrame({
    "categoria": [
        "Eletrônicos", "Eletrônicos", "Eletrônicos", "Eletrônicos", "Roupas", "Roupas",
        "Roupas", "Roupas", "Alimentos", "Alimentos", "Alimentos", "Alimentos",
        "Livros", "Livros", "Livros", "Livros", "Brinquedos", "Brinquedos",
        "Brinquedos", "Brinquedos",
    ],
    "regiao": [
        "Norte", "Sul", "Leste", "Oeste", "Norte", "Sul",
        "Leste", "Oeste", "Norte", "Sul", "Leste", "Oeste",
        "Norte", "Sul", "Leste", "Oeste", "Norte", "Sul",
        "Leste", "Oeste",
    ],
    "vendas_medias": [
        183.94, 72.57, 258.83, 130.2, 96.63, 60.19, 197.72, 219.39,
        54.15, 178.02, 106.62, 211.29, 93.59, 222.73, 146.68, 284.18,
        84.38, 135.27, 78.37, 281.17,
    ],
})

dados_boxplot = pd.DataFrame({
    "departamento": [
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    ],
    "salario": [
        9257.07, 6542.55, 7210.87, 5199.82, 4763.46, 4123.45, 5450.96, 9716.98,
        4282.73, 6468.81, 4737, 5948.3, 7296.96, 5774.8, 8906.91, 9684.46,
        3064.08, 5804.76, 7103.5, 8970.7, 6205.07, 6965.11, 4975.7, 4317.61,
        9529.42, 3807.88, 11075.08, 8269.01, 8189.95, 8007.07, 6557.8, 7686.15,
        6669.43, 7967.88, 6941.05, 5336.89, 5476.5, 5277.52, 8699.08, 5919.47,
        19600, 21000, 2087.9, 4396.84, 5514.52, 4773.08, 3396.68, 2413.19,
        3865.73, 3840.78, 3030.8, 4551.04, 5846.63, 4222.28, 4160.48, 3062.77,
        5397.41, 3924.86, 3421.04, 4063.69, 4471.96, 4139.22, 5206.15, 4383.97,
        3716.06, 4401.19, 4499.64, 2703.62, 5149.42, 3699.1, 3724.68, 4751.38,
        4747.17, 3299.17, 4802.9, 3439.55, 5819.57, 3171.81, 4239.48, 3217.98,
        6222.7, 2762.18, 11200, 12000, 4524.36, 3265.09, 3645.89, 4453.54,
        5224.58, 5623.4, 2463.05, 4267.75, 5459.49, 2314.69, 4314.38, 3997.92,
        4414.54, 3227.7, 2564.38, 2086.89, 4976.38, 5104.05, 4302.69, 3465.85,
        2376.95, 4563.35, 2899.22, 3288.7, 3413.44, 3802.46, 3240.96, 4033.46,
        3378.18, 4701.37, 5031.06, 4108.54, 4462.63, 6117.86, 2827.4, 2766.53,
        4695, 5946.54, 3739.5, 5726.83, 11200, 12000, 7168.76, 5808.45,
        5266.29, 8101.47, 5398.82, 7142.23, 9771.06, 6463.13, 9299.52, 4874.55,
        6065.66, 4537.5, 7127.74, 8365.14, 7131.58, 9147.34, 5688.94, 7394.35,
        6076.93, 7632.93, 7881.54, 8019.19, 5126.46, 5442.94, 5767.5, 6581.96,
        7152.58, 8239.16, 5515.83, 4198.22, 10772.55, 5019.96, 8463.57, 7054.72,
        7439.78, 6997.29, 6326.53, 7811.95, 6232.47, 9041.03, 19600, 21000,
    ],
})

dados_dispersao = pd.DataFrame({
    "altura_cm": [
        182, 188.2, 168.9, 179.8, 155.5, 177.8, 168.4, 156.4, 180.3, 151.9,
        150.9, 173.6, 175.7, 179.7, 177.4, 184.8, 177, 168.7, 169.3, 167.2,
        173, 159, 173.4, 169.1, 172.8, 172.8, 145.5, 161, 168.9, 169.4,
        172.6, 173, 185.2, 173.1, 166.9, 154, 156.3, 175.4, 180.6, 185.4,
        161.7, 167, 172.4, 190.5, 171.1, 185.5, 171.7, 181.5, 180.3, 171.7,
        159.8, 167.3, 184.9, 178.8, 165.7, 166.6, 152.7, 184.4, 178.9, 168.6,
        172, 148.3, 165.1, 183.3, 179.8, 173.3, 169.9, 178, 167.2, 153.4,
        169.9, 174, 181.2, 155.6, 168.8, 169.2, 159, 174.9, 177.5, 167.1,
        190.6, 166.8, 165.5, 165.2, 161.8, 164.4, 155.7, 168.1, 170.6, 147.2,
        169, 170.4, 175.1, 182, 178.5, 163.8, 162.6, 175.8, 164.5, 157.7,
        193.7, 166.9, 163.7, 148.1, 178.5, 160.1, 170.3, 179.7, 160.3, 170.8,
        185.2, 145.4, 161.9, 161, 168.1, 169.5, 159.4, 163.5, 162.3, 166.5,
        172.2, 179.1, 180.6, 176.5, 161.3, 170, 193.7, 180.1, 165.6, 185.8,
        166.1, 163.3, 184, 156.9, 150.9, 179.4, 170.3, 171.3, 166.4, 167.6,
        165.4, 163.7, 166.2, 165.9, 161.7, 164.5, 145, 176.8, 173.9, 169.2,
    ],
    "peso_kg": [
        75, 80.7, 58.4, 69.1, 52.6, 71.1, 71.8, 58.9, 77, 42.9,
        43, 61.3, 69.5, 58, 67.4, 74.8, 61.7, 65.8, 56.6, 61.8,
        79.6, 45.1, 65.3, 60.2, 62.5, 69.3, 46.5, 58.7, 58.4, 74.7,
        56.5, 60.6, 77.5, 66.3, 62.6, 56.5, 50.1, 68.4, 69.6, 79.8,
        54, 58.7, 67.9, 86.6, 53, 78.8, 63.2, 78.1, 71, 71,
        50.4, 49.4, 81.7, 66.7, 51.2, 60, 46.2, 80.1, 75.4, 62.2,
        60.4, 44.9, 59.4, 77.9, 67.5, 64, 65.4, 76.4, 65.3, 48.4,
        60.5, 68.6, 67.6, 45.9, 69.4, 64.3, 51.4, 71.5, 76.2, 58.2,
        79.4, 57.4, 63.8, 63.6, 62.6, 63, 41.9, 62.7, 58.2, 39.9,
        62.9, 67.6, 63.2, 62.2, 71.6, 70.6, 55.4, 68.5, 67, 54.9,
        85.5, 62.4, 58.6, 37.6, 64, 63.5, 64.2, 72.2, 53.8, 67.6,
        89.4, 43.5, 52.8, 54.2, 66.7, 59.7, 57.7, 45.5, 54.9, 63,
        71.3, 67.1, 65, 67.6, 49.5, 62.2, 84.3, 65.5, 63.1, 76.5,
        64.9, 47.8, 70.5, 53.8, 41.8, 70.6, 63.3, 64.9, 56.4, 61.6,
        55, 60.7, 59, 60.1, 68.4, 52.6, 47.4, 55.9, 56.1, 56,
    ],
    "sexo": [
        "Feminino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Masculino",
        "Masculino", "Masculino", "Feminino", "Feminino", "Feminino", "Masculino", "Feminino", "Feminino",
        "Feminino", "Masculino", "Masculino", "Masculino", "Feminino", "Feminino", "Feminino", "Masculino",
        "Masculino", "Feminino", "Masculino", "Masculino", "Masculino", "Masculino", "Feminino", "Masculino",
        "Masculino", "Masculino", "Masculino", "Feminino", "Feminino", "Masculino", "Masculino", "Masculino",
        "Masculino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino", "Masculino",
        "Feminino", "Feminino", "Feminino", "Feminino", "Feminino", "Feminino", "Masculino", "Feminino",
        "Feminino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Masculino",
        "Feminino", "Feminino", "Masculino", "Feminino", "Masculino", "Masculino", "Masculino", "Masculino",
        "Masculino", "Feminino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino",
        "Feminino", "Masculino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino",
        "Feminino", "Masculino", "Masculino", "Masculino", "Feminino", "Feminino", "Masculino", "Masculino",
        "Feminino", "Feminino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino",
        "Feminino", "Feminino", "Feminino", "Feminino", "Feminino", "Masculino", "Feminino", "Feminino",
        "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino", "Masculino", "Feminino",
        "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino", "Masculino", "Masculino",
        "Masculino", "Masculino", "Feminino", "Feminino", "Masculino", "Feminino", "Feminino", "Feminino",
        "Feminino", "Masculino", "Masculino", "Feminino", "Masculino", "Masculino", "Masculino", "Feminino",
        "Feminino", "Feminino", "Masculino", "Feminino", "Feminino", "Masculino",
    ],
})

dados_distribuicao = pd.DataFrame({
    "idade": [
        24, 28, 19, 33, 29, 24, 21, 22, 25, 24, 30, 23, 28, 25, 26, 24, 29, 29, 27, 28,
        20, 27, 31, 27, 20, 25, 27, 21, 18, 23, 21, 25, 18, 28, 22, 30, 24, 25, 24, 22,
        37, 23, 30, 20, 27, 27, 25, 22, 24, 23, 37, 25, 28, 34, 21, 25, 24, 25, 24, 21,
        26, 20, 30, 28, 23, 23, 26, 21, 34, 27, 27, 28, 22, 30, 26, 30, 24, 32, 27, 36,
        23, 26, 20, 22, 28, 31, 40, 25, 20, 29, 19, 28, 22, 26, 30, 24, 30, 29, 18, 20,
        18, 35, 24, 34, 18, 22, 29, 26, 28, 19, 32, 29, 27, 22, 27, 24, 18, 25, 24, 30,
        27, 47, 36, 48, 48, 44, 51, 35, 54, 39, 33, 43, 28, 47, 43, 55, 50, 34, 38, 49,
        52, 55, 55, 44, 48, 55, 43, 48, 42, 41, 45, 39, 44, 37, 43, 49, 40, 45, 46, 49,
        44, 54, 28, 69, 38, 48, 37, 50, 47, 40, 54, 44, 49, 38, 45, 61, 53, 47, 41, 46,
        47, 49, 36, 50, 36, 58, 39, 47, 53, 43, 48, 56, 50, 48, 32, 38, 53, 50, 51, 50,
    ],
})

dados_frequencia = pd.DataFrame({
    "tipo_atendimento": [
        "Bug", "Dúvida", "Elogio", "Bug", "Reclamação", "Reclamação",
        "Dúvida", "Dúvida", "Bug", "Cancelamento", "Reclamação", "Dúvida",
        "Dúvida", "Elogio", "Bug", "Bug", "Bug", "Reclamação",
        "Dúvida", "Dúvida", "Bug", "Reclamação", "Dúvida", "Dúvida",
        "Elogio", "Dúvida", "Dúvida", "Reclamação", "Elogio", "Elogio",
        "Dúvida", "Elogio", "Dúvida", "Dúvida", "Elogio", "Reclamação",
        "Bug", "Elogio", "Reclamação", "Dúvida", "Dúvida", "Dúvida",
        "Dúvida", "Cancelamento", "Dúvida", "Bug", "Reclamação", "Bug",
        "Reclamação", "Reclamação", "Reclamação", "Dúvida", "Elogio", "Dúvida",
        "Dúvida", "Reclamação", "Dúvida", "Cancelamento", "Cancelamento", "Cancelamento",
        "Dúvida", "Dúvida", "Cancelamento", "Reclamação", "Cancelamento", "Cancelamento",
        "Bug", "Dúvida", "Dúvida", "Bug", "Dúvida", "Dúvida",
        "Reclamação", "Cancelamento", "Elogio", "Reclamação", "Dúvida", "Reclamação",
        "Cancelamento", "Dúvida", "Reclamação", "Bug", "Elogio", "Elogio",
        "Elogio", "Dúvida", "Dúvida", "Bug", "Bug", "Bug",
        "Cancelamento", "Reclamação", "Reclamação", "Bug", "Reclamação", "Elogio",
        "Bug", "Bug", "Dúvida", "Dúvida", "Dúvida", "Reclamação",
        "Dúvida", "Reclamação", "Reclamação", "Dúvida", "Reclamação", "Dúvida",
        "Dúvida", "Bug", "Dúvida", "Dúvida", "Reclamação", "Bug",
        "Dúvida", "Reclamação", "Dúvida", "Dúvida", "Reclamação", "Reclamação",
        "Reclamação", "Elogio", "Cancelamento", "Reclamação", "Dúvida", "Bug",
        "Dúvida", "Reclamação", "Dúvida", "Dúvida", "Cancelamento", "Bug",
        "Elogio", "Reclamação", "Dúvida", "Dúvida", "Dúvida", "Reclamação",
        "Elogio", "Elogio", "Dúvida", "Cancelamento", "Elogio", "Reclamação",
        "Reclamação", "Reclamação", "Dúvida", "Dúvida", "Bug", "Dúvida",
        "Dúvida", "Dúvida", "Dúvida", "Bug", "Elogio", "Reclamação",
        "Dúvida", "Reclamação", "Reclamação", "Dúvida", "Reclamação", "Dúvida",
        "Reclamação", "Reclamação", "Dúvida", "Dúvida", "Reclamação", "Reclamação",
        "Bug", "Elogio", "Dúvida", "Dúvida", "Reclamação", "Dúvida",
        "Reclamação", "Cancelamento", "Reclamação", "Dúvida", "Reclamação", "Reclamação",
        "Reclamação", "Cancelamento", "Dúvida", "Cancelamento", "Cancelamento", "Dúvida",
        "Dúvida", "Dúvida", "Dúvida", "Dúvida", "Elogio", "Dúvida",
        "Dúvida", "Bug", "Dúvida", "Bug", "Dúvida", "Dúvida",
        "Elogio", "Reclamação", "Bug", "Elogio", "Bug", "Dúvida",
        "Dúvida", "Bug", "Bug", "Cancelamento", "Reclamação", "Dúvida",
        "Bug", "Dúvida", "Cancelamento", "Bug", "Reclamação", "Bug",
        "Bug", "Dúvida", "Cancelamento", "Reclamação", "Bug", "Dúvida",
        "Bug", "Dúvida", "Dúvida", "Cancelamento", "Dúvida", "Dúvida",
        "Cancelamento", "Cancelamento", "Reclamação", "Reclamação", "Reclamação", "Dúvida",
        "Dúvida", "Elogio", "Bug", "Bug", "Bug", "Dúvida",
        "Reclamação", "Dúvida", "Reclamação", "Reclamação", "Bug", "Dúvida",
        "Dúvida", "Dúvida", "Bug", "Reclamação", "Dúvida", "Dúvida",
        "Elogio", "Dúvida", "Bug", "Elogio", "Dúvida", "Dúvida",
        "Cancelamento", "Dúvida", "Dúvida", "Bug", "Cancelamento", "Cancelamento",
        "Bug", "Dúvida", "Dúvida", "Bug", "Reclamação", "Reclamação",
        "Cancelamento", "Dúvida", "Reclamação", "Dúvida", "Reclamação", "Dúvida",
        "Dúvida", "Dúvida", "Reclamação", "Elogio", "Reclamação", "Cancelamento",
        "Dúvida", "Dúvida", "Bug", "Dúvida", "Cancelamento", "Dúvida",
        "Cancelamento", "Dúvida", "Bug", "Reclamação", "Cancelamento", "Dúvida",
        "Reclamação", "Cancelamento", "Reclamação", "Reclamação", "Elogio", "Reclamação",
    ],
})

dados_heatmap = pd.DataFrame(
    {
        "8:00": [
            90, 33, 88, 51, 63, 142, 113,
        ],
        "10:00": [
            89, 75, 93, 31, 97, 74, 49,
        ],
        "12:00": [
            84, 47, 58, 49, 54, 139, 199,
        ],
        "14:00": [
            83, 98, 68, 25, 44, 144, 49,
        ],
        "16:00": [
            44, 71, 81, 22, 60, 64, 151,
        ],
        "18:00": [
            26, 85, 33, 30, 55, 49, 197,
        ],
        "20:00": [
            52, 30, 60, 97, 28, 164, 78,
        ],
    },
    index=["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],
)

dados_linhas = pd.DataFrame({
    "data": pd.to_datetime([
        "2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05", "2026-01-06",
        "2026-01-07", "2026-01-08", "2026-01-09", "2026-01-10", "2026-01-11", "2026-01-12",
        "2026-01-13", "2026-01-14", "2026-01-15", "2026-01-16", "2026-01-17", "2026-01-18",
        "2026-01-19", "2026-01-20", "2026-01-21", "2026-01-22", "2026-01-23", "2026-01-24",
        "2026-01-25", "2026-01-26", "2026-01-27", "2026-01-28", "2026-01-29", "2026-01-30",
        "2026-01-31", "2026-02-01", "2026-02-02", "2026-02-03", "2026-02-04", "2026-02-05",
        "2026-02-06", "2026-02-07", "2026-02-08", "2026-02-09", "2026-02-10", "2026-02-11",
        "2026-02-12", "2026-02-13", "2026-02-14", "2026-02-15", "2026-02-16", "2026-02-17",
        "2026-02-18", "2026-02-19", "2026-02-20", "2026-02-21", "2026-02-22", "2026-02-23",
        "2026-02-24", "2026-02-25", "2026-02-26", "2026-02-27", "2026-02-28", "2026-03-01",
        "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05", "2026-03-06", "2026-03-07",
        "2026-03-08", "2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13",
        "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19",
        "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25",
        "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31",
    ]),
    "vendas": [
        107.45, 99.61, 113.09, 127.9, 103.23, 104.91, 133.8, 123.31,
        106.44, 123.31, 109.9, 111.55, 123.85, 93.21, 97.72, 116.85,
        111.77, 133.37, 116.72, 110.84, 155.69, 132.01, 138.09, 117.39,
        132.28, 143.8, 126.56, 151.14, 138.18, 144.5, 141.54, 180.03,
        153.73, 139.75, 169.64, 140.68, 163.81, 132.96, 144.12, 168.68,
        178.49, 171.67, 169.05, 167.96, 151.98, 165.05, 170.62, 195.07,
        186.05, 156.14, 189.13, 180.18, 177.49, 198.5, 206.48, 206.67,
        181.79, 191.43, 202.72, 214.07, 193.94, 200.02, 187.9, 188.24,
        220.05, 229.89, 210.16, 227.97, 220.03, 206.62, 223.4, 242.73,
        220.81, 246.5, 185.42, 238.73, 229.4, 225.29, 232.84, 203.33,
        231.54, 241.87, 260.37, 232.11, 229.45, 235.73, 258.67, 251.56,
        240.37, 257.7,
    ],
    "loja": [
        "Loja B", "Loja B", "Loja A", "Loja B", "Loja B", "Loja A", "Loja B", "Loja A",
        "Loja A", "Loja B", "Loja A", "Loja A", "Loja A", "Loja A", "Loja B", "Loja A",
        "Loja B", "Loja A", "Loja A", "Loja A", "Loja A", "Loja B", "Loja B", "Loja A",
        "Loja A", "Loja B", "Loja A", "Loja A", "Loja A", "Loja B", "Loja B", "Loja B",
        "Loja A", "Loja A", "Loja B", "Loja B", "Loja B", "Loja B", "Loja A", "Loja B",
        "Loja A", "Loja B", "Loja A", "Loja B", "Loja B", "Loja B", "Loja B", "Loja A",
        "Loja B", "Loja A", "Loja A", "Loja A", "Loja A", "Loja B", "Loja A", "Loja A",
        "Loja A", "Loja B", "Loja B", "Loja B", "Loja B", "Loja A", "Loja A", "Loja B",
        "Loja A", "Loja A", "Loja A", "Loja B", "Loja B", "Loja A", "Loja B", "Loja B",
        "Loja B", "Loja B", "Loja B", "Loja A", "Loja B", "Loja A", "Loja A", "Loja B",
        "Loja A", "Loja A", "Loja A", "Loja B", "Loja B", "Loja A", "Loja B", "Loja B",
        "Loja B", "Loja B",
    ],
})

def nova_figura():
    return plt.subplots(figsize=tamanho, layout="constrained")


def grafico_barras():
    fig, ax = nova_figura()
    sns.barplot(data=dados_barras, x="categoria", y="vendas_medias", hue="regiao", palette=cores[:4], ax=ax)
    ax.set(title="Vendas médias por categoria e região", xlabel="", ylabel="Vendas médias", ylim=(0, 340))
    sns.move_legend(ax, "upper center", ncol=4, title=None, fontsize=9)
    return fig


def grafico_pizza():
    fig, ax = nova_figura()
    fatias, rotulos, percentuais = ax.pie(
        x=[45000, 32000, 21000, 8000, 14000],
        labels=["Site", "Loja Física", "Aplicativo", "Telefone", "Parceiros"],
        colors=cores,
        autopct=lambda p: f"{p:.1f}%".replace(".", ","),
        startangle=90,
        counterclock=False,
        pctdistance=0.79,
        wedgeprops={"width": 0.42, "edgecolor": "white", "linewidth": 2},
    )
    plt.setp(percentuais, color="white", fontweight="bold", fontsize=9)
    ax.text(0, 0, "120.000\nfaturamento", ha="center", va="center", fontsize=11, fontweight="bold", color="#0f172a")
    ax.set(title="Faturamento por canal de venda")
    return fig


def grafico_frequencia():
    fig, ax = nova_figura()
    sns.countplot(
        data=dados_frequencia,
        x="tipo_atendimento",
        order=["Dúvida", "Reclamação", "Bug", "Cancelamento", "Elogio"],
        color=azul,
        ax=ax,
    )
    ax.bar_label(ax.containers[0], fontsize=10, color="#334155")
    ax.set(title="Chamados por tipo de atendimento", xlabel="", ylabel="Quantidade de chamados", ylim=(0, 132))
    return fig


def grafico_distribuicao():
    fig, ax = nova_figura()
    sns.histplot(data=dados_distribuicao, x="idade", kde=True, color=azul, edgecolor="white", ax=ax)
    media = dados_distribuicao["idade"].mean()
    mediana = dados_distribuicao["idade"].median()
    ax.axvline(media, color=laranja, linestyle="--", linewidth=1.6, label=f"Média ({media:.1f})".replace(".", ","))
    ax.axvline(mediana, color="#e11d48", linestyle="--", linewidth=1.6, label=f"Mediana ({mediana:.0f})")
    ax.legend(fontsize=9)
    ax.set(title="Distribuição de idade dos clientes", xlabel="Idade (anos)", ylabel="Frequência")
    return fig


def grafico_boxplot():
    fig, ax = nova_figura()
    sns.boxplot(
        data=dados_boxplot,
        x="departamento",
        y="salario",
        hue="departamento",
        palette=cores[:4],
        width=0.55,
        legend=False,
        ax=ax,
    )
    ax.set(title="Salário por departamento", xlabel="", ylabel="Salário")
    return fig


def grafico_dispersao():
    fig, ax = nova_figura()
    sns.scatterplot(
        data=dados_dispersao,
        x="altura_cm",
        y="peso_kg",
        hue="sexo",
        palette=[azul, laranja],
        s=45,
        alpha=0.8,
        edgecolor="white",
        ax=ax,
    )
    sns.move_legend(ax, "upper left", title=None)
    ax.set(title="Altura × peso por sexo", xlabel="Altura (cm)", ylabel="Peso (kg)")
    return fig


def grafico_linhas():
    fig, ax = nova_figura()
    sns.lineplot(
        data=dados_linhas,
        x="data",
        y="vendas",
        hue="loja",
        hue_order=["Loja A", "Loja B"],
        palette=[azul, laranja],
        linewidth=1.8,
        ax=ax,
    )
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))
    sns.move_legend(ax, "upper left", title=None)
    ax.set(
        title="Vendas diárias por loja",
        xlabel="",
        ylabel="Vendas",
        xlim=(dados_linhas["data"].min(), dados_linhas["data"].max()),
    )
    return fig


def grafico_heatmap():
    fig, ax = nova_figura()
    sns.heatmap(
        data=dados_heatmap,
        annot=True,
        fmt="d",
        cmap="YlGnBu",
        linewidths=1.5,
        linecolor="white",
        cbar=False,
        annot_kws={"size": 9},
        ax=ax,
    )
    ax.set(title="Movimento de clientes por dia e horário", xlabel="", ylabel="")
    ax.tick_params(axis="both", length=0)
    return fig


def mostrar(figura):
    memoria = io.BytesIO()
    figura.savefig(memoria, format="png", dpi=200)
    st.image(memoria)
    plt.close(figura)


def secao(texto):
    st.markdown(f'<div class="secao">{texto}</div>', unsafe_allow_html=True)


def analise(itens):
    paragrafos = ""
    for rotulo, texto in itens:
        paragrafos += f'<p><span class="tag">{rotulo}</span>{texto}</p>'
    st.markdown(
        f'<div class="analise"><div class="analise-titulo">Análise</div>{paragrafos}</div>',
        unsafe_allow_html=True,
    )

with st.sidebar:
    st.markdown(
        '<div class="aluno-titulo">Informações do aluno</div>'
        f'<div class="aluno-campo"><div class="aluno-rotulo">Nome</div><div class="aluno-valor">{nome_aluno}</div></div>'
        f'<div class="aluno-campo"><div class="aluno-rotulo">Número da chamada</div><div class="aluno-valor">{numero_chamada}</div></div>'
        f'<div class="aluno-campo"><div class="aluno-rotulo">Turma</div><div class="aluno-valor">{turma_aluno}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="topo">'
    '<div class="topo-titulo">Atividade 06 - Painel de gráficos</div>'
    '<div class="topo-sub">Oito conjuntos de dados, oito gráficos e uma análise para cada grupo</div>'
    "</div>",
    unsafe_allow_html=True,
)

secao("Comparação entre categorias")
linha_1 = st.columns(3, gap="large")
with linha_1[0]:
    mostrar(grafico_barras())
with linha_1[1]:
    mostrar(grafico_pizza())
with linha_1[2]:
    mostrar(grafico_frequencia())
analise([
    ("Barras", "A região Oeste tem a maior média das vendas médias (225,25) e o Norte a menor (102,54). O maior valor individual é de Livros no Oeste (284,18) e o menor, de Alimentos no Norte (54,15). Entre as categorias, Livros lidera (186,80) e Alimentos fica por último (137,52)."),
    ("Pizza", "O faturamento total é de 120.000. O Site responde por 37,5% e a Loja Física por 26,7%, somando 64,2%. Os canais digitais (Site e Aplicativo) juntos chegam a 55,0%, e o Telefone é o menor canal, com 6,7%."),
    ("Frequência", "Dos 300 chamados, Dúvida é o tipo mais comum (116; 38,7%), seguido de Reclamação (73; 24,3%). Elogio é o menos frequente (29; 9,7%). Bug, Reclamação e Cancelamento somam 155 chamados (51,7%)."),
])

secao("Distribuição e relação entre variáveis")
linha_2 = st.columns(3, gap="large")
with linha_2[0]:
    mostrar(grafico_distribuicao())
with linha_2[1]:
    mostrar(grafico_boxplot())
with linha_2[2]:
    mostrar(grafico_dispersao())
analise([
    ("Distribuição", "As 200 idades vão de 18 a 69 anos, com média de 33,6 e mediana de 29. Como a média fica acima da mediana, a distribuição é assimétrica à direita: 50,5% dos clientes têm entre 18 e 29 anos (idade mais frequente: 24) e só 2 têm 60 anos ou mais."),
    ("Boxplot", "Vendas (mediana de 7.130) e TI (6.614) têm salários típicos bem acima de Marketing (4.191) e RH (4.188). TI tem a maior dispersão (amplitude interquartil de cerca de 2.884). Cada departamento tem 2 outliers: até 21.000 em TI e Vendas e até 12.000 em Marketing e RH."),
    ("Dispersão", "Nas 150 pessoas, altura e peso têm correlação positiva forte (r = 0,85): quanto maior a altura, maior o peso. Os grupos por sexo se sobrepõem, com alturas médias de 169,9 cm (Feminino) e 169,4 cm (Masculino) e pesos médios de 62,4 kg e 63,0 kg, então o sexo não separa os pontos neste conjunto."),
])

secao("Evolução e padrões")
linha_3 = st.columns(3, gap="large")
with linha_3[0]:
    mostrar(grafico_linhas())
with linha_3[1]:
    mostrar(grafico_heatmap())
analise([
    ("Linhas", "As vendas crescem de forma contínua nos 90 dias (1º de janeiro a 31 de março de 2026): a média mensal sobe de 122,26 em janeiro para 172,85 em fevereiro e 225,38 em março, alta de 84,3% entre janeiro e março. O mínimo foi 93,21 (14/01) e o máximo, 260,37 (24/03). Cada dia tem registro de uma única loja (Loja A em 44 dias, Loja B em 46), então as duas linhas se alternam e a comparação direta entre elas é limitada; as médias são 167,83 (Loja A) e 178,96 (Loja B)."),
    ("Heatmap", "O movimento de clientes se concentra no fim de semana: média de 115,1 aos sábados e domingos contra 59,8 nos dias úteis. Os picos são domingo às 12:00 (199) e às 18:00 (197) e sábado às 20:00 (164). Quinta-feira é o dia mais fraco (média de 43,6), com os menores valores às 16:00 (22) e às 14:00 (25). Nos dias úteis, o horário de maior movimento muda de um dia para outro."),
])
