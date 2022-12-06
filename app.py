#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file  : app.py
@author: sunzijun
@contact : sunzijun@pku.edu.cn
@date  : 2022/12/7 1:08 上午
@version: 1.0
@desc  :
"""
import os

from pyChatGPT import ChatGPT


def chat_hf(text, session_tokenz):
    try:
        # Save the session_token variable to the system environment
        os.environ['SESSION_TOKEN'] = session_token

        # Load the saved session_token value from the system environment
        loaded_session_token = os.environ['SESSION_TOKEN']

        api = ChatGPT(session_token)
        resp = api.send_message(text)

        api.refresh_auth()  # refresh the authorization token
        api.reset_conversation()  # reset the conversation
        xyz = resp['message']
    except:

        api = ChatGPT(session_tokenz)
        resp = api.send_message(text)

        api.refresh_auth()  # refresh the authorization token
        api.reset_conversation()  # reset the conversation
        xyz = resp['message']

    return xyz


# @title GRadio for SDK api

import gradio as gr

gr.Interface(
    chat_hf,
    [gr.Textbox(label=' Input '),
     gr.Textbox(label=' If it fails enter cusom session ')],
    outputs=gr.outputs.Textbox(type="text", label="chatGPT response")
    , title="" + ' ChatGpt 🤖💬💻 on hugginface. ' + "",
    description="ChatGPT is a powerful dialog model trained by OpenAI").launch(
    debug=True)
