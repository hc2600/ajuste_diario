#########
#  Rodar o mouseInfo para pegar as posições
#  no CMD: python
#  from mouseinfo import mouseInfo
#  mouseInfo
#  Tirar o 3 sec delay
#  apontar para o intem e tocar F6 com a janela mouseInfo na frente

import pyautogui
import pyperclip
import time


# Tocar na planilha
pyautogui.click(2739,411,duration=1)

# Abrir pagina de pesquisa CTRL + H
pyautogui.hotkey('ctrl','h')
time.sleep(2)
# Localizar /200 
pyautogui.click(2914,469,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
pyautogui.write("/200")


# Substituir por  /213
pyautogui.click(2914,526,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
pyautogui.write("/213")

# Pesquisar: 
pyautogui.click(2923,578,duration=1)
time.sleep(1)

# Intervalo específico
pyautogui.click(2923,659,duration=1)
time.sleep(1)

# Entrar com intervalo
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
# Descomentar se até 3º ou especial 
# pyperclip.copy('Diário!LJ6:LJ77')

# Descomentar se 4º ou 5º ano
pyperclip.copy('Diário!MX6:MX77')

pyautogui.hotkey('ctrl', 'v') 
time.sleep(1)

# Pesquisar também dentro de formulas
pyautogui.click(2820,768,duration=1)
time.sleep(2)

# Substituir tudo
pyautogui.click(3083,894,duration=2)
time.sleep(1)
# Concluido
pyautogui.click(3225,901,duration=1)





