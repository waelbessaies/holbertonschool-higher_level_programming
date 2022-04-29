#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for hiddenlist in dir(hidden_4):
        if hiddenlist[0] != "_":
            print(hiddenlist)
