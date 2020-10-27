import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#from hyperparams import *
import pandas as pd

def save_keyIndex(df, file, sheetname) :
    #-- write an object to an Excel sheet using pd.DataFrame.to_excel()
    #filepath = fileDict["PATH"]
    #datafile = fileDict["NAME"]
    filename = os.path.basename(file)	
    file_dir = os.path.abspath(os.path.dirname(file))
    keyfile = file_dir + "/keyInfo/" + filename.replace(".xlsx", "") + "_keyInfo.xlsx"
    
    # 최초 생성 이후 mode는 append; 새로운 시트를 추가
    if not os.path.exists(keyfile):
        with pd.ExcelWriter(keyfile, mode='w', engine='openpyxl') as writer: # pylint: disable=abstract-class-instantiated
            #df.to_excel(writer, index=False)
            df.to_excel(writer, # directory and file name to write
                        sheet_name = sheetname, 
                        na_rep = 'NaN', 
                        float_format = "%.2f", 
                        header = True, 
                        #columns = ["group", "value_1", "value_2"], # if header is False
                        index = True, 
                        index_label = "id", 
                        startrow = 0, 
                        startcol = 0, 
                        #engine = 'xlsxwriter', 
                        freeze_panes = (2, 0)
                        ) 
    else:
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
                        
def save_output(df, file, sheetname) :
    #filepath = fileDict["PATH"]
    filename = os.path.basename(file)	
    file_dir = os.path.abspath(os.path.dirname(file))
    outputfile = file_dir + "/output/" + filename.replace(".xlsx", "") + "_output.xlsx"

    if not os.path.exists(outputfile):
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
    else:
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
                        