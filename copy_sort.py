#This script searching the evaluation files
import os
import datetime

def list():
    # searching recursive in the folder with os.walk
    for root, dirs, files in os.walk('D:\\Communicator\\CommunicationInterface\\'):
        for file in files:
            # specify the extension of the file
            if file.endswith('.csv'):
                global file_name, edited_filename
                Y = int(file[5:9])
                M = int(file[10:12])
                D = 1

                '''print(os.path.join(root, file))'''                                                  # ha kell a teljes útvonal is akkor kell a root, ha csak a fájlnév akkor csak a file
                file_name = datetime.datetime(Y, M, D)
                edited_filename = file_name.strftime('%Y-%B')
                os.system(f'mkdir -p D:\\csv_files\\{edited_filename}')

                if M == 1:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-January')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 2:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-February')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 3:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-March')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 4:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-April')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 5:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-May')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 6:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-June')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 7:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-July')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 8:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-August')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 9:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-September')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 10:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-Oktober')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 11:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-November')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')
                if M == 12:
                    source = (os.path.join(root, file))
                    destination = ('D:\\csv_files\\2022-December')
                    os.system(f'xcopy {source} {destination} /d/e/c/i/h/r/k/y')

list()
