"""
部分用例需要与 "wxpy 机器人" 进行互动
"""

import os
from functools import partial

import pytest

from wxpy import *

_base_dir = os.path.dirname(os.path.realpath(__file__))

_bot = Bot(os.path.join(_base_dir, 'wxpy_bot.pkl'))
_friend = ensure_one(_bot.friends().search('wxpy 机器人'))
_group = ensure_one(_bot.groups().search('wxpy test'))
_member = ensure_one(_group.search('游否'))

attachments_dir = os.path.join(_base_dir, 'attachments')
gen_attachment_path = partial(os.path.join, attachments_dir)

global_use = partial(pytest.fixture, scope='session', autouse=True)


@global_use()
def base_dir():
    return _base_dir


@global_use()
def bot():
    return _bot


@global_use()
def friend():
    return _friend


@global_use()
def group():
    return _group


@global_use()
def member():
    return _member


@global_use()
def image_path():
    return gen_attachment_path('image.png')


@global_use()
def file_path():
    return gen_attachment_path('file.txt')


@global_use()
def video_path():
    return gen_attachment_path('video.mp4')