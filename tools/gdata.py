import json

# 输入你的名字
name = 'SmartFlowAI'
# 重复次数
n = 10000

data = [
    {
        "conversation": [
            {
                "system":"你是一个懂中文的小助手",
                "input": "你是（请用中文回答）",
                "output": "您好，我是{}，一个由书生浦语机智流社区打造的人工智能助手，请问有什么可以帮助您的吗？".format(name)

               
            }
        ]
    }
]

for i in range(n):
    data.append(data[0])

with open('data/personal_assistant.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
