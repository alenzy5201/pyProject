import pandas as pd

# # 读取Excel文件，指定工作表名称或索引，并跳过表头行
# excel_file_path = './files.xlsx'
# sheet_name = 'Sheet1'  # 或者使用 sheet_name=3，根据索引选择第四个工作表
# df = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=None)
#
# # print(df.columns)
# print(df[0][0])
#
#
# # 假设姓名所在列为 '姓名'，身份证号码所在列为 '身份证号码'
# name_column = '姓名'
# id_column = '身份证号码'
#
# # 输入要查找的姓名
# target_name = '周豪'
#
# # 使用 loc 方法定位行数据
# target_row = df.loc[df[2] == target_name]  # 0 是默认的列索引，根据实际情况调整
#
# # 获取身份证号码列的数据
# if not target_row.empty:
#     id_number = target_row.iloc[0][3]  # 1 是身份证号码列的索引，根据实际情况调整
#     print(f'{target_name} 的身份证号码是：{id_number}')
# else:
#     print(f'未找到姓名为 {target_name} 的记录')

'''
表中电话为空 -> 本人电话为无 
联系人电话 -> 户主关系中向上找到户主的行-》填户主的电话
联系人姓名-》户主关系中找到户主的行——》
    弟： 户主名 + 【哥】
    父亲： 户主名 + 关系

'''

excel_file_path = './files.xlsx'
df = pd.read_excel(excel_file_path)

#tel relation re_tel re_n
def fun(target_bh):
    bh = '公民身份号码'
    re = '与户主关系'
    t ='联系电话'
    n = '姓名'
    target_row = df.loc[df[bh] == target_bh]# 通过身份证号确定目标行数

    if not target_row.empty:
        print("找到数据",len(target_row))
    else :
        print("没有找到数据")
        return {},{},{},{},{}
    name = target_row[n].iloc[0]
    print("姓名",name)
    relation = target_row[re].iloc[0]
    print("当前关系", relation)
    tel = str(target_row[t].iloc[0]).split('.')[0]  # 电话可能为空
    if( pd.isnull(tel) ):
        print("当前电话",tel)
    else:
        print("没有电话号码")
    # 找联系电话
    if relation != '户主':
        # 找到户主作为联系电话
        print("当前为非户主")
        upper_rows = df.loc[:target_row.index[0]] #获取从头到现在的所有行数据
        #print(upper_rows[upper_rows[:]['与户主关系']=='户主'].tail(1))
        upper_rel_row = upper_rows[upper_rows[:]['与户主关系']=='户主'].tail(1)
        re_tel = upper_rel_row.iloc[0][t]
        re_tel = str(re_tel).split('.')[0]
        re_n =  upper_rel_row.iloc[0][n]
        print(re_tel)
    else:
        # 户主找到成员 成员号码作为联系电话  如果成员没有联系电话 自己的号码作为联系电话
        print("当前为户主")
        target_index = target_row.index[0]
        print("当前的索引为",target_index)
        if df.iloc[target_index + 1][re] == '户主' : #只有户主的家庭
            return name, tel,relation,tel,name
        re_tel = tel #默认联系电话为自己
        re_n = name
        while 1:
            next_row = df.iloc[target_index + 1]
            print("当前与户主的关系",next_row[re])
            if pd.isna(next_row[t]) == 0 and not next_row[re] =='户主': #存在下一条身份不是户主的数据
                re_tel = next_row[t]
                re_n = next_row[n]
                relation = next_row[re]
                if re_tel:#如果rel存在 则找到一个电话号码不为空的家庭成员
                    re_tel = str(re_tel).split('.')[0]
                    print("户主的联系人姓名{},联系电话为{},".format(re_n,re_tel))
                    break
            else:
                break;
            target_index = target_index+1
    if not target_row.empty:
        if pd.isna(tel):
            tel_ = "无"
        else:
            tel_ = tel[0]
    return name,tel, relation, re_tel,re_n
    # if not target_row.empty:
    #     relation = target_row[re] #关系 不需要寻找可以直接返回
    #     relation = relation
    #     tel = str(target_row[t][0]).split('.')#电话
    #     print(relation)
    #     print(tel)
    # #找联系电话
    #     if relation != '户主':
    #         #找到户主作为联系电话
    #         upper_rows = df.loc[:target_row.index[0]]
    #         upper_rel_row = upper_rows[upper_rows[1] == '户主'].tail(1)
    #         re_tel = upper_rel_row[t]
    #     else:
    #         #户主找到成员 成员号码作为联系电话  如果成员没有联系电话 自己的号码作为联系电话
    #         while 1:
    #             target_index = target_row.index[0]
    #             next_row = df.iloc[target_index + 1]
    #             if next_row[re] == '户主':
    #                 re_tel = tel
    #                 break
    #             if pd.isna(next_row[t]) == 0:
    #                 re_tel = next_row[t][0]
    #                 break
    #
    #     if not target_row.empty:
    #         if pd.isna(tel):
    #             tel_ = "无"
    #         else:
    #             tel_= tel[0]
    #     return tel, relation, re_tel
    # else:
    #     print('未找到记录')
    #     return '','',''




# tel,relation,re_tel = fun(target_bh='513022197809077807', df=df)
# print(tel,relation,re_tel)