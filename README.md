# mone_

CLI tool to store your transactions.
NO methods are given to process the stored information, it is just meant for storing.

Stores in a file with extension .udb with the format:

     :<transaction_type = (r)eceived or (s)pent>-<date>-<amount>-<description = string written between *-*>:
      

eg- :(r)-2022_09_30-400-*found on road*:

Note: the found on road text will be inside two *'s


I suggest building the executable and adding it to path, as you want to access it from anywhere.
for building install pyinstaller and run

      pyinstaller --noconfirm --onefile --console --add-data "../path-to-udb-folder"  "../path-to-file.py"
