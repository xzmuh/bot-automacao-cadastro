# Sistema teste utilizado
# 1. Acessar
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 2. Fazer login
# 3. Importar base
# 4. Cadastrar
# 5. Repetir
import pyautogui
import time
pyautogui.PAUSE = 0.3

# Inicio
    # Abrir o navegador
pyautogui.press('win')
time.sleep(1)
pyautogui.write("chorme")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)

# Ir para a pagina de login
    # Digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.click(x=1063, y=68)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)

# Fazer Login
pyautogui.click(x=504, y=411)
usuario="xzmuh.courses@hotlnk.com"
senha="123456"
pyautogui.write(usuario)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1.5)

# Ler base de dados
import pandas

baseDeDados = pandas.read_csv("produtos.csv")

# Cadastrar produtos
for linha in baseDeDados.index:

    pyautogui.click(x=538, y=291)

    codigo = baseDeDados.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(baseDeDados.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(baseDeDados.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(baseDeDados.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(baseDeDados.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    pyautogui.scroll(-400)

    custo = str(baseDeDados.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = baseDeDados.loc[linha, "obs"]

    if not pandas.isna(obs):
        pyautogui.write(obs)
    else:
        pyautogui.write(" ")

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(600)

pyautogui.scroll(-850)