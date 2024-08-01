from qw_webhook.webhook import QWWebhook

webhook_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a7b704b2-889c-4d30-8026-359f010ceb7f"
msg_type = "text"
msg_content ={
        "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
		"mentioned_list":["wangqing","@all"],
		"mentioned_mobile_list":["13800001111","@all"]
    }

# msg_type = "markdown"
# msg_content = {
#         "content": "实时新增用户反馈<font color=\"warning\">132例</font>，请相关同事注意。\n类型:<font color=\"comment\">用户反馈</font>普通用户反馈:<font color=\"comment\">117例</font>VIP用户反馈:<font color=\"comment\">15例</font>"
#     }

# msg_type = "news"
# msg_content = {
# "articles" : [
#            {
#                "title" : "中秋节礼品领取",
#                "description" : "今年中秋节公司有豪礼相送",
#                "url" : "www.qq.com",
#                "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
#            }
#         ]
#     }



qw_webhook = QWWebhook(webhook_url)
qw_webhook.send_message(msg_type, msg_content)