import os

def get_FileSize(filePath): # 获取文件的大小,结果保留两位小数，单位为MB
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

def file_extension(filepath): # 获得文件扩展名
    return os.path.splitext(filepath)[1]  


# 判断文件是否符合上传的要求，大小必须小于10M，并且后缀名有要求
# REQUIRES: the file path is a str and it exists
# MODIFIES: None
# EFFECTS: return str information which represents the file is valid or not
#          If success, return "success"
def file_valid(filepath):
    if (not (os.path.exists(filepath))):
        return "The File does not exist"
    file_size = get_FileSize(filepath)
    file_suffix_name = file_extension(filepath)
    suffix_allowed = ['.pdf','.doc','.docx','.ppt','.pptx','.txt']
    if (file_size > 10):
        return "Please upload files smaller than 10MB"
    if (not(file_suffix_name.lower() in suffix_allowed)):
        return "Don't allow file with " + file_suffix_name
    return "Success"

print(file_valid("/Users/Mr.ZY/Downloads/solution.pdf"))
