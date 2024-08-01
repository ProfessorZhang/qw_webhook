import json
import logging
import sys
from requests.exceptions import RequestException
import requests
import argparse


logging.basicConfig(level=logging.INFO,stream=sys.stdout,format='%(asctime)s - %(levelname)s - %(message)s')
class QWWebhook:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send_message(self,msgtype:str,msgcontent:dict):
        """
        Send a message to WeChat Work (企业微信) using a webhook URL

        For more information, please refer to the official documentation: https://developer.work.weixin.qq.com/document/path/99110
        :param webhookurl: The webhook URL to send the message to.
        :param msgtype: The type of the message (e.g., "markdown").
        :param msgcontent: The content of the message.
        """

        if msgtype not in ["text","markdown","news","image","file","voice","template_card"]:
            raise ValueError("Invalid message type. Supported types are 'text','markdown','news','file','voice','template_card'.")

        webhook_header = {"Content-Type": "application/json"}
        webhook_data = {
            "msgtype": msgtype,
             msgtype : msgcontent
        }

        try:
            response = requests.post(self.webhook_url,data=json.dumps(webhook_data),headers=webhook_header)
            response.raise_for_status
            logging.info("webhook request success")
        except RequestException as e:
            logging.error(f"webhook request failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Send a message to WeChat Work (企业微信) via webhook.")
    parser.add_argument('--webhook_url', type=str, required=True, help="The webhook URL to send the message to.")
    parser.add_argument('--msg_type', type=str, required=True, choices=["text","markdown","news","image","file","voice","template_card"],help="The type of the message.")
    parser.add_argument('--msg_content', type=dict, required=True, help="The content of the message.")

    args = parser.parse_args()
    qw_webhook = QWWebhook(args.webhook_url)
    qw_webhook.send_message(args.msg_type, args.msg_content)

if __name__ == "__main__":
    main()