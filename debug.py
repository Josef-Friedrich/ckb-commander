import time

with open("/dev/input/ckb1/cmd", "w") as file:
    file.write("get :rgb\n")

with open("/dev/input/ckb1/notify0") as file:
    line = file.readline()

    print(line)
