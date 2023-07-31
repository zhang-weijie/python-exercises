import os
import easygui as g


extensions=['.py','.c','.cpp','.pas','.asm','.h']
ext_file_dict=dict((('.py',0),('.c',0),('.cpp',0),('.pas',0),('.asm',0),('.h',0)))
ext_line_dict=dict((('.py',0),('.c',0),('.cpp',0),('.pas',0),('.asm',0),('.h',0)))
def search_file(start_path):
    os.chdir(start_path)
    file_list=os.listdir(os.curdir)
    for each_file in file_list:
        if os.path.isfile(each_file):
            each_line_ext=os.path.splitext(each_file)[1]
            if each_line_ext in extensions:
                ext_file_dict[each_line_ext]+=1
                try:
                    with open(os.getcwd()+os.sep+each_file) as f:
                        f.seek(0)
                        lines_list=f.readlines()
                        ext_line_dict[each_line_ext]+=len(lines_list)
                except UnicodeDecodeError:
                    pass
        else:
            start_path=os.getcwd()+os.sep+each_file
            search_file(start_path)
            os.chdir(os.pardir)

start_path=g.diropenbox()
search_file(start_path)
text=[]
for each in ext_file_dict:
    file_num=ext_file_dict[each]
    line_num=ext_line_dict[each]
    text.append('【%s】源文件%d个，源代码%d行\n'%(each,int(file_num),int(line_num)))

save_path=g.diropenbox()
with open(save_path+'result.txt','w') as f:
    f.writelines(text)

line_sum=0
for each in ext_line_dict:
    line_sum+=int(ext_line_dict[each])
progress_rate=line_sum/100000
linesleft_sum=100000-line_sum
msg='您目前累计编写了%d行代码，完成度%f\n离10万行代码还差%d行，请继续努力~'%(line_sum,progress_rate,linesleft_sum)
title='统计结果'
with open(save_path+'result.txt') as file:
    result=file.read()
g.textbox(msg=msg,title=title,text=result)
    
                    
                    
                    
