#This program only runs properly in the right environment but some code
#fragments can be used on their own.
#This evaluation program is a special use program. Evaluate the .csv files and
#makes a statement on the scrap rate. Create several new csv file where can you
#see these velues and create a graph about it.

import csv
import glob, os, datetime
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# This program runs first backup script, what you can find on the link below.
# https://github.com/kiskokas/Python_Code.git

exec(open('copy_sort.py').read())

#Here you can select the folder where the files are.

root = tk.Tk()
root.withdraw()

path = filedialog.askdirectory(title='Select folder')
selected_folder_name = path[13:]

os.chdir(f'D:\\csv_files\\{selected_folder_name}\\')
os.system(f'mkdir -p D:\\_Evaluation_\\2022\\{selected_folder_name}')

start = input('Please enter the number of Week or Press Enter: ')

monthly_parts = 0
monthly_result = 0
msumm_st20 = 0
msumm_st30 = 0
msumm_st40 = 0
msumm_st50 = 0
msumm_st51 = 0
msumm_st60 = 0
msumm_st80 = 0

summ_all_parts = 0
summ_result = 0
summ_st20 = 0
summ_st30 = 0
summ_st40 = 0
summ_st50 = 0
summ_st51 = 0
summ_st60 = 0
summ_st80 = 0
all_parts = -1
result = 0
final_percent = 0


def week_nr():
        global date, cw
        date = datetime.date(year, month, day)
        date = date.strftime('%Y_%m_%d')
        date = datetime.datetime(year, month, day)
        cw = date.strftime('%W')
