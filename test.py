mydict={"a":1,"b":2}
if 1 in mydict:
    print(1)

dict_test = {'Name': 'Runoob', 'num':{'first_num': '66', 'second_num': '70'}, 'age': '15'}

# print(dict_test.get('first_num')) # None
# print('{:^50}'.format('*'*50)) #: 号后面带填充的字符；^表示居中对齐，{}里面对应后面formate中的值
# print(dict_test.get('num').get('first_num')) # 66

if not dict_test.get("ame"):
    print(1)