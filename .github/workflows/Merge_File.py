import os
import shutil

file_paths = ["Direct_Rule", "Proxy_Rule", "Reject_Rule"]


def merge_and_deduplicate_files(path):
    output_file_path = f"{os.path.basename(path)}.rule"
    with open(output_file_path, 'w', encoding='utf8') as out_f:
        data_set = set()
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf8') as in_f:
                    lines = [line.strip() for line in in_f.readlines() if not line.startswith("#")]
                    data_set.update(lines)
        data_list = sorted(data_set)
        out_f.writelines(line + '\n' for line in data_list if line.strip())
    return output_file_path


if __name__ == '__main__':
    os.chdir("./rule")
    for path in file_paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"创建目录 {path} 成功")
        output_file_path = merge_and_deduplicate_files(path)
        shutil.rmtree(path)
        print(f"删除 {path} 文件夹")
        print(f"{os.path.basename(output_file_path)} 文件创建成功")
