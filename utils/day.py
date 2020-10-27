import pandas as pd

class DAY :
    def __init__(self, df_day, scale = 2) : 
        self.df_day = df_day
        self.scale = scale

        if self.scale == 2 :
            self.matching_table_dict = {
                '평일' : ['월', '화', '수', '목', '금'],
                '주말' : ['토', '일']
            }

    def categorizing(self) :
        temp_day = []
        
        for element in self.df_day :
            if element in self.matching_table_dict['평일'] : 
                temp_day.append('평일')
            elif element in self.matching_table_dict['주말'] : 
                temp_day.append('주말')
            else :
                temp_day.append('NULL')
            
        sr_day = pd.Series(temp_day)
        return sr_day
        
