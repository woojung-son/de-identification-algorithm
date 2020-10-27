import sys, os
import csv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#from hyperparams import *
import pandas as pd

def save_csv_keyIndex(df, file, sheetname) :
    # file = C:\Users\sonwj\vscode python workplace\covid19-app\pseudonymization\data\k_ciber_security.csv
    # sheetname = k_ciber_security
    filename = os.path.basename(file)
    file_dir = os.path.abspath(os.path.dirname(file))

    #outputfile = file_dir + "/keyInfo/" + filename.replace(".csv") + "_output.csv"
    keyfile = file_dir + "/keyInfo/" + filename.replace(".csv", "") + "_csv_keyInfo.csv"
    
    # 최초 생성 이후 mode는 append; 새로운 시트를 추가
    if not os.path.exists(keyfile):
        #fp = open('data.csv', 'r', encoding='utf-8')
        #rdr = csv.reader(fp)
        #for line in rdr :
        #    print(line)
        #df.to_csv(keyfile, header=True, index=False, encoding="euc-kr")
        df.to_csv(keyfile, header=True, index=False, encoding="utf-8-sig")

    else:
        '''
        with pd.ExcelWriter(keyfile, mode='a', engine='openpyxl') as writer: # pylint: disable=abstract-class-instantiated
            #df.to_excel(writer, index=False)
            df.to_excel(writer, # directory and file name to write
                        sheet_name = sheetname, 
                        na_rep = 'NaN', 
                        float_format = "%.2f", 
                        header = True, 
                        #columns = ["group", "value_1", "value_2"], # if header is False
                        index = False, 
                        index_label = "id", 
                        startrow = 0, 
                        startcol = 0, 
                        #engine = 'xlsxwriter', 
                        freeze_panes = (2, 0)
                        ) 
        '''
                        
def save_csv_output(df, file, sheetname) :
    #filepath = fileDict["PATH"]
    filename = os.path.basename(file)	
    file_dir = os.path.abspath(os.path.dirname(file))
    outputfile = file_dir + "/output/" + filename.replace(".csv", "") + "_output.csv"

    if not os.path.exists(outputfile):
        df.to_csv(outputfile, header=True, index=False)
        '''
        with pd.ExcelWriter(outputfile, mode='w', engine='openpyxl') as writer: # pylint: disable=abstract-class-instantiated
            #df.to_excel(writer, index=False)
            df.to_excel(writer, # directory and file name to write
                        sheet_name = sheetname, 
                        na_rep = 'NaN', 
                        float_format = "%.2f", 
                        header = True, 
                        #columns = ["group", "value_1", "value_2"], # if header is False
                        index = False, 
                        #index_label = "data-id", 
                        startrow = 0, 
                        startcol = 0, 
                        #engine = 'xlsxwriter', 
                        freeze_panes = (2, 0)
                        ) 
        '''
    else:
        file_list = os.listdir(file_dir)
        k_cyber_numlist = []

        for file in file_list :
            if 'k_ciber_security' in file :
                k_cyber_numlist.append(int(file[16]))
        if len(k_cyber_numlist) == 0 :
            k_cyber_nextnum = 1
        else :
            k_cyber_nextnum = max(k_cyber_numlist) + 1

        outputfile = file_dir + "/output/" + filename.replace(".csv") + "_output_" + str(k_cyber_nextnum) + ".csv"

        '''
        with pd.ExcelWriter(outputfile, mode='a', engine='openpyxl') as writer: # pylint: disable=abstract-class-instantiated
            #df.to_excel(writer, index=False)
            df.to_excel(writer, # directory and file name to write
                        sheet_name = sheetname, 
                        na_rep = 'NaN', 
                        float_format = "%.2f", 
                        header = True, 
                        #columns = ["group", "value_1", "value_2"], # if header is False
                        index = False, 
                        #index_label = "data-id", 
                        startrow = 0, 
                        startcol = 0, 
                        #engine = 'xlsxwriter', 
                        freeze_panes = (2, 0)
                        ) 
        '''