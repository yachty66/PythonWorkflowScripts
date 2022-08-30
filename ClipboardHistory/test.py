p = 1

def on():
    
    global p
    p += 1
    
if __name__ == "__main__":
    for i in range (3):
        on()
        print(p)