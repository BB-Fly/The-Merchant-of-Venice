import re

# with open ("data/merchant/merchant.1.1.html") as handler
#     text = handler.read()
# print(text)

# with open
# def get_list_scene("data/Merchant of Venice_ List of Scenes.html"):
import re


def str_find(s:str,target:str,idx:int)->int:
    i = idx;
    while(i<len(s)):
        j=0
        while(j<len(target) and j+i<len(s)):
            if s[i+j]==target[j]:
                j += 1
            else:
                break
        if j<len(target):
            i+=1
        else:
            return i
    
    return -1

def get_list_scene(file_path):
    with open(file_path) as handler:
        text = handler.read()

    pattern = r'<a href="(.+)">'
    alist = re.findall(pattern, text)
    for i in range(len(alist)):
        alist[i]  = 'data/' + alist[i]
    return alist


def get_scene_script(file_path,act_list:list):
    state = 0
    res:str = ''
    idx = 0
    with open(file_path) as handler:
        text = handler.read()
    
    # ACT
    idx = str_find(text,'Act',idx)
    str_tmp = ''
    while(text[idx]!=','):
        str_tmp += text[idx]
        idx+=1
    if str_tmp not in act_list:
        res += ('\n## '+str_tmp+'\n')
        act_list.append(str_tmp)

    # Scene
    idx = str_find(text,'SCENE',idx)
    str_tmp = ''
    while(text[idx]!='<'):
        str_tmp += text[idx]
        idx += 1
    res += ('\n### '+str_tmp+'\n')

    idx_h = str_find(text, '<i>', idx) # hint
    idx_n = str_find(text, '<A NAME=', idx) # name and line

    while(True):

        if idx_h!=-1 and (idx_n==-1  or idx_h<idx_n):
            # Hint
            idx = idx_h + 3
            str_tmp = ''
            while(text[idx]!='<'):
                str_tmp += text[idx]
                idx += 1
            res += ('\n*'+str_tmp+'*\n')
            idx_h = str_find(text, '<i>', idx)
            state = 1

        elif idx_n!=-1:
            # name or line
            idx = idx_n + 8

            if text[idx] =='s':
                # name
                idx = str_find(text, '<b>', idx)
                idx += 3
                str_tmp = ''
                while(text[idx]!='<' and text[idx]!=' '):
                    str_tmp += text[idx]
                    idx += 1
                res += ('\n**'+str_tmp+'**\n')
                state = 1

            else:
                # line
                idx = str_find(text, '>', idx)
                idx += 1
                str_tmp = ''
                while (text[idx]==' ' or text[idx]=='\t'):
                    idx += 1
                while(text[idx]!='<'):
                    str_tmp += text[idx]
                    idx += 1
                if state==1:
                    res += '\n'
                res += (str_tmp + '  \n')
                state=0
            idx_n = str_find(text, '<A NAME=', idx)
        else:
            # break loop
            break


    return res


def write_script(file_name:str, content:str):
    with open(file_name,'a') as fp:
        fp.write(content)
    return


def get_scene_tag_dict(file_path):

    tag_dict = {}
    idx = 0
    res:str


    with open(file_path) as f:
        text = f.read()
    
    while(idx!=-1 and idx<len(text)):
        res = ''
        idx = str_find(text,'<',idx)
        if idx==-1:
            break
        idx+=1
        if text[idx]=='/' or text[idx]=='!':
            continue
        else:
            while(text[idx]!=' ' and text[idx]!='>'):
                if(ord(text[idx])>=ord('A') and ord(text[idx])<=ord('Z')):
                    res += chr(ord(text[idx])+ord('a')-ord('A'))
                else:
                    res += text[idx]
                idx += 1
            if res!='':
                if tag_dict.get(res):
                    tag_dict[res] = tag_dict[res]+1
                else:
                    tag_dict[res] = 1

    return tag_dict


def get_TAG(file_path="data/Merchant of Venice_ List of Scenes.html",targetpath="document/venice.tag"):

    alist = get_list_scene(file_path)
    res_dict = get_scene_tag_dict(file_path)

    for scene in alist:
        tag_dict = get_scene_tag_dict(scene)
        for key, val in tag_dict.items():
            if res_dict.get(key):
                res_dict[key] = res_dict[key] + val
            else:
                res_dict[key] = val
    
    with open(targetpath,'a+') as fp:
        for key_val in sorted(res_dict.items(),key=lambda x:-x[1]):
            s = ' '*(16-len(key_val[0]))
            fp.write("{}{}{}\n".format(key_val[0],s,key_val[1]))
        
    return

def get_MD(file_path="data/Merchant of Venice_ List of Scenes.html",targetpath="document/venice.MD"):

    with open(file_path) as fp:
        text = fp.read()
        idx = 0
        idx = str_find(text,'<title>',idx)
        str_tmp = ''
        idx += 7
        while(text[idx]!='\n' and text[idx]!='<' and text[idx]!=':'):
            str_tmp += text[idx]
            idx += 1
        res = "# "+str_tmp+"\n"
        write_script(targetpath,res)

    alist = get_list_scene(file_path)
    actList = []
    for scene in alist:
        res = get_scene_script(scene,actList)
        write_script(targetpath,res)
    return



def main():
    get_MD()
    get_TAG()

if __name__ =='__main__':
    main()