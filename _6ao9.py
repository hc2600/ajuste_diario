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


# Pesquisar também dentro de formulas
pyautogui.click(2820,768,duration=1)
time.sleep(2)


# Pesquisar: 
pyautogui.click(2923,578,duration=1)


# Intervalo específico
pyautogui.click(2923,659,duration=1)



# Entrar com intervalo
# de 6º ao 9º alterna entre disciplinas
""" 
Ciências!OG6:OG77
Matemática!OF6:OF77
História!OF6:OF77
Geografia!OF6:OF77
Arte!OF6:OF77
Ed. Física!OF6:OF77
Português!OF6:OF77
Inglês!OF6:OF77
Espanhol!OF6:OF77
 """
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')


#Ciências!OG6:OG77
pyperclip.copy('Ciências!OG6:OG77')
pyautogui.hotkey('ctrl', 'v') 



# Substituir tudo
pyautogui.click(3083,894,duration=2)
time.sleep(2)


#Matemática!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
 
pyperclip.copy('Matemática!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 


# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(2)

#História!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
 
pyperclip.copy('História!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 


# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(2)

#Geografia!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
 
pyperclip.copy('Geografia!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 


# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(2)


#Arte!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')

pyperclip.copy('Arte!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 


# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(4)


#Ed. Física!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
 
pyperclip.copy('Ed. Física!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 

# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(2)

#Português!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
 
pyperclip.copy('Português!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 


# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(2)


#Inglês!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')

pyperclip.copy('Inglês!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 

# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(2)


#Espanhol!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
 
pyperclip.copy('Espanhol!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 

# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(2)

#Mandarim!OF6:OF77
pyautogui.click(3046,583,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')

pyperclip.copy('Mandarim!OF6:OF77')
pyautogui.hotkey('ctrl', 'v') 

# Substituir tudo
pyautogui.click(3083,894,duration=1)
time.sleep(1)
# Concluido
pyautogui.click(3225,901,duration=1)