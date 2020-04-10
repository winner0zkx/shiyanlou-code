for i in range(1,101):
    if i % 7 == 0:
        pass
    elif int(i / 10) % 7 == 0 and int(i / 10) != 0:
        pass
    elif (i % 10) % 7 == 0 and (i % 10) != 0:
        pass
    elif (i % 100) % 7 == 0 and (i % 100) != 0:
        pass
    else:
        print(i)

