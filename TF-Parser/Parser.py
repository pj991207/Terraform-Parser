#Terraform Code Parser

import zipfile
import os
import hcl2
import glob

##zip파일 열기
def open_zip(path : str) -> None:
    zip = zipfile.ZipFile(path)
    zip.extractall('Example_2')
    zip.close()

##.tf 파일 확장자를 갖는 파일의 경로를 찾음
def open_tf_file(path : str) -> None:
    file_path = glob.glob(path+'\**\*.tf',recursive=True)
    ##.tf 파일을 열고 이 내용을 file_path : file 형태로 dictonary로 저장함.
    for path in file_path:
        with open(path,'r', encoding='UTF-8') as file:
            value = hcl2.load(file)
            if "module" in value: find_tf_module({'key':path,'value':value})

#module에서 cidr_block찾는다.
def find_tf_module(tf_dict: dict):
    temp = ['cidr', 'private_subnets', 'public_subnets']
    if isinstance(tf_dict, dict):
        for module in tf_dict['value']['module'][0]:
            module_dict_value = tf_dict['value']['module'][0][module]
            module_source = module_dict_value['source']
            for key in temp:
                print(f'{key} is {module_dict_value[key][0]}')

if __name__ == "__main__":
    name = "Example_2.zip"
    open_zip(name)
    open_tf_file('Example_2')
