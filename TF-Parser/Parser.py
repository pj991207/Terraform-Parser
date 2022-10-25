#Terraform Code Parser

import zipfile
import os
import hcl2

##zip파일 열기
def open_zip(path : str):
    openZip = zipfile.ZipFile(path)
    openZip.extractall('Example_2')
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
def find_tf_module_file(tf_dict:dict):
    tf_dict_key = list(tf_dict.keys())
    module_path = []
    for key in tf_dict_key:
        if 'module' in tf_dict[key].keys():
            module_path.append(key)
    find_tf_moudle(tf_dict,module_path)

#module에서 cidr_block찾는다.
def find_tf_moudle(tf_dict:dict,path:list):
    for i in path:
        module_dict = tf_dict[i]['module'][0]
        module_name = list(module_dict.keys())[0]
        module_dict_value = module_dict[module_name]
        module_source = module_dict_value['source']
        if type(module_source) is list:
            module_source = find_value_in_list(module_source)
        else:
            pass
        module_cidr_block = find_tf_module_cidr_block(module_dict_value,module_source)
        module_private_subnets = find_tf_module_private_subnets(module_dict_value,module_source)
        module_public_subnets = find_tf_module_public_subnets(module_dict_value,module_source)
        print(i,module_cidr_block,module_private_subnets,module_public_subnets)

def find_tf_module_cidr_block(module_dict_value:dict,src:str):
    if "cidr" in module_dict_value.keys():
        cidr_block = module_dict_value['cidr']
        if type(cidr_block) is list:
            cidr_block = find_value_in_list(cidr_block)
    else:
        pass
    return cidr_block

def find_tf_module_private_subnets(module_dict_value:dict,src:str):
    if "private_subnets" in module_dict_value.keys():
        private_subnets = module_dict_value['private_subnets']
        if type(private_subnets) is list:
            private_subnets = find_value_in_list(private_subnets)
    else:
        pass
    return private_subnets

def find_tf_module_public_subnets(module_dict_value:dict,src:str):
    if "public_subnets" in module_dict_value.keys():
        public_subnets = module_dict_value['public_subnets']
        if type(public_subnets) is list:
            public_subnets = find_value_in_list(public_subnets)
    else:
        pass
    return public_subnets

def find_value_in_list(value:list):
    while True:
        if type(value) == list:
            value = value[0]
        else:
            return value

if __name__ =="__main__":
    name = "Example_2.zip"
    open_zip(name)
    open_tf_file('Example_2')
