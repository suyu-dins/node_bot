import telebot
import requests
import base64
import random
import datetime

# 获取当前日期和时间
dt = datetime.datetime.now()
formatted_dt = dt.strftime('%Y-%m-%d %H:%M')

BOT_TOKEN = "6166183546:AAFe_HnAot-YUUpd2QYy4VwG6_PoHaTVuRE"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["node"])
def get_nodes(message):
    try:
        url = 'https://pastebin.com/raw/LLTyw9Bw'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} 

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        content = response.content
        decoded_content = base64.b64decode(content).decode('utf-8')
        list_of_lines = decoded_content.split('\n')
        random.shuffle(list_of_lines)
        selected_elements = list_of_lines[:10]

        text = '\n'.join(selected_elements)
        text = text + "\n\n获取节点时间为：%s" % (formatted_dt)
        bot.reply_to(message, text)
        print("获取节点成功！")

    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f'获取节点信息失败：{e}')

print("机器人启动成功！")
bot.polling()
