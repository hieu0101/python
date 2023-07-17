a="minh hieu"
b="tran "
#f là f-string bắt buộc để chèn a=f"{...}{....}"
c=f"{b}{a}"
print (c)
c=f"{b.title()}{a.title()}"
print (c)
print("------------------")
#\t lùi vào 1 ô ,\n xuống dòng 
print ("python")
print ("\tpython")
print ("\npython")
print ("\n\tpython")
print("------------------")
#d.rstrip ( loại bỏ khoảng trắng bên phải)
#d.lstrip()( loại bỏ khoảng trắng bên trái)
#d.strip()( loại bỏ khoảng trắng 2 bên )
d=' python '
print (d.rstrip())
print (d.lstrip())
print (d.strip())
print("------------------\n")
first=" do thi "
last=" thanh thao"
full=f"{first.title()}{last.title().strip()} hôm nay cậu khỏe không"
print( full)
full=f'{first.title()}{last.title().strip()} nói :' '" ờ tôi ổn"'
print(full)
full=f'{first.title()}{last.title().strip()} nói :' '" ờ tôi ổn"'.strip()
print(full)
full=f'{first.title()}{last.title().strip()} nói :' '\n" ờ tôi ổn"'
print(full)
