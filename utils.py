from pony.orm import *
from pyrogram.types import Message
from os import listdir

# ========= DB build =========
db = Database()


class User(db.Entity):
    uid = PrimaryKey(int, auto=True)
    status = Required(int)  # status-user: "INSERT"/"NOT-INSERT"


db.bind(provider='sqlite', filename='zipbot.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# ========= helping func =========
def dir_work(uid: int) -> str:
    """ static-user folder """
    return f"static/{uid}/"


def zip_work(uid: int) -> str:
    """ zip-archive file """
    return f'static/{uid}.zip'


def list_dir(uid: int) -> list:
    """ items in static-user folder """
    return listdir(dir_work(uid))


def up_progress(current, total, msg: Message):
    """ edit status-msg with progress of the uploading """
    msg.edit(f"**Upload progress: {current * 100 / total:.1f}%**")

def process_command(command):
    # Split the command into command name and arguments
    parts = command.split()
    command_name = parts[0]
    args = parts[1:]

    # Process the command based on the command name
    if command_name == "/zip":
        # Assuming the arguments after the command specify the directory path and output file path
        directory_path = args[0]
        output_file_path = args[1]

        # Call the function to create the zip archive
        create_zip_archive(directory_path, output_file_path)

def create_zip_archive(directory_path, output_file_path):
    with zipfile.ZipFile(output_file_path, 'w') as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory_path))

# ========= MSG class =========
class Msg:

    def start(msg: Message) -> str:
        """ return start-message text """
        txt = f"Hey {msg.from_user.mention}!\n" \
              "\nI can compress files in to an archive." \
              "\nJust send /zip, and follow the instructions."
        return txt

    zip = "Send the files you want to compress, and at the end send /stopzip after all the files have been downloaded.\n" \
          "\n\nNote: due to upload limit, the total size of the file(s) can be at most 2GB."
    too_big = "Note: due to upload limit, the total size of the file(s) can be at most 2GB."
    too_much = "Note: the total number of the files can be at most 500"
    send_zip = "Send /zip to compress the files"
    zipping = "start compressing {} files..."
    uploading = "uploading archive..."
    unknow_error = "An unknown error occurred"
    downloading = "downloading..."
    zero_files = "No files were sent"
