# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2018-04-11
# 说明：删除文件名中含有“.”的名称为“_”

# 文件夹套文件夹的形式，此为根目录
rootdir = r"D:\01-Working\2018\20180411-HAD_FREQ\2017shp"
# 获取子文件夹
folders = os.listdir(rootdir)
    
# 遍历子文件夹里面的文件重命名
for folder in folders:
    fs = os.listdir(os.path.join(rootdir, folder))
    for f in fs:
        file_ext = os.path.splitext(f)
        # 纯文件名
        f_name = file_ext[0]
        # 扩展名，前面带点
        f_ext = file_ext[1]
        # 如果文件名中存在点，则将其替换为下划线重命名
        if f_name.find(".") > 0:
            path_new = f_name.replace(".", "_") + f_ext
            os.rename(os.path.join(rootdir, folder, f), os.path.join(rootdir, folder, path_new))

