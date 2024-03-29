import json
import requests
from tqdm import tqdm
import time
import test

A = 'eyJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImU4NjBhNWExYTZhOTQwYjQ5YmU1NjM3Y2JlNjAxODFjIiwidXNlcklkIjoiZTZlOTc3YjJkNWE2NGE0OTgyYmNhNzg3YWNhZmEwZmIiLCJzaWQiOiIyQTEwOUQ3NEM3RUYyRTJERkE0OTcwMzdFQjQwOTc4MTQ4OTBGNzE1NUYyN0JGODYzMUM3Q0EyOTE3MkU0MEVGODg1QTk0OEE2MjYyMTE3RUUwMDkxN0Q1NkYzRkNBQzUiLCJzY29wZSI6IlNDT1BFX0VIUiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3MDU0MTUyNDJ9.EURnO7_FM7U1cCDowBbj2EWVeXDRIPm7MrUa7D35UsED7vdgNxbYbVWRBso8A94SPMvCIcdsHluPUf74whFT3wk6fJFgjdamSDKMfDUgx1IBWURSUHuvIIWuANwhfS1Y7jUVyiNFvf3IzA2z6CWC0lGr9qQ-9m9QoJ9D6b_2T-wpAZFL_t4lvrsGVHkWQdB0HpYrVp87kLAnr7rJx0LXY2kMeA9B28Avv8dWp8E9odP3Iieg49L1qqiIE19Lpwxnjx8KKB12SO4pjBzHCIRw91nf7hUOLtKDgf0OegWlUgIS2psW8rS3KNNQXRrUgGFyhM-km0a5EziREAUejQdXfA'
C = 'uuid=d9a00ca7204ca246e228d5e237114eca; sid=46398098118f476498a351e0d4509f80; token=eyJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImU4NjBhNWExYTZhOTQwYjQ5YmU1NjM3Y2JlNjAxODFjIiwidXNlcklkIjoiZTZlOTc3YjJkNWE2NGE0OTgyYmNhNzg3YWNhZmEwZmIiLCJzaWQiOiIyQTEwOUQ3NEM3RUYyRTJERkE0OTcwMzdFQjQwOTc4MTQ4OTBGNzE1NUYyN0JGODYzMUM3Q0EyOTE3MkU0MEVGODg1QTk0OEE2MjYyMTE3RUUwMDkxN0Q1NkYzRkNBQzUiLCJzY29wZSI6IlNDT1BFX0VIUiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3MDU0MTUyNDJ9.EURnO7_FM7U1cCDowBbj2EWVeXDRIPm7MrUa7D35UsED7vdgNxbYbVWRBso8A94SPMvCIcdsHluPUf74whFT3wk6fJFgjdamSDKMfDUgx1IBWURSUHuvIIWuANwhfS1Y7jUVyiNFvf3IzA2z6CWC0lGr9qQ-9m9QoJ9D6b_2T-wpAZFL_t4lvrsGVHkWQdB0HpYrVp87kLAnr7rJx0LXY2kMeA9B28Avv8dWp8E9odP3Iieg49L1qqiIE19Lpwxnjx8KKB12SO4pjBzHCIRw91nf7hUOLtKDgf0OegWlUgIS2psW8rS3KNNQXRrUgGFyhM-km0a5EziREAUejQdXfA'

url = 'https://ehr.scwjxx.cn/ehrc/ehr/jkda/get/paging/simple'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accesstoken': A,
    'Accesstoken2': '',  # 替换为你的实际访问令牌2
    'Cookie': C}
number = 14
size = 14
# get时需要的参数对象
'''
qhId:   
    3组：J511722110207002
    4组：J511722110207006
    5组：J511722110207004
    6组：J511722110207001
'''
params = {
    'total': 0,
    'pageNumber': number,
    'current': 1,
    'pageSize': size,
    'area': '',
    'daztCode': 10,
    'qyCsConditionCondition': '=%3D',
    '_type': 'area',
    'wgId': '',
    'qhId': 'J511722110207001',
    'keywordType': 'zjhm',
    'zrysIds': '',
    'nlBeginType': '年',
    'nlEndType': '年',
    # 其他参数...
}

# 通过sample地址 指定params参数 拿到列表数据
response = requests.get(url, headers=headers, params=params)
data = response.json()
print("连接成功获取到多个列表数据")
print(data)

# 假设远端服务器的 API 地址为 remote_api_url
remote_api_url = 'https://ehr.scwjxx.cn/ehrc/ehr/jkda/update'

# 在请求中添加头部信息
headers1 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Accesstoken': A,
    'Accesstoken2': '',
    'Content-Type': 'application/json',
    'Cookie': C,
    'Origin': 'https://ehr.scwjxx.cn',
    'Referer': 'https://ehr.scwjxx.cn/index.html',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

url1 = 'https://ehr.scwjxx.cn/ehrc/ehr/jkda/get/'

total = 332
#
# 遍历每个不同的 daId 中的数据 通过record获取修改的id 拼接url

count = (int(params['pageNumber']) - 1) * int(params['pageSize'])
print(count)

while count != total:
    for record in data['data']['data']:
        # print(record)
        id = record['daId']
        xm = record['xm']
        # print("当前id为{},姓名为{}".format(record['daId'],record['xm']))
        url2 = url1 + record['daId']
        # 拼接的url用于获取数据 用于作为修改数据时的包内容
        response = requests.get(url2, headers=headers)
        data = response.json()  # 当前data格式中 有curseNum
        data = data['data']
        # 逻辑处理 需要修改的字段为gzwd
        # 年龄小于7岁
        '''''
        逻辑处理
            字段 nl
            字段：gzdw 务农 未成年 学生
            字段：zy： 如果是务农 则为7，且zyBbfl为农民  如果是未成年学生 则为8
            字段: ylfyzffs 全为256
        '''''
        print(
            "请求到的数据为：工作单位:{}, 职业:{}, 文化程度{},支付方式:{}".format(data['gzdw'], data['zy'], data['whcd'],
                                                                                 data['ylfyzffs']))
        data['ylfyzffs'] = 256
        age = int(data['nl'][:-1])  # 获取年龄
        zjhm = (data['zjhm'])
        print("\n当前姓名:{},身份证:{}".format(xm, zjhm, age))

        if age < 18:
            data['gzdw'] = '未成年'
            data['zy'] = 8
            if age < 7:
                data['whcd'] = 90
            elif age >= 7 and age < 12:
                data['whcd'] = 80
            elif age >= 12 and age < 15:
                data['whcd'] = 70
            elif age >= 15 and age <= 18:
                data['whcd'] = 60
            # print("修改数据为：工作单位:{}, 职业:{}, 支付方式:{},文化程度".format(data['gzdw'], data['zy'], data['ylfyzffs']))
        elif age >= 18 and age <= 22:
            data['gzdw'] = '学生'
            data['zy'] = 8
            data['whcd'] = 20
            # print("修改数据为：工作单位:{}, 职业:{}, 支付方式:{}".format(data['gzdw'], data['zy'], data['ylfyzffs']))
        else:
            data['gzdw'] = '务农'
            data['zy'] = 7
            data['zyBbfl'] = '农民'
            if age <= 30:
                data['whcd'] = 60
            elif age > 30 and age <= 40:
                data['whcd'] = 70
            elif age > 40 and age <= 50:
                data['whcd'] = 80
            else:
                data['whcd'] = 90
            # print("\n当前姓名:{},年龄为:{},修改后的支付方式为{}".format(xm, age, data['ylfyzffs']))

        print("修改数据为：工作单位:{}, 职业:{}, 文化程度{},支付方式:{}".format(data['gzdw'], data['zy'], data['whcd'],
                                                                               data['ylfyzffs']))


        name, tel, relation, re_tel, one = test.fun(zjhm)  # tel 和 re_tel有可能为空
        print("表格中数据请求完毕", name, tel, relation, re_tel, one)
        if not name and not tel and not relation and not re_tel and not one:  # 全为空 不操作
            pass
        else:  # 找到了数据
            ######填写本人电话号码####
            if tel =='nan':
                data['brdh'] = '无'
            else:
                data['brdh'] = tel

            #####联系人姓名 户主名字+关系 户主名和自己的名字一致表示只有一人口
            if name == one:
                data['lxrxm'] = '无'
            else:
                data['lxrxm'] = one + '【' + relation + '】'
            ###联系人电话
            if re_tel != 'nan':
                data['lxrdh'] = re_tel
            else:
                data['lxrdh'] = '无'
            print("修改了以下数据")
            print("本人电话{},联系人姓名{},联系人电话{}".format(data['brdh'], data['lxrxm'], data['lxrdh']))

        # 修改 然后推送
        # print(remote_api_url)
        # print(data)
        # print(headers1)
        response = requests.put(remote_api_url, json=data, headers=headers1)
        # 检查请求是否成功
        if response.status_code == 200:
            print('数据推送成功,当前的page:{}. count为：{}'.format(params['pageNumber'], count))
            response = requests.get(url2, headers=headers)
            data = response.json()
            data = data['data']

            print(
                "修改并推送后的数据为：工作单位:{}, 职业:{}, 文化程度{},支付方式:{}".format(data['gzdw'], data['zy'],
                                                                                           data['whcd'],
                                                                                           data['ylfyzffs']))
        else:
            print('数据推送失败，状态码:', response.status_code)
            print('错误信息:', response.text)
        count = count + 1
        time.sleep(1)

    print("当前页面执行完毕")
    time.sleep(1)
    number = number + 1
    params['pageNumber'] = number
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(params['pageNumber'])

#

'''
# 假设远端服务器的 API 地址为 remote_api_url
remote_api_url = 'https://ehr.scwjxx.cn/ehrc/ehr/jkda/update'

# 在请求中添加头部信息
headers1 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Accesstoken': 'eyJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImU4NjBhNWExYTZhOTQwYjQ5YmU1NjM3Y2JlNjAxODFjIiwidXNlcklkIjoiZTZlOTc3YjJkNWE2NGE0OTgyYmNhNzg3YWNhZmEwZmIiLCJzaWQiOiI5QTUyNkIyODg1Q0UwNzVBOTE4QkIxNEY0RTQxQUQwMDVBMEIwREI4OTcyQzM2Q0U2MEE2MUQ0OUU1NTk4QjZBODg1QTk0OEE2MjYyMTE3RUUwMDkxN0Q1NkYzRkNBQzUiLCJzY29wZSI6IlNDT1BFX0VIUiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3MDQ1NTAzODJ9.HC2B0nAVCVHaC-jX7tr7C8MSzJGxG8gg1xg5xnkXNHAACT-yfa9FMqgLgra9XKi1lZZ_nIPtiAEMgW5vUeQ2NFR0CI_1e5UQ10UD0VtGeboYb-lYTn-XlK6YeXKmK4_MnK_vQzcE9Tk--kv5RWCYgm5KHYKLbhAO4RwkTQEd5svOGJO0CHWT0LRA8xs9XDCYjvfWwOc_wTKhcexsE2xxe_YhYmdY4CtXrH0w-Hv4GPEbtfPtd-xRgsU5sh3GoQmv6jlMgN8YlptrMnlavkC03tINmkawXUBD7tTRHkLBhFMYd3bAmqSunAs9wCSa5HkhUEYheeiKHq8Zu4tAJjWHcg',  # 替换为你的实际访问令牌
    'Accesstoken2': '',
    'Content-Length': '4038',
    'Content-Type': 'application/json',
    'Cookie': 'uuid=d9a00ca7204ca246e228d5e237114eca; sid=5db402d5246c4f33b62d27f28136fdd9; token=yeyJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImU4NjBhNWExYTZhOTQwYjQ5YmU1NjM3Y2JlNjAxODFjIiwidXNlcklkIjoiZTZlOTc3YjJkNWE2NGE0OTgyYmNhNzg3YWNhZmEwZmIiLCJzaWQiOiI5QTUyNkIyODg1Q0UwNzVBOTE4QkIxNEY0RTQxQUQwMDVBMEIwREI4OTcyQzM2Q0U2MEE2MUQ0OUU1NTk4QjZBODg1QTk0OEE2MjYyMTE3RUUwMDkxN0Q1NkYzRkNBQzUiLCJzY29wZSI6IlNDT1BFX0VIUiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3MDQ1NTAzODJ9.HC2B0nAVCVHaC-jX7tr7C8MSzJGxG8gg1xg5xnkXNHAACT-yfa9FMqgLgra9XKi1lZZ_nIPtiAEMgW5vUeQ2NFR0CI_1e5UQ10UD0VtGeboYb-lYTn-XlK6YeXKmK4_MnK_vQzcE9Tk--kv5RWCYgm5KHYKLbhAO4RwkTQEd5svOGJO0CHWT0LRA8xs9XDCYjvfWwOc_wTKhcexsE2xxe_YhYmdY4CtXrH0w-Hv4GPEbtfPtd-xRgsU5sh3GoQmv6jlMgN8YlptrMnlavkC03tINmkawXUBD7tTRHkLBhFMYd3bAmqSunAs9wCSa5HkhUEYheeiKHq8Zu4tAJjWHcg	',  # 替换为你的实际 Cookie
    'Origin': 'https://ehr.scwjxx.cn',
    'Referer': 'https://ehr.scwjxx.cn/index.html',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

# 使用 requests 发送 PUT 请求将数据推送到远端服务器
print(data)
response = requests.put(remote_api_url, json=data['data'], headers=headers1)

# # 遍历数据找到需要修改的字段
# for record in data['data']['data']:
#     if 'ylfyzffs' in record:
#         # 找到 ylfyzffs 字段并修改
#         record['ylfyzffs'] = 1  # 修改为你需要的值
#
# # 将修改后的数据转换为 JSON 字符串
# modified_data_json = json.dumps(data)
#
# # 假设远端服务器的 API 地址为 remote_api_url
# remote_api_url = 'https://ehr.scwjxx.cn/ehrc/ehr/jkda/update'
#
# # 使用 requests 发送 POST 请求将数据推送到远端服务器
# response = requests.post(remote_api_url, json={'data': modified_data_json})
#
# # 检查请求是否成功
# if response.status_code == 200:
#     print('数据推送成功')
# else:
#     print('数据推送失败，状态码:', response.status_code)
#     print('错误信息:', response.text)




# # Step 1: 获取数据
# url = 'https://ehr.scwjxx.cn/ehrc/ehr/jkda/get/paging/simple?total=0&pageNumber=1&current=1&pageSize=4&area=&daztCode=10&qyCsConditionCondition=%3D&_type=area&wgId=&qhId=J511722110207002&keywordType=zjhm&zrysIds=&nlBeginType=%E5%B9%B4&nlEndType=%E5%B9%B4'
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()['data']['data']
#
#     # Step 2: 解析数据，找到需要修改的字段
#     for item in data:
#         # 假设我们要修改 'gxId' 字段
#         gx_id = item.get('gxId', '')
#
#         # Step 3: 修改字段
#         if gx_id:
#             # 修改 'gxId' 为新的值
#             item['gxId'] = 'new_value'
#
#     # Step 4: 构造更新请求
#     update_url = 'https://ehr.scwjxx.cn/update_user_data'
#     update_payload = {'data': data}  # 这取决于服务器的 API 设计
#
#     update_response = requests.post(update_url, json=update_payload)
#
#     if update_response.status_code == 200:
#         print("数据更新成功")
#     else:
#         print("数据更新失败")
#
# else:
#     print("获取数据失败")
'''
