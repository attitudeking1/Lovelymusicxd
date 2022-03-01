from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import BOT_USERNAME

from config import SUPPORT_CHANNEL, SUPPORT_GROUP


def choose_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 Play Music",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎥 Play Video",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Updates",
                url=f"{SUPPORT_CHANNEL}",
            ),
            InlineKeyboardButton(
                text="Support",
                url=f"{SUPPORT_GROUP}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑 Close Search",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="Add me",
                url=f"t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ], 
    ]
    return buttons


def livestream_markup(quality, videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎥  Start Live",
                callback_data=f"LiveStream {quality}|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 Close",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Updates",
                url=f"{SUPPORT_CHANNEL}",
            ),
            InlineKeyboardButton(
                text="Support",
                url=f"{SUPPORT_GROUP}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Add me",
                url=f"t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ], 
    ]
    return buttons


def stream_quality_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📽 360P",
                callback_data=f"VideoStream 360|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 720P",
                callback_data=f"VideoStream 720|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 480P",
                callback_data=f"VideoStream 480|{videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back",
                callback_data=f"gback_list_chose_stream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 Close Search",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons
