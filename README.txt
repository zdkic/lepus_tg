1.安裝需要的python套件
yum install epel-release
yum install python-pip
pip install requests

2.更換sendsms_api.py
cp sendsms_api.py /usr/local/lepus/include/

3.更換index.php
cp index.php /opt/lampp/htdocs/application/views/settings/

4.新增數據
/opt/lampp/bin/mysql -uroot -p
use lepus;
INSERT INTO `options` VALUES ('sms_telegram_bot_token', '', 'telegram机器人token');
INSERT INTO `options` VALUES ('sms_telegram_chat_id', '', 'chat_id');

5.新增字串
/opt/lampp/htdocs/application/language/zh-hans/mtop_content_lang.php
$lang['telegram_bot_token'] = 'telegram机器人token';
$lang['telegram_chat_id'] = 'telegram chat_id';
=>
加在$lang['fetion_pass'] = '飞信密码';這行後面

/opt/lampp/htdocs/application/language/english/mtop_content_lang.php
$lang['telegram_bot_token'] = 'telegram bot token';
$lang['telegram_chat_id'] = 'telegram chat_id';
=>
加在$lang['fetion_pass'] = 'Fetion Pass';這行後面

6.新增telegram測試程式
cp test_send_tg.py /usr/local/lepus/
cd /usr/local/lepus/
python test_send_tg.py
=>
確認telegram可以收到訊息

7.檢查數據
/opt/lampp/bin/mysql -uroot -p
use lepus;
select * from options;
=>
| sms_fetion_user        |                                                  | 飞信发送短信账号                                      |
| sms_fetion_pass        |                                                  | 飞信发送短信密码                                      |
| smstype                | api                                              | 发送短信方式：fetion/api                              |
| sms_telegram_bot_token | bot1967011651:AAGcNPdaf0tJPgaTNNUIpz_0jDqxehmT0-Y | telegram机器人 token                                  |
| sms_telegram_chat_id  | 799735683                                        | chat_id

8.Web介面中的告警短信收件人欄位(在配置中心/全局配置/告警/)不可為空, 可以隨便填個值
# alarm.py有檢察send_sms_to_list變數, 如果為空則不傳送短信
if send_sms_to_list:
     sms_to_list=send_sms_to_list.split(';')
else:
     send_sms=0