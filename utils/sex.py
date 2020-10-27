import pandas as pd
import numpy as np

class SEX :
    def __init__(self, df_sex, random_state = np.random.randint(100)) : 
        self.df_sex = df_sex
        np.random.seed(random_state)
        #self.matching_table_dict = np.random.choice([1,2], 2, replace=False)
        #print(self.matching_table)
        self.matching_table_dict = dict(zip(['남', '여'], np.random.choice([1,2], 2, replace=False)))

    def masking(self, masking_digit = 13) :
        temp_name = []
        #write_wb = Workbook()
        
        for element in self.df_sex :
            element = element.replace(element[1:], "*" * (len(element) - 1))
            temp_name.append(element)
            

        sr_name = pd.Series(temp_name)
        return sr_name

    def pseudonymizatoin(self, pseudonym_type = "HASH") :
        if pseudonym_type == "HASH" :
            sr_ssn, df_ssn_keyInfo = 1,2
        
        return sr_ssn, df_ssn_keyInfo

    def substituting(self) : 
        temp_sex = []
        for element in self.df_sex :
            if str(element) not in self.matching_table_dict.keys() : # 결측치 탐지
                self.matching_table_dict[str(element)] = max(self.matching_table_dict.values()) + 1

            temp_sex.append(self.matching_table_dict[element])

        sr_sex = pd.Series(temp_sex)
        df_sex_keyInfo = pd.DataFrame({'key' : list(self.matching_table_dict.keys()), 
                                        'value' : list(self.matching_table_dict.values())}, 
                                        index = range(len(self.matching_table_dict)))
        return sr_sex, df_sex_keyInfo



        
