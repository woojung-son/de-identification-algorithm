from hyperparams import MEDICAL_INFO
from utils.name import Name
from utils.ssn import SSN
from utils.sex import SEX
from utils.age import AGE
from utils.bloodtype import BLOODTYPE
from utils.address import ADDRESS
from utils.sensitive_attributes import SA
from utils.tokenize import TOKENIZE
from utils.day import DAY

from utils.save_file import save_keyIndex, save_output
from utils.save_csv_file import save_csv_keyIndex, save_csv_output
import pandas as pd
import argparse

import os

COLUMN_TYPE = {
    'ID' : ["회원번호", "이름", "핸드폰번호", "차량번호"],
    'Quasi' : ["성별", "나이", "주소", "생일", ],
    'SA' : {
        'categorize' : ["전년도 누적금액", "전년도 누적 구매횟수", "최종구매일자", 
                        "최종 주문 요일", "주말여부", "대분류", "중분류", "세분류", 
                        "구매액"],
        'pseudonym' : {
            "직업" : [""]
        },
        'drop' : ['제품코드', '제품이름', '최종 주문시간', '수량']
    }
}

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()

    parser.add_argument('inputfile', type=str, 
                help="Enter the input file you want to pseudonym : ")
    args = parser.parse_args()
    inputfile = args.inputfile

    # medical_info.xlsx ===========================================
    #df = pd.read_excel(MEDICAL_INFO["PATH"] + MEDICAL_INFO["NAME"], sheet_name="telco", data_only=True)
    #df = pd.read_excel(inputfile, sheet_name="telco", data_only=True)
    df = pd.read_csv(inputfile)
    print(df.head(n=1))
    columns = list(df)

    for column in columns : 
        print('de-identifying ', column, ' ...')
        df_column = df[column]
        df_keyInfo = pd.DataFrame()
        if column not in COLUMN_TYPE['ID'] and column not in COLUMN_TYPE['Quasi'] : # 민감정보일 때  
            if column in COLUMN_TYPE['SA']['categorize'] :
                if column == "최종구매일자" : 
                    SensAttr = SA(df_column)
                    sr_column = SensAttr.categorizing_date()
                elif column == "최종 주문 요일" : 
                    Day = DAY(df_column)
                    sr_column = Day.categorizing()
                elif column == "주말여부" : 
                    TOKENIZE = TOKENIZE(df_column)
                    sr_column, df_keyInfo = TOKENIZE.substituting()
                else : 
                    SensAttr = SA(df_column, num_scale=0)
                    sr_column = SensAttr.categorizing()

                df[column] = sr_column
            if column in COLUMN_TYPE['SA']['pseudonym'].keys() :
                SensAttr = SA(df_column, exceptions=COLUMN_TYPE['SA']['pseudonym']["직업"], random_state = 1)
                sr_column, df_keyInfo = SensAttr.pseudonymization(pseudonym_type="Counter")
                df[column] = sr_column
            if column in COLUMN_TYPE['SA']['drop'] : 
                df.drop([column], axis='columns', inplace=True)

        else : # 식별자 or 준식별자일 때
            if column == "회원번호" or column == "회원번호" or column == "핸드폰번호" : 
                df.drop([column], axis='columns', inplace=True)
            if column == "이름" :
                # Name
                Name = Name(df_column)
                sr_column = Name.masking(2)
                df[column] = sr_column
            elif column == "주민번호" :
                # Social Security Number
                SSN = SSN(df_column)
                sr_column, df_keyInfo = SSN.pseudonymization()
                df[column] = sr_column
            elif column == "성별" : 
                # Sex
                SEX = SEX(df_column)
                sr_column, df_keyInfo = SEX.substituting()
                df[column] = sr_column
            elif column == "휴대전화" :
                df.drop([column], axis='columns', inplace=True)
            elif column == "나이" : 
                # Age
                AGE = AGE(df_column)
                sr_column= AGE.categorizing()
                df[column] = sr_column
            elif column == "주소" :
                # Address
                ADDRESS = ADDRESS(df_column)
                sr_column= ADDRESS.categorizing()
                df[column] = sr_column
            elif column == "차량번호" : 
                df.drop([column], axis='columns', inplace=True)
            elif column == "혈액형" : 
                # Bloodtype
                BLOODTYPE = BLOODTYPE(df_column)
                sr_column, df_keyInfo = BLOODTYPE.substituting()
                df[column] = sr_column

            
            if not df_keyInfo.empty :
                print(df_keyInfo)
                save_csv_keyIndex(df_keyInfo, inputfile, column)

    save_csv_output(df, inputfile, "output")
    '''
    df_name = df["이름"]
    df_ssn = df["주민번호"]
    df_sex = df["성별"]
    df_bloodtype = df["혈액형"]

    # Name
    Name = Name(df_name)
    sr_name = Name.masking(2)
    
    # Social Security Number
    SSN = SSN(df_ssn)
    sr_ssn, df_ssn_keyInfo = SSN.pseudonymizatoin()

    # Sex
    SEX = SEX(df_sex)
    sr_sex, df_sex_keyInfo = SEX.substituting()
    
    # Bloodtype
    BLOODTYPE = BLOODTYPE(df_bloodtype)
    sr_bloodtype, df_bloodtype_keyInfo = BLOODTYPE.substituting()

    df["이름"] = sr_name
    df["주민번호"] = sr_ssn
    df["성별"] = sr_sex
    df["혈액형"] = sr_bloodtype

    #save_keyIndex(df_sex_keyInfo, MEDICAL_INFO, "SEX")
    #save_keyIndex(df_ssn_keyInfo, MEDICAL_INFO, "SSN")
    #save_keyIndex(df_bloodtype_keyInfo, MEDICAL_INFO, "BLOODTYPE")
    #save_output(df, MEDICAL_INFO, "output")
    # endof medical_info.xlsx ===========================================
    
    # finantial_info.xlsx ===========================================
    df = pd.read_excel(MEDICAL_INFO["PATH"] + MEDICAL_INFO["NAME"], sheet_name="telco", data_only=True)
    df_name = df["이름"]
    df_ssn = df["주민번호"]
    df_sex = df["성별"]

    # Name
    Name = Name(df_name)
    sr_name = Name.masking(2)
    
    # Social Security Number
    SSN = SSN(df_ssn)
    sr_ssn, df_ssn_keyInfo = SSN.pseudonymizatoin()

    # Sex
    SEX = SEX(df_sex)
    sr_sex, df_sex_keyInfo = SEX.substituting()

    df["이름"] = sr_name
    df["주민번호"] = sr_ssn
    df["성별"] = sr_sex

    print(df)
    '''
    
    