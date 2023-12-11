import os
import configparser
import re


# 判断文件或文件夹是否需要忽略
def ignore_file_or_folder(item_name, is_file):
    # 判断对应文件是否需要过滤
    if is_file:
        for pattern in folders_to_ignore_files:
            if re.match(pattern, item_name) or item_name == pattern:
                return True
    else:
        for pattern in folders_to_ignore_folders:
            if re.match(pattern, item_name) or item_name == pattern:
                return True
    return False  # 当所有模式都检查完后才返回 False


# root_folder:项目根路径
# folder_path:当前文件夹路径
# 转化结果存储位置
def handle_files(root_folder, folder_path, markdown_list):
    # 获取当前目录下的所有文件和文件夹
    contents = os.listdir(folder_path)
    files = []
    folders = []
    # 处理当前目录下的文件和文件夹
    for item in contents:
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):  # 是文件
            result = ignore_file_or_folder(item, True)
            if result:
                continue
            files.append(item_path)
        elif os.path.isdir(item_path):  # 文件夹
            if ignore_file_or_folder(item, False):
                continue
            folders.append(item_path)

    # 先处理文件
    for file_path in files:
        # 将完整路径转换为相对路径
        relative_path = os.path.relpath(file_path, root_folder)
        file_name = os.path.basename(file_path)
        # 缩进值=相对路径中的/的个数
        indentation = ' ' * (relative_path.count(os.sep) * 3)
        item = f"{indentation}- [{os.path.splitext(file_name.replace(' ', ''))[0]}]({relative_path.replace(os.sep, '/')})"
        markdown_list.append(item)

    # 再处理文件夹
    for folder_path in folders:
        # 将完整路径转换为相对路径
        relative_path = os.path.relpath(folder_path, root_folder)
        folder_name = os.path.basename(folder_path)
        # 缩进值=相对路径中的/的个数
        indentation = ' ' * (relative_path.count(os.sep) * 3)
        item = f"{indentation}- {os.path.splitext(folder_name.replace(' ', '%20'))[0]}"
        markdown_list.append(item)
        handle_files(root_folder, folder_path, markdown_list)

    # 去除文件中的空格，并修改对应的文件名
    # directory, filename = os.path.split(relative_path) # 获取文件目录以及文件名
    # new_filename = filename.replace(' ', '') # 移除文件名中的空格，并修改对应文件名字
    # new_file_path = os.path.join(directory, new_filename)
    # os.rename(relative_path, new_file_path)


def generate_markdown_list(root_folder, folders_to_convert):
    markdown_list = []
    for folder_name in folders_to_convert:
        folder_path = os.path.join(root_folder, folder_name)
        if not os.path.exists(folder_path):
            print(f"文件夹或文件： '{folder_name}' 不存在")
            continue
        # 处理文件
        handle_files(root_folder, folder_path, markdown_list)

    return '\n'.join(markdown_list)


# 读取配置文件
current_directory = os.getcwd()  # 获取当前工作目录
config_file_path = os.path.join(current_directory, 'config.ini')  # 构建相对于当前目录的配置文件路径
config = configparser.ConfigParser()
config.read(config_file_path)
# 获取配置信息
root_folder_path = config.get('Settings', 'root_folder_path')  # 根目录
folders_to_convert = config.get('Settings', 'folders_to_convert').split(',')  # 根目录中需要转为markdown的文件夹，即笔记所存储的位置
output_file_path = config.get('Settings', 'output_file_path')  # 获取输出文件路径
folders_to_ignore_folders = config.get('Settings', 'folders_to_ignore_folders').split(',')  # 获取需要忽略的文件夹列表
folders_to_ignore_files = config.get('Settings', 'folders_to_ignore_files').split(',')  # 获取需要忽略的文件列表

# 生成Markdown列表
markdown_list_output = generate_markdown_list(root_folder_path, folders_to_convert)

# 将Markdown列表写入文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(markdown_list_output)

print(f"Markdown列表已写入文件：{output_file_path}")
