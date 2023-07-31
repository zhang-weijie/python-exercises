import easygui as g
import os

file_path=g.fileopenbox(default='*.txt')
title=os.path.basename(file_path)
msg='请查看【%s】文件内容'%title
with open(file_path) as f:
    text=f.read()
text_after=g.textbox(msg,title,text)

if text!=text_after[:-1]:
    choice=g.choicebox('检测到文件内容发生改变，请选择执行以下操作：','警告',['覆盖保存','放弃保存','另存为...'])
    if choice=='覆盖保存':
        with open(file_path,'w') as f:
            f.write(text_after[:-1])
    if choice=='放弃保存' or choice==None:
        pass
    if choice=='另存为...':
        file_path=g.filesavebox(default='record(2).txt')
        with open(file_path,'w') as f:
            f.write(text_after[:-1])
g.msgbox('操作完成！')
    
