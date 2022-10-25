#Terraform Code Parser

import zipfile
import os
import hcl2

##zip파일 열기
def open_zip(path : str):
    openZip = zipfile.ZipFile(path)
    openZip.extractall()
    openZip.close()

##.tf 파일 확장자를 갖는 파일의 경로를 찾음
def open_tf_file(path : str):
    file_path = []
    tf_dict = {}
    for (root, directories, files) in os.walk(path):
        for file in files:
            if '.tf' in file:
                file_path.append(os.path.join(root,file))
    ##.tf 파일을 열고 이 내용을 file_path : file 형태로 dictonary로 저장함.
    for path in file_path:
        with open(path,'r',encoding='UTF-8') as file:
            tf_dict[path]=hcl2.load(file)

    find_tf_module_file(tf_dict)

##.tf 파일에서 module을 사용하는 tf 파일을 찾는다.
def find_tf_module_file(tf_dict):
    tf_dict_key = list(tf_dict.keys())
    module_path = []
    for key in tf_dict_key:
        if 'module' in tf_dict[key].keys():
            #find source
            module_path.append(key)
            #print("path : ",key)
            #print("value : ",tf_dict[key]['module'])
    find_tf_moudle_cidr_block(module_path)

def find_tf_moudle_cidr_block(path):



if __name__ =="__main__":
    name = "Example_1.zip"
    open_zip(name)
    list_tf_file('Example_1')