#Create a new csv file and fill out with the values of monthly evaluation.
def csv_monthly():

        header = ['datum', 'Produced Parts', 'NOK Parts', 'NOK Parts on St20', 'NOK Parts on St30', 'NOK Parts on St40',
                  'NOK Parts on St50', 'NOK Parts on St51', 'NOK Parts on St60', 'NOK Parts on St80', 'Rate of error']

        csv_data = [selected_folder_name, monthly_parts, monthly_result, msumm_st20, msumm_st30, msumm_st40, msumm_st50, msumm_st51, msumm_st60,
                    msumm_st80, final_percent]

        with open(f'D:\\_Evaluation_\\2022\\{selected_folder_name}\\{selected_folder_name}_month.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(csv_data)

#Create a new csv file and fill out with the values of weekly evaluation.
def csv_weekly_header():
        header = ['datum', 'Produced Parts', 'NOK Parts', 'NOK Parts on St20', 'NOK Parts on St30', 'NOK Parts on St40',
                  'NOK Parts on St50', 'NOK Parts on St51', 'NOK Parts on St60', 'NOK Parts on St80', 'Rate of error']

        with open(f'D:\\_Evaluation_\\2022\\{selected_folder_name}\\{selected_folder_name}_weekl.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)

def csv_weekly():
        csv_data = [file, all_parts, result, result_St20, result_St30, result_St40, result_St50, result_St51, result_St60,
                    real_result_St80, percent]

        with open(f'D:\\_Evaluation_\\2022\\{selected_folder_name}\\{selected_folder_name}_weekl.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(csv_data)
#Create a new csv file and fill out with the values of daily evaluation.
def csv_daily_header():
        header = ['datum', 'CW', 'Produced Parts', 'NOK Parts', 'NOK Parts on St20', 'NOK Parts on St30', 'NOK Parts on St40',
                  'NOK Parts on St50', 'NOK Parts on St51', 'NOK Parts on St60', 'NOK Parts on St80', 'Rate of error']

        with open(f'D:\\_Evaluation_\\2022\\{selected_folder_name}\\{selected_folder_name}_daily.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)

def csv_daily():
        csv_data = [file, cw, mall_parts, mresult, mresult_St20, mresult_St30, mresult_St40, mresult_St50, mresult_St51, mresult_St60,
                    mreal_result_St80, mpercent]

        with open(f'D:\\_Evaluation_\\2022\\{selected_folder_name}\\{selected_folder_name}_daily.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(csv_data)
#Barchart
def chart():
        fig = plt.figure(figsize=(6, 6), dpi=100)
        labels = ('St20', 'St30', 'St40', 'St50', 'St51', 'St60', 'St80')
        labelpos = np.arange(len(labels))
        data_monthly = [msumm_st20,msumm_st30,msumm_st40,msumm_st50,msumm_st51,msumm_st60,msumm_st80]

        ##This section formats the barchart for output

        plt.bar(labelpos, data_monthly, align='center', alpha=1.0)
        plt.xticks(labelpos, labels)
        plt.ylabel('By the piece of NOK Parts')
        plt.xlabel('Stations')
        plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
        plt.title('NOK')
        plt.xticks(rotation=30, horizontalalignment="center")

        #Applies the values on the top of the bar chart
        for index, datapoints in enumerate(data_monthly):
            plt.text(x=index, y=datapoints + 0.1, s=f"{datapoints}", fontdict=dict(fontsize=10), ha='center', va='bottom')

        plt.savefig(f'D:\\_Evaluation_\\2022\\{selected_folder_name}\\{selected_folder_name}_graph.png')
        '''plt.show()'''

#Open the csv file and do the evaluation
def analyse():

        with open(real_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                global result, percent
                result = 0
                global result_St20, result_St30, result_St40, result_St50, result_St51, result_St60, result_St80, real_result_St80
                result_St20 = 0
                result_St30 = 0
                result_St40 = 0
                result_St50 = 0
                result_St51 = 0
                result_St60 = 0
                result_St80 = 0
                real_result_St80 = 0
                summ_previous_states = 0
                global all_parts
                all_parts = -1
                search_parts = 'NOK'
                search_NOK_State = 'NIO'

                for row in csv_reader:
                        if search_parts in str(row):

                                all_parts += 1
                                result += 1
                                if search_NOK_State in str(row[13]):
                                        result_St20 += 1
                                if search_NOK_State in str(row[23]):
                                        result_St30 += 1
                                if search_NOK_State in str(row[26]):
                                        result_St40 += 1
                                if search_NOK_State in str(row[52]):
                                        result_St50 += 1
                                if search_NOK_State in str(row[56]):
                                        result_St51 += 1
                                if search_NOK_State in str(row[66]):
                                        result_St60 += 1
                                if search_NOK_State in str(row[104]):
                                        summ_previous_states = result_St20 + result_St30 + result_St40 + result_St50 + result_St51 + result_St60
                                        result_St80 += 1
                                        real_result_St80 = result_St80 - summ_previous_states
                        else:
                                all_parts += 1

        percent = round(((result / all_parts) * 100), 2)

def monthly_analyse():

        with open(file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                global mresult, mpercent
                mresult = 0
                global mresult_St20, mresult_St30, mresult_St40, mresult_St50, mresult_St51, mresult_St60, mresult_St80, mreal_result_St80
                mresult_St20 = 0
                mresult_St30 = 0
                mresult_St40 = 0
                mresult_St50 = 0
                mresult_St51 = 0
                mresult_St60 = 0
                mresult_St80 = 0
                mreal_result_St80 = 0
                msumm_previous_states = 0
                global mall_parts
                mall_parts = -1
                msearch_parts = 'NOK'
                msearch_NOK_State = 'NIO'

                for row in csv_reader:
                        if msearch_parts in str(row):

                                mall_parts += 1
                                mresult += 1
                                if msearch_NOK_State in str(row[13]):
                                        mresult_St20 += 1
                                if msearch_NOK_State in str(row[23]):
                                        mresult_St30 += 1
                                if msearch_NOK_State in str(row[26]):
                                        mresult_St40 += 1
                                if msearch_NOK_State in str(row[52]):
                                        mresult_St50 += 1
                                if msearch_NOK_State in str(row[56]):
                                        mresult_St51 += 1
                                if msearch_NOK_State in str(row[66]):
                                        mresult_St60 += 1
                                if msearch_NOK_State in str(row[104]):
                                        msumm_previous_states = mresult_St20 + mresult_St30 + mresult_St40 + mresult_St50 + mresult_St51 + mresult_St60
                                        mresult_St80 += 1
                                        mreal_result_St80 = mresult_St80 - msumm_previous_states
                        else:
                                mall_parts += 1

        mpercent = round(((mresult / mall_parts) * 100), 2)

#If the user has specified the number of week then will run this fragment also
#and fill out the weekly csv also, if not then will be empty.
csv_weekly_header()
for file in glob.glob('*.csv'):
        year = int(file[5:-10])
        month = int(file[10:-7])
        day = int(file[13:-4])
        week_nr()
        if cw == start:
                real_file = file[0:]
                analyse()
                csv_weekly()
                summ_all_parts += all_parts
                summ_result += result

csv_daily_header()
for file in glob.glob('*.csv'):
        year = int(file[5:-10])
        month = int(file[10:-7])
        day = int(file[13:-4])
        week_nr()
        monthly_analyse()
        csv_daily()
        monthly_parts += mall_parts
        monthly_result += mresult
        msumm_st20 += mresult_St20
        msumm_st30 += mresult_St30
        msumm_st40 += mresult_St40
        msumm_st50 += mresult_St50
        msumm_st51 += mresult_St51
        msumm_st60 += mresult_St60
        msumm_st80 += mreal_result_St80
        final_percent = round((monthly_result / monthly_parts)*100, 2)

csv_monthly()
print('The analysis is complete!')
chart()
