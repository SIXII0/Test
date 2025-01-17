names = ['Bob','Tom','alice','Jerry','Wendy','Smith']   #名字列表
new_names = [name.upper()for name in names if len(name)>3]  #名字长度大于3的进行大写操作
print(new_names)