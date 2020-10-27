import pandas as pd
import numpy as np

class TOKENIZE :
    def __init__(self, df_target, random_state = np.random.randint(100)) : 
        self.df_target = df_target
        np.random.seed(random_state)
        #self.matching_table_dict = np.random.choice([1,2], 2, replace=False)
        #print(self.matching_table)
        self.matching_table_dict = dict(zip(['F', 'T'], np.random.choice([1,2], 2, replace=False)))

    def pseudonymizatoin(self, pseudonym_type = "HASH") :
        if pseudonym_type == "HASH" :
            sr_ssn, df_ssn_keyInfo = 1,2
        
        return sr_ssn, df_ssn_keyInfo

    def substituting(self) : 
        temp_target = []
        for element in self.df_target :
            if str(element) not in self.matching_table_dict.keys() : # 결측치 탐지
                self.matching_table_dict[str(element)] = max(self.matching_table_dict.values()) + 1

            temp_target.append(self.matching_table_dict[element])

        sr_target = pd.Series(temp_target)
        df_target_keyInfo = pd.DataFrame({'key' : list(self.matching_table_dict.keys()), 
                                        'value' : list(self.matching_table_dict.values())}, 
                                        index = range(len(self.matching_table_dict)))
        return sr_target, df_target_keyInfo



        
