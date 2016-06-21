#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import signal
import sys
import json
from .cipher import Caesar

import requests

class Bot:

    def __init__(self):
        self.token = '220644016:AAFPqs28vTXx63w9imQHEGxwLdCafur3GA0'
        self.update_id = 0
        self.caesar = Caesar(3)

    def make_query(self, method, payload=None):
        url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, method)
        r = requests.post(url, payload, timeout=0.5)
        return r.json()

    def get_me(self):
        response = self.make_query('getMe')
        return response

    def get_updates(self, offset, limit=100, timeout=0):
        response = self.make_query('getUpdates', {'offset': offset, 'limit': limit, 'timeout': timeout})
        return response

    def set_webhook(self, url):
        response = self.make_query('setWebhook', {'url': url})
        return response

    def delete_webhook(self):
        response = self.make_query('setWebhook')
        return response

    def send_message(self, chat_id, text=None, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        response = self.make_query('sendMessage', {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'disable_notification': disable_notification, 'reply_to_message_id': reply_to_message_id, 'reply_markup': reply_markup})
        return response

    def forward_message(self, chat_id, from_chat_id, message_id, disable_notification=False):
        response = self.make_query('forwardMessage', {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'disable_notification': disable_notification, 'message_id': message_id})
        return response

    def checkResult(self, result):
        print(result)
        if 'message' in result:
            if 'type' in result['message']['chat']:
                if result['message']['chat']['type'] == 'private':
                    if 'text' in result['message']:
                        decrypted_sentence = self.caesar.decrypt_sentence(result['message']['text'])
                        self.send_message(result['message']['chat']['id'], text=decrypted_sentence)

        if 'inline_query' in result:
            if result['inline_query']['query']:
                sentence = result['inline_query']['query']
                encrypted_sentence = self.caesar.encrypt_sentence(sentence)

                document = json.dumps([{'type': 'article',
                                        'id': '0',
                                        'input_message_content': {'message_text': encrypted_sentence },
                                        'title': "Send your text encrypted",
                                        'description': encrypted_sentence
	            }])

                response = requests.post(
                    url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'answerInlineQuery'),
                    data={'inline_query_id': result['inline_query']['id'], 'results': document},
                    timeout=0.5
                ).json()
