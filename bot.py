# ----------------------------------------------------------------------------------------
# --------------------put a licence that doesnt involve-----------------------------------
# -------------------my ass and gives you all the rights----------------------------------
# -------------------and permissions, im finna go, broda----------------------------------
# ----------------------------------------------------------------------------------------

import logging
from tpblite import TPB
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from qbittorrent import Client
from telegram import ParseMode
import os
from zipfile import ZipFile
import time


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
TOKEN = "1781260611:AAEFP471uLAWFv59h5s_6b0XQbBkaAWprF4"


class mainapp(object):
    def __init__(self):
        self.num = 0
        self.queue = ["null"]
        self.current = "Updated: \n"
        self.adult_content = ""
        self.adult_sw = "🛑️"

    def get_all_file_paths(self, directory):
        self.file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                self.file_paths.append(filepath)
        return self.file_paths

    def start(self, update: Update, context: CallbackContext) -> None:
        self.user = update.effective_user
        self.chatid = update.message.chat_id
        update.message.reply_text(
            'Hi ' + self.user.username +
            '\n    🌟️ Welcome to the unofficial TPB telegram bot 🌟️     \n\n' +
            '‼ before using this bot please go through /rules and read about the disclaimer ‼'
        )

        try:
            a = open('./users/' + str(self.user.username) + ".txt")
        except:
            os.mkdir('./users/')
            a = open('./users/' + str(self.user.username) + ".txt", "w+")
            a.write('True')

    def wrench(self, update: Update, context: CallbackContext) -> None:
        text = "🔧️ Settings 🔧️:"

        keyboard = [
            [
                InlineKeyboardButton("Set Channel🔈️", callback_data='s1')
            ],
            [
                InlineKeyboardButton("Set group 👥️", callback_data='s2')
            ],
            [
                InlineKeyboardButton("Set Google Drive", callback_data='s3')
            ],
            [
                InlineKeyboardButton("Adult content " + self.adult_sw, callback_data='grown')
            ],
            [
                InlineKeyboardButton("Close ", callback_data='end')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.bot.sendMessage(text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

    def status(self, update: Update, context: CallbackContext) -> None:
        self.current += (
                "===>> V-0.2\n\n" +
                "-> 🛠️ Settings Feature\n" +
                "-> 🗃️ Download Option for files lesser than 800mbs\n " +
                "-> 📃️ Status Feature \n" +
                "-> 💬️ Channel Or Group Posting Feature \n" +
                "-> 🐛️ Bug Clean Up")

        update.message.reply_text(self.current)

    def grp(self, update: Update, context: CallbackContext) -> None:
        a = open('./users/' + str(self.user.username) + ".txt")
        if a.read() == 'False':
            self.chatid = update.message.chat_id
            update.message.reply_text("done")

    def hands(self, update: Update, context: CallbackContext) -> None:
        a = open('./users/' + str(self.user.username) + ".txt")
        txt = update.message.text
        txt = txt.split("/feedback")
        if a.read() == 'False':
            update.message.bot.sendMessage(text=txt[1], chatid=1026202266)

    def chnl(self, update: Update, context: CallbackContext) -> None:
        a = open('./users/' + str(self.user.username) + ".txt")
        if a.read() == 'False':
            x = update.message.text
            x.split("/channel")
            self.chatid = int(x[1])
            update.message.reply_text("done")

    def law(self, update: Update, context: CallbackContext) -> None:
        a = open('./users/' + str(self.user.username) + ".txt", "w+")
        a.write('False')
        update.message.reply_text('⚠️ATTENTION⚠️: \n\n' +
                                  '‼️1, This is only a file sharing bot designed for legal and appropriate use.\n' +
                                  '‼️2, I`m not responsible for your download of any illegal content or misuse ' +
                                  'without permission!!!\n' +
                                  '‼️3, Please respect any and all licence laws of your country, telegram and any ' +
                                  'other private or government organizations related to this topic!\n' +
                                  '‼️4, this bot is affiliated with neither contents released on it nor its ' +
                                  'users!!!\n✏️ by continuing you`re agreeing to these rules ✏️ ')

    def niceguy(self, update: Update, context: CallbackContext) -> None:
        a = open('./users/' + str(self.user.username) + ".txt")
        if a.read() == 'False':
            update.message.reply_text(
                "UwU " + str(self.user.first_name) + "such a nice dude, sorry but I cant accept any" +
                "thing rn except for some motivation just say it irl, it`ll reach me don`t worry")
        else:
            update.message.reply_text('I`m sorry🙇‍♂️️ but its a must for you to check the disclaimer and' +
                                      'follow the rules, you cant access any of the commands here without ' +
                                      'that, use /rules to do so')

    def help_command(self, update: Update, context: CallbackContext) -> None:
        a = open('./users/' + str(self.user.username) + ".txt")
        if a.read() == 'False':
            update.message.reply_text('📖️welcome, the commands are pretty simple: \n' +
                                      '♠️ just text what you want \n' +
                                      '♠️ pick one from the given options\n' +
                                      '***🚧️ the download option isn`t finished yet 🚧️***\n' +
                                      '♠️ click link\n' +
                                      '♠️ copy the magnet link\n' +
                                      '♠️ use the magnet link on other bots or services like: @TorrentXbot or ' +
                                      '@uploadbot\n\n' +
                                      '💬️ for better results its recommended you specify the file type by including ' +
                                      'it in your query:\n' +
                                      '          search: \n' +
                                      '              Harry Potter book \n' +
                                      '          rather than:\n' +
                                      '               Harry Potter\n' +
                                      '💬️ note that uploading a file in telegram has a 2gb size limit\n' +
                                      '💬️ after finishing a search you should end it so that it wont mess up '
                                      'your next search\n' +
                                      '💬️ for more use /settings\n' +
                                      '💬️ need help? contact @saikyou\n'
                                      )
        else:
            update.message.reply_text('I`m sorry🙇‍♂️️ but its a must for you to check the disclaimer and follow' +
                                      ' the rules, you cant access any of the commands here without that, use /rules')

    def begin(self, update: Update, context: CallbackContext) -> None:
        a = open('./users/' + str(self.user.username) + ".txt")
        if a.read() == 'False':
            t = TPB('https://tpb.party')
            self.torrents = t.search(update.message.text)
            for x in self.torrents:
                if x.category == self.adult_content:
                    self.torrents.list.remove(x)

            message = ""
            torrent = self.torrents[0]
            keyboard = [
                [

                ],
                [

                ],
                [
                    InlineKeyboardButton("end", callback_data='end')
                ]
            ]
            text = [("1,\n✏️ NAME-> " + str(torrent.title) +
                     "\n\n💾️ SIZE-> " + str(torrent.filesize))]
            keyboard[0].append(InlineKeyboardButton('1', callback_data='0'))

            self.count = 1
            for x in range(1, 11):
                try:
                    if self.count < 8:
                        keyboard[0].append(InlineKeyboardButton(str(self.count + 1), callback_data=str(self.count)))
                    else:
                        keyboard[1].append(InlineKeyboardButton(str(self.count + 1), callback_data=str(self.count)))

                    if self.count < 11:
                        torrent = self.torrents[x]
                        text.append(str(x + 1) + ",\n✏️ <b>NAME</b> :- " + str(torrent.title) +
                                    "\n\n💾️ <b>SIZE</b> :- " + str(torrent.filesize))
                        self.count += 1
                except:
                    break

            if len(self.torrents) > 23:
                keyboard[2].append(InlineKeyboardButton('⏭️ next', callback_data='next'))
            for y in text:
                message += y + "\n------------------------------------------------------------------------\n"

            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(message, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
        else:
            update.message.reply_text('I`m sorry🙇‍♂️️ but its a must for you to check the disclaimer and' +
                                      'follow the rules, you cant access any of the commands here without ' +
                                      'that, use /rules to do so')

    def button(self, update: Update, context: CallbackContext) -> None:
        a = open('./users/' + str(self.user.username) + ".txt")
        if a.read() == 'False':
            query = update.callback_query
            query.answer()

            if query.data == 'end':
                query.edit_message_text("closed")
            elif query.data == 'link':
                query.message.reply_text(self.torrent.magnetlink)
            elif query.data == 's1':
                query.edit_message_text(
                    "Add the bot to the channel as admin and send chat id, in syntax /chnl <chat id>")
            elif query.data == 's2':
                query.edit_message_text("Add the bot to the group and do /grp")
            elif query.data == 's3':
                query.edit_message_text("not available yet, sumimasen")
            elif query.data == 'grown':
                self.adult_content = 'NULL'
                self.adult_sw = "☑️"
                text = "🔧️ Settings 🔧️:"
                keyboard = [
                    [
                        InlineKeyboardButton("Set Channel🔈️", callback_data='s1')
                    ],
                    [
                        InlineKeyboardButton("Set group 👥️", callback_data='s2')
                    ],
                    [
                        InlineKeyboardButton("Set Google Drive", callback_data='s3')

                    ],
                    [
                        InlineKeyboardButton("Adult content " + self.adult_sw, callback_data='grown')
                    ],
                    [
                        InlineKeyboardButton("Close ", callback_data='end')
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                query.edit_message_text(text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
                        
            elif query.data == 'next':
                text = []
                message = ""
                keyboard = [
                    [

                    ],
                    [

                    ],
                    [
                        InlineKeyboardButton("⛔️ end", callback_data='end')
                    ]
                ]
                for x in range(11, 21):
                    try:
                        if self.count < 21:
                            torrent = self.torrents[x]
                            text.append(str(x + 1) + ",\n✏️ <b>NAME</b> :- " + str(torrent.title) +
                                        "\n\n💾️ <b>SIZE</b> :- " + str(torrent.filesize))
                            self.count += 1

                        if self.count < 18:
                            keyboard[0].append(InlineKeyboardButton(str(self.count), callback_data=str(self.count - 1)))

                        else:
                            keyboard[1].append(InlineKeyboardButton(str(self.count), callback_data=str(self.count - 1)))
                    except:
                        break

                for y in text:
                    message += y + "\n------------------------------------------------------------------------\n"

                reply_markup = InlineKeyboardMarkup(keyboard)
                query.edit_message_text(message, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

            elif query.data == 'down':
                if len(self.queue) < 8:
                    if self.torrent.byte_size < 838860800 and self.torrent.seeds > 0:
                        qb = Client("http://127.0.0.1:8080/")
                        qb.login("admin", "12345678")
                        query.edit_message_text('Downloading....')
                        path = '/home/supergoat365/Desktop/tpbproj/torrents/' + self.torrent.title
                        self.queue.append(self.user.username)

                        try:
                            os.mkdir(path)
                        except:
                            pass
                        if not path.endswith(('.mp3', '.mp4', '.jpg', '.jpeg', '.mkv', '.m4a', '.zip')):
                            print("zip")
                            qb.download_from_link(self.torrent.magnetlink, savepath=path)
                            size = 0
                            directory = path

                            while 0 != 1:
                                file_paths = self.get_all_file_paths(directory)
                                size += os.stat(path).st_size
                                size_form = size * 0.00000095367432
                                size_2 = self.torrent.byte_size * 0.00000095367432
                                per = (size_form/size_2)*100
                                perce = str(per).split(".")
                                percent = str(round(int(perce[0]), 3)) + "%"
                                try:
                                    query.edit_message_text(
                                        'Downloading....\n' +
                                        str(round(size_form, 3)) + " / " + str(round(size_2, 3)) + "megabytes\n" +
                                        percent + ' downloaded'
                                    )
                                except:
                                    time.sleep(3)

                                if size >= self.torrent.byte_size:
                                    break

                            query.edit_message_text('Zipping....\n')
                            path = path + ".zip"
                            d = file_paths[0].split("/")

                            with ZipFile(path, 'w') as zipr:
                                for file in file_paths:
                                    zipr.write(file, d[-1])

                        else:
                            qb.download_from_link(self.torrent.magnetlink, savepath=path)
                            time.sleep(3)
                            while os.stat(path).st_size < self.torrent.byte_size:
                                size_form = os.stat(path).st_size * 0.00000095367432
                                size_2 = self.torrent.byte_size * 0.00000095367432
                                per = (size_form / size_2) * 100
                                perce = per.split(".")
                                percent = str(round(int(perce[0]), 3)) + "%"

                                try:
                                    query.edit_message_text('Downloading....\n' +
                                                            str(round(size_form, 3)) + " / " +
                                                            str(round(size_2, 3)) + "bytes\n" +
                                                            percent + "Downloaded"
                                                            )
                                except:
                                    time.sleep(1)

                        query.edit_message_text('Uploading....')
                        name = self.torrent.title.split(".")
                        ftype = name[-1]
                        self.path = path

                        self.queue.remove(self.user.username)
                        if ftype == "mp4" or ftype == "mkv":
                            query.message.reply_video(
                                                 video=open(path + "/" + self.torrent.title, 'rb'),
                                                 caption="|||🗂️ provided by @Haillmebot 🗂️|||"
                                                 )
                            os.remove(path)
                            qb.delete_all_permanently()
                        elif ftype == "mp3" or ftype == "m4a":
                            query.message.reply_audio(
                                                 audio=open(path + "/" + self.torrent.title, 'rb'),
                                                 caption="|||🗂️ provided by @Haillmebot 🗂️|||"
                                                 )
                            os.remove(path)
                            qb.delete_all_permanently()
                        elif ftype == "jpg" or ftype == "jpeg":
                            query.message.reply_photo(
                                                 photo=open(path + "/" + self.torrent.title, 'rb'),
                                                 caption="|||🗂️ provided by @Haillmebot 🗂️|||"
                                                 )
                            os.remove(path)
                            qb.delete_all_permanently()
                        else:
                            query.message.reply_document(
                                                   document=open(path, 'rb'),
                                                   caption="|||🗂️ provided by @Haillmebot 🗂️|||"
                                                   )
                            os.remove(path)
                            qb.delete_all_permanently()

                else:
                    query.edit_message_text('too many requests, please wait')

                if self.torrent.byte_size > 838860800:
                    query.edit_message_text('Sorry but currently you can only download files lesser than 800mbs')
                elif self.torrent.seeds < 1:
                    query.edit_message_text('Sorry but the torrrent has no seeds')
                elif self.torrent.seeds < 1 and self.torrent.byte_size > 838860800:
                    query.edit_message_text('Sorry but the torrrent size is too big and has no seeds')
                else:
                    print("error")

            else:
                self.torrent = self.torrents[int(query.data)]
                text = "✏️ <b>NAME</b>:- " + str(self.torrent.title) + "\n\n" + \
                       "📅️ <b>DATE</b>:- " + str(self.torrent.upload_date) + "\n\n" + \
                       "💾️ <b>SIZE</b>:- " + str(self.torrent.filesize) + "\n\n" + \
                       "💌️ <b>UPLOADER</b>:- " + str(self.torrent.seeds) + "\n\n" + \
                       "🌱️ <b>SEEDS</b>:- " + str(self.torrent.seeds) + "\n\n" + \
                       "🚸️ <b>LEECHES</b>:- " + str(self.torrent.leeches) + "\n\n" + \
                       "⚠️ <b>TRUST</b>:- " + str(self.torrent.is_trusted) + "\n\n" + \
                       "🎫️ <b>VIP</b>:- " + str(self.torrent.is_vip) + "\n\n" + \
                       "🎛️ <b>CATEGORY</b>:- " + str(self.torrent.category) + "\n\n" + \
                       "|| Provided by @Haillmebot ||"

                keyboard = [
                    [
                        InlineKeyboardButton("🔽️ Download", callback_data="down"),
                        InlineKeyboardButton("🔗️ link", callback_data="link"),
                    ],
                    [
                        InlineKeyboardButton("⛔️ end", callback_data="end"),
                    ],
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                query.edit_message_text(text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

    def main(self) -> None:
        updater = Updater(TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.start))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.button))
        dispatcher.add_handler(CommandHandler("help", self.help_command))
        dispatcher.add_handler(CommandHandler("donate", self.niceguy))
        dispatcher.add_handler(CommandHandler("rules", self.law))
        dispatcher.add_handler(CommandHandler("settings", self.wrench))
        dispatcher.add_handler(CommandHandler("grp", self.grp))
        dispatcher.add_handler(CommandHandler("chnl", self.chnl))
        dispatcher.add_handler(CommandHandler("status", self.status))
        dispatcher.add_handler(CommandHandler("feedback", self.hands))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.begin))
        updater.start_polling()
        updater.idle()


mainapp()
mainapp().main()
