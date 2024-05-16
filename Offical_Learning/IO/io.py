import os
import shutil
import glob

'''
# input 输入
str1 = input("请输入内容")
print("你输入的内容为：", str1)
'''

'''
# 文件的打开与关闭
obj = open("test.txt", "r")
print(obj.name)
print(obj.closed)
print(obj.mode)
obj.close()
print(obj.closed)
'''

'''
# 文件写入及异常的判断
obj = open("test.txt", "r+")
print(obj.name)
for i in range(10):
    try:
        obj.write(str(i))
    except IOError:
        print("IOError")
    finally:
        continue
print("write finish")
obj.close()
'''

'''
# 读取文件内容
obj = open("test.txt", "r+")
print(obj.name)
content = obj.read()
print(content)
obj.close()
'''

'''
# 文件定位
file = open("test.txt", "r+")
str = file.read()
print("读取到的内容为",str)

# 查找当前位置
position = file.tell()
print("当前读取到的位置为",position)

# 把指针调回到文件开头
position = file.seek(0, 0)
str2 = file.read()
print("在此读取到的内容为", str)
file.close()
'''

'''
# 文件重命名
file = open("test_rename.txt", "r+")
if file.name == "test_rename.txt":
    os.rename("test_rename.txt", "test.txt")
else:
    print("文件的名字已经是 test.txt")
file.close()
'''

'''
# 文件的删除
file = open("test_remove.txt", "r+")
if file.name == "test_remove.txt":
    os.remove("test_remove.txt")
else:
    print("我只能删除 test_remove.txt")
file.close()
'''

# 创建目录 os.mkdir()
# 改变目录 os.chdir()
# 获取当前目录 os.getcwd()
# 删除目录 os.rmdir()

'''
创建目录结构：在当前工作目录下创建一个新的目录data_analysis。
文件复制：将当前目录下的所有.txt和.csv文件复制到新创建的data_analysis目录中。
文件重命名：在data_analysis目录中，将所有文件的扩展名从.txt改为.data。
删除文件：删除data_analysis目录中所有大小小于10KB的文件。
目录遍历：打印出data_analysis目录及其所有子目录中的所有文件的完整路径。
文件写入：在data_analysis目录中创建一个名为summary.txt的文件，并向其中写入文本“Data analysis completed successfully!”。
错误处理：确保你的脚本能够处理任何可能发生的错误，如文件不存在、权限问题等。
'''

# 定义当前工作目录
current_dir = os.getcwd()

# 创建目录结构
data_analysis_dir = os.path.join(current_dir, 'data_analysis')
try:
    os.makedirs(data_analysis_dir, exist_ok=True)
except OSError as e:
    print(f"Error creating directory: {e}")
    exit()

# 文件复制
txt_files = glob.glob(os.path.join(current_dir, '*.txt'))
csv_files = glob.glob(os.path.join(current_dir, '*.csv'))
for file_path in txt_files + csv_files:
    try:
        shutil.copy(file_path, data_analysis_dir)
    except IOError as e:
        print(f"Error copying file {file_path}: {e}")

# 文件重命名
for file_path in glob.glob(os.path.join(data_analysis_dir, '*.txt')):
    try:
        new_file_path = os.path.splitext(file_path)[0] + '.data'
        os.rename(file_path, new_file_path)
    except OSError as e:
        print(f"Error renaming file {file_path}: {e}")

# 删除文件
for file_path in glob.glob(os.path.join(data_analysis_dir, '**', '*.data'), recursive=True):
    try:
        if os.path.getsize(file_path) < 10 * 1024:  # 10KB
            os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file {file_path}: {e}")

# 目录遍历
for root, dirs, files in os.walk(data_analysis_dir):
    for file in files:
        print(os.path.join(root, file))

# 文件写入
summary_file_path = os.path.join(data_analysis_dir, 'summary.txt')
try:
    with open(summary_file_path, 'w') as file:
        file.write("Data analysis completed successfully!")
except IOError as e:
    print(f"Error writing to file {summary_file_path}: {e}")