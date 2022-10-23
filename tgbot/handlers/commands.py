from time import time
from django.utils.translation import gettext as _
from telegram import ChatPermissions
from tgbot.utils import (
    extract_user_data_from_update, is_direct_message,
    is_admin,
)


def command_start(update, context):
    user_data = extract_user_data_from_update(update)

    if not is_direct_message(update):
        return

    text = 'Hello {} {} !'.format(user_data.get('first_name', ''), user_data.get('last_name', ''))
    user_id = extract_user_data_from_update(update)['user_id']
    context.bot.send_message(chat_id=user_id, text=text)

def health(update, conext):
    user_data = extract_user_data_from_update(update)

    if not is_direct_message(update):
        return

    conext.bot.send_message(
        chat_id=user_data.get('user_id'),
        text='Hey, {} {}! I\'m healthy!'.format(user_data.get('first_name', ''), user_data.get('last_name', ''))
    )

def lang(update, context, lang=None):
    SUPPORTED_LANGS = {
        'en': 'English 🇺🇸',
        'ua': 'Ukrainian 🇺🇦',
    }

    response = "*Supported languages:* \n"

    for code in SUPPORTED_LANGS.keys():
        response += "/{} {} \n".format(code, SUPPORTED_LANGS.get(code))

    response_chat_id = update.message.chat.id

    if not is_direct_message(update) and not is_admin(update):
        return
    
    return context.bot.send_message(parse_mode='MarkdownV2' ,chat_id=response_chat_id, text=response, reply_to_message_id=update.message.message_id)

def mute(update, context):
    if is_direct_message(update) or not is_admin(update):
        return

    mute_time = 30
    from_user = update.message.reply_to_message.from_user
    message = update.message.text.split(' ')
    if len(message) == 2:
        if message[1].isdigit():
            mute_time = int(message[1])

        if message[1] == 'forever':
            mute_time = 0

    from pprint import pp
    pp(mute_time)

    if update.message.chat.type != 'supergroup':
        return context.bot.send_message(
            parse_mode='MarkdownV2',
            chat_id=update.message.chat.id,
            text='This feature is not supported in private chats\.',
            reply_to_message_id=update.message.message_id
        )

    context.bot.restrict_chat_member(
        update.message.chat.id,
        update.message.reply_to_message.from_user.id,
        until_date=time()+((mute_time + 5) if mute_time == 0 else mute_time*60),
        permissions=ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False,
        )
    )
    
    context.bot.send_message(
        parse_mode='MarkdownV2',
        chat_id=update.message.chat.id,
        text='*{} {}* muted for {}\.'.format(from_user.first_name, from_user.last_name, str(mute_time) + ' minutes' if mute_time > 0 else 'forever'),
        reply_to_message_id=update.message.message_id
    )
