# -*- coding:utf-8 -*-

import requests
import config


def send_local_qwen_message(message, user_input):
    """
    请求Qwen函数
    """
    print('--------------------------------------------------------------------')
    if config.DEBUG:
        print('prompt输入:', message)
    elif user_input:
        print('用户输入:', user_input)
    print('----------------------------------')
    headers = {
        # "Authorization": f"Bearer {config.API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": message,
        "history": [
            [
                "You are a helpful assistant.", ""
            ]
        ]
    }

    try:
        response = requests.post(config.Qwen_URL, headers=headers, json=data, verify=False)
        if response.status_code == 200:
            answer = response.json()['data']
            print('LLM 输出：', answer)
            print('--------------------------------------------------------------------')
            return answer
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None


def send_chatgpt_message(message, user_input):
    """
    请求chatGPT函数
    """
    print('--------------------------------------------------------------------')
    if config.DEBUG:
        print('prompt输入:', message)
    elif user_input:
        print('用户输入:', user_input)
    print('----------------------------------')
    headers = {
        "Authorization": f"Bearer {config.GPT_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{message}"}
        ]
    }

    try:
        response = requests.post(config.GPT_URL, headers=headers, json=data, verify=False)
        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]['content']
            print('LLM 输出：', answer)
            print('--------------------------------------------------------------------')
            return answer
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None


def send_glm4_message(message, user_input):
    """
    请求 GLM4-api 服务
    """
    print('--------------------------------------------------------------------')
    if config.DEBUG:
        print('prompt输入:', message)
    elif user_input:
        print('用户输入:', user_input)
    print('----------------------------------')
    # 配置 GLM-4 的key
    headers = {
        "Authorization": f"Bearer {config.GLM4_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "glm-4",
        "messages": [
            {"role": "system", "content": "你是个人助手。"},
            {"role": "user", "content": f"{message}"}
        ]
    }

    try:
        response = requests.post(config.GLM4_URL, headers=headers, json=data)
        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]['content']
            print('LLM 输出：', answer)
            print('--------------------------------------------------------------------')
            return answer
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None


# 接口测试
if __name__ == "__main__":
    message = "你好！"
    print(send_glm4_message(message, user_input=""))
