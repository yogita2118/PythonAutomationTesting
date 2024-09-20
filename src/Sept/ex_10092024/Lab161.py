import os

full_path_file = os.path.join("/Users/Yogi/PycharmProjects/PythonAutomationTesting/src/Sept/ex_10092024/Yogi", "yogi.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)