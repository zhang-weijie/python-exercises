import pickle
def save_file(boy_line,girl_line,count):
    boy_file_name='小甲鱼'+str(count)+'.pkl'
    girl_file_name='小客服'+str(count)+'.pkl'
    boy_file=open('D:\\'+boy_file_name,'wb')
    girl_file=open('D:\\'+girl_file_name,'wb')
    pickle.dump(boy_line,boy_file)
    pickle.dump(girl_line,girl_file)
    boy_file.close()
    girl_file.close()

def split_file():
    start_file=open('D:\\record.txt')
    boy_line=[]
    girl_line=[]
    count=1
    for each_line in start_file:
        if each_line[0:1]!='=':
            (role,line_spoken)=each_line.split(':',1)
            if role=='小甲鱼':
                boy_line.append(line_spoken)
            if role=='小客服':
                girl_line.append(line_spoken)
        else:
            save_file(boy_line,girl_line,count)
            boy_line=[]
            girl_line=[]
            count+=1
    
    save_file(boy_line,girl_line,count)
    start_file.close()


      
