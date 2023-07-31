print('red\tyellow\tgreen\twhite\t')
for red in range(0,3):
    for yellow in range(0,6):
        for green in range(0,8):
            for white in range(1,9):
                if red+yellow+green==10:
                    print(red,'\t',yellow,'\t',green,'\t',white,'\t')
                
