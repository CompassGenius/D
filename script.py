class Script(object):
    START_TXT = """<b>@cinema_kotaka..!</b>"""
    FORCESUB_TXT = "You Need To Join Our Channel and Press Refresh Button to get the file\n🍎ഫയലുകൾ ലഭിക്കുന്നതിനായി  നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ join ചെയ്യണം\n🍎 ശേഷം refresh button അമർത്തുക",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Join Channel",url="https://t.me/Dustinreq")],
                                                       [InlineKeyboardButton(text="Refresh", url=f"https://t.me/{me.username}?start={file_uid}")]]),
                    reply_to_message_id=update.message_id
