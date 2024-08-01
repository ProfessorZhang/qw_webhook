from qw_webhook.webhook import QWWebhook
def main():
    # edit your key
    webhook_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=??"
    msg_type = "text"
    msg_content = {
        "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
        "mentioned_list": ["wangqing", "@all"],
        "mentioned_mobile_list": ["13800001111", "@all"]
    }
    qw_webhook = QWWebhook(webhook_url)
    qw_webhook.send_message(msg_type,msg_content)

if __name__ == "__main__":
    main()