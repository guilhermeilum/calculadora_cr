# Carregar o PDF e extrair o texto
from re import findall, search
from PyPDF2 import PdfReader
from glob import glob


class ErroPersonalizado(Exception):
    pass


def carregar_pdf(caminho_arquivo):
    with open(caminho_arquivo, "rb") as file:
        reader = PdfReader(file)
        texto = ""
        for pagina in reader.pages:
            texto += pagina.extract_text()
        return texto


# Caminho do PDF
caminho_pdf = glob("*.pdf")
if len(caminho_pdf) < 1:
    raise ErroPersonalizado("Não tem nenhum arquivo .pdf na pasta!")
if len(caminho_pdf) > 1:
    raise ErroPersonalizado("Só pode ter um arquivo .pdf na pasta!")
texto_pdf = carregar_pdf(caminho_pdf[0])


# Expressão regular para capturar o padrão
padrao = r"\d+\s\d+\s[A-D]"

resultados = findall(padrao, texto_pdf)
resultados = [search(r"[A-D]", resultado)[0] for resultado in resultados]

tamanho = len(resultados)

# Disciplinas com conceito e carga horária teórica e prática
courses = [
    {"name": "Álgebra Linear", "grade": "Nota", "CH": 30},
    {"name": "Ciência Moderna", "grade": "Nota", "CH": 30},
    {"name": "Dinâmica", "grade": "Nota", "CH": 30},
    {"name": "Energia em Sistemas Vivos I", "grade": "Nota", "CH": 30},
    {"name": "Forma, Função e Informação", "grade": "Nota", "CH": 30},
    {"name": "Fundamentos da Matéria", "grade": "Nota", "CH": 30},
    {"name": "Funções de Variáveis Reais", "grade": "Nota", "CH": 30},
    {"name": "Imersão no CNPEM", "grade": "Nota", "CH": 60},
    {"name": "Integrais de Várias Variáveis", "grade": "Nota", "CH": 30},
    {"name": "Lógica Computacional", "grade": "Nota", "CH": 30},
    {"name": "Laboratório de Humanidades I", "grade": "Nota", "CH": 30},
    {"name": "Práticas Básicas de Laboratório", "grade": "Nota", "CH": 120},
    {"name": "Práticas em Ciências de Dados", "grade": "Nota", "CH": 60},
    {"name": "Termodinâmica", "grade": "Nota", "CH": 30},
    {"name": "Álgebra Linear Computacional", "grade": "Nota", "CH": 30},
    {"name": "Aprendizado de Máquina", "grade": "Nota", "CH": 60},
    {"name": "Ciência na Segunda Modernidade", "grade": "Nota", "CH": 30},
    {"name": "Equações Diferenciais", "grade": "Nota", "CH": 30},
    {"name": "Estrutura e Função de Proteínas", "grade": "Nota", "CH": 30},
    {"name": "Eletromagnetismo", "grade": "Nota", "CH": 30},
    {"name": "Fundamentos da Quântica", "grade": "Nota", "CH": 30},
    {"name": "Integração Curricular da Extensão I", "grade": "Nota", "CH": 125},
    {"name": "Iniciação à Pesquisa I (CNPEM)", "grade": "Nota", "CH": 120},
    {"name": "Laboratório Avançado I", "grade": "Nota", "CH": 60},
    {"name": "Laboratório de Humanidades II", "grade": "Nota", "CH": 30},
    {"name": "Orgânica", "grade": "Nota", "CH": 30},
    {"name": "Probabilidade e Estatística", "grade": "Nota", "CH": 30},
    {"name": "Tempo em Sistemas Vivos I", "grade": "Nota", "CH": 30},
    {"name": "Antinomia Cultura-Natureza", "grade": "Nota", "CH": 30},
    {"name": "Análise Numérica", "grade": "Nota", "CH": 30},
    {"name": "Dinâmica Avançada", "grade": "Nota", "CH": 30},
    {"name": "Decodificação da Informação Genética", "grade": "Nota", "CH": 30},
    {"name": "Integração Curricular da Extensão II", "grade": "Nota", "CH": 50},
    {"name": "Iniciação à Pesquisa II (CNPEM)", "grade": "Nota", "CH": 120},
    {"name": "Laboratório Avançado II", "grade": "Nota", "CH": 60},
    {"name": "Laboratório de Humanidades III", "grade": "Nota", "CH": 30},
    {"name": "Modelagem de Empreendimentos Inovadores", "grade": "Nota", "CH": 30},
    {"name": "Redes Neurais e Algoritmos Genéticos", "grade": "Nota", "CH": 60},
    {"name": "Séries e Transformadas", "grade": "Nota", "CH": 30},
    {"name": "Termodinâmica Avançada", "grade": "Nota", "CH": 30},
    {"name": "Teoria Quântica", "grade": "Nota", "CH": 30},
    {"name": "Tempo em Sistemas Vivos II", "grade": "Nota", "CH": 30},
    {"name": "Átomos, Moléculas e Eletrônica Molecular", "grade": "Nota", "CH": 30},
    {"name": "Biomatemática", "grade": "Nota", "CH": 30},
    {"name": "Ciências Ambientais", "grade": "Nota", "CH": 30},
    {"name": "Célula e Suas Interações I", "grade": "Nota", "CH": 30},
    {"name": "Cinética Química", "grade": "Nota", "CH": 30},
    {"name": "Fundamentos Estatísticos da Termodinâmica", "grade": "Nota", "CH": 30},
    {"name": "A Grande Aceleração no Antropoceno", "grade": "Nota", "CH": 30},
    {"name": "Integração Curricular da Extensão III", "grade": "Nota", "CH": 125},
    {"name": "Iniciação à Pesquisa III (CNPEM)", "grade": "Nota", "CH": 120},
    {"name": "Laboratório Avançado III", "grade": "Nota", "CH": 60},
    {"name": "Laboratório de Humanidades IV", "grade": "Nota", "CH": 30},
    {"name": "Matéria Condensada I", "grade": "Nota", "CH": 30},
    {"name": "Otimização", "grade": "Nota", "CH": 30},
    {"name": "Simulação Atomística", "grade": "Nota", "CH": 60},
    {"name": "A Célula e Suas Interações II", "grade": "Nota", "CH": 30},
    {"name": "Cultura Digital", "grade": "Nota", "CH": 30},
    {"name": "Espaços Normados", "grade": "Nota", "CH": 30},
    {"name": "Energia em Sistemas Vivos II", "grade": "Nota", "CH": 30},
    {"name": "Integração Curricular da Extensão IV", "grade": "Nota", "CH": 50},
    {"name": "Iniciação à Pesquisa IV (CNPEM)", "grade": "Nota", "CH": 180},
    {"name": "Laboratório Avançado IV", "grade": "Nota", "CH": 60},
    {"name": "Matéria Condensada II", "grade": "Nota", "CH": 30},
    {"name": "Matéria Condensada Mole", "grade": "Nota", "CH": 30},
    {"name": "Práticas Computacionais Avançadas", "grade": "Nota", "CH": 60},
    {"name": "Iniciação à Pesquisa V (CNPEM)", "grade": "Nota", "CH": 300},
    {"name": "Tópicos Avançados em Ciências", "grade": "Nota", "CH": 30},
]

courses = courses[:tamanho]

for dicionario, nota in zip(courses, resultados):
    dicionario["grade"] = nota

# Definição das notas em termos numéricos
grades = {"A": 10, "B": 8.995, "C": 6.995}

# Cálculo do CR
total_weighted_grade = sum(grades[course["grade"]] * course["CH"] for course in courses)
total_ch = sum(course["CH"] for course in courses)

cr = total_weighted_grade / total_ch
print("Os dados usados foram:")
print(courses)
print("O CR é:", cr)
input("Presione enter para fechar...")
