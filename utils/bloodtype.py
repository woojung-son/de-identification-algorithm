import pandas as pd
import numpy as np

class BLOODTYPE :
    def __init__(self, df_bloodtype, random_state = np.random.randint(100)) : 
        self.df_bloodtype = df_bloodtype
        np.random.seed(random_state)
        #self.matching_table_dict = np.random.choice([1,2], 2, replace=False)
        #print(self.matching_table)
        self.matching_table_dict = dict(zip(['A', 'B', 'O', 'AB'], np.random.choice([1,2,3,4], 4, replace=False)))

    def masking(self, masking_digit = 13) :
        temp_name = []
        #write_wb = Workbook()
        
        for element in self.df_bloodtype :
            element = element.replace(element[1:], "*" * (len(element) - 1))
            temp_name.append(element)
            

        sr_bloodtype = pd.Series(temp_name)
        print(sr_bloodtype)
        return sr_bloodtype

    def pseudonymizatoin(self, pseudonym_type = "HASH") :
        if pseudonym_type == "HASH" :
            sr_bloodtype, df_bloodtype_keyInfo = 1,2
        
        return sr_bloodtype, df_bloodtype_keyInfo

    def substituting(self) : 
        temp_bloodtype = []
        for element in self.df_bloodtype :
            if str(element) not in self.matching_table_dict.keys() : # 결측치 탐지
                print(self.matching_table_dict)
                print("outliar found")
                self.matching_table_dict[str(element)] = max(self.matching_table_dict.values()) + 1

            temp_bloodtype.append(self.matching_table_dict[str(element)])

        sr_bloodtype = pd.Series(temp_bloodtype)
        df_bloodtype_keyInfo = pd.DataFrame({'key' : list(self.matching_table_dict.keys()), 
                                        'value' : list(self.matching_table_dict.values())}, 
                                        index = range(len(self.matching_table_dict)))
        
        return sr_bloodtype, df_bloodtype_keyInfo
