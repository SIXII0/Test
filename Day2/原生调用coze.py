import requests
import time
# 定义API的URL
api_url = 'https://api.coze.cn/v3/chat'
retrieve_url ='https://api.coze.cn/v3/chat/retrieve'
message_url='https://api.coze.cn/v3/chat/message/list'

#定义令牌
API_token ='pat_xyvCL9CXmPwVhyfxFOfs8555awhNilMG0Dlg0uiFxyeJ7CxwGRA8w7vk1ZEbZVH2'

# 定义请求头和请求体
headers = {
    'Authorization': 'Bearer '+API_token,  # 替换API访问令牌
    'Content-Type': 'application/json'
}
#调用的机器人ID和用户ID
# bot_id = '7419135881967091712'
# user_id = '123'
# additional_messages='你好'

#text=input()
#print(text)


data1={
    'bot_id':'7419135881967091712',
    'user_id':'123',
    'additional_messages': [        #additional_messages是一个对象
       {
            "role":"user",            #对象中包含多个键值对。
            "type":"question",              
            "content":'成都九寨沟',
            "content_type":"text"
       }
    ]
}

# 发送POST请求
response1 = requests.post(api_url, headers=headers, json=data1)
# 检查响应状态码
if response1.status_code == 200:
    # 解析响应JSON数据
    result1 = response1.json()
    print('生成的文本:', result1)
    #json解码结构中'data'层'status'用[]来表示，不用'.'
    chat_id=result1['data']['id']
    conversation_id=result1['data']['conversation_id']
else:
    print('请求失败:', response1.status_code, response1.text)


    
#定义一个及时查看对话详情的函数
def getretrieve(conversation_id,chat_id):
    data2={
        'conversation_id':conversation_id,
        'chat_id':chat_id,
    }
    #发送get请求
    response2 = requests.get(retrieve_url, headers=headers,params=data2)

    #检查相应状态码
    if response2.status_code == 200:
        # 解析响应JSON数据
        result2 = response2.json()
        #print('生成的文本:', result2)

        #json解码结构中'data'层'status'用[]来表示，不用'.'
        if result2['data']['status'] != 'in_progress':     #不在进行中就退出循环
            return False
        #睡眠2秒
        time.sleep(2)
        return True
    else:
        print('请求失败:', response2.status_code, response2.text)
        return False

while True:
    if(getretrieve(conversation_id,chat_id)==False):
        break


data3={
      'conversation_id':conversation_id,
        'chat_id':chat_id,
    }

#发送get请求
response3=requests.get(message_url, headers=headers,params=data3)
if response3.status_code == 200:
    # 解析响应JSON数据
    result3 = response3.json()
    print('生成的文本:',result3)
else:
    print('请求失败:', response1.status_code, response1.text)