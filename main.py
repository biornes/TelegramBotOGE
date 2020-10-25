import telebot
import requests
def main():
    headers = {'User-Agent': ''}
    r = requests.get('https://inf-oge.sdamgia.ru/test?theme=21', headers = headers)
    print (r.content)
    pass


if __name__ == '__main__':
    main()