**getSidebar.exe：**

​	读取config.ini文件，将该文件中指定的笔记文件转化为Docsify可以识别的markdown的list。

**config.ini：**

​	配置需要读取的文件信息。其中：

~~~
root_folder_path：表示该项目的根路径
folders_to_convert：表示根路径下哪些文件夹为笔记文件夹，需要被读取转换。多个文件夹使用','分割
output_file_path：表示笔记文件目录信息生成后存储的位置。
folders_to_ignore_folders：表示需要被忽略的文件夹（可以使用正则表达式）
folders_to_ignore_files：表示需要被忽略的文件（可以使用正则表达式）
~~~

