import os
import json
import hashlib

def dict_md5(d):
    # 将 dict 转换为排序的 JSON 字符串，确保顺序一致
    dict_str = json.dumps(d, sort_keys=True)
    # 编码为字节
    dict_bytes = dict_str.encode('utf-8')
    # 计算 MD5
    return hashlib.md5(dict_bytes).hexdigest()

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")


def write_file(file_path:str,data:any):
    # Ensure the directory exists before writing the file
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # Save the data to the JSON file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
