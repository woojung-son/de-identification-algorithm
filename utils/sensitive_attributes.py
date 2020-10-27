import pandas as pd
import locale
import numpy as np
import datetime

class SA :
    def __init__(self, df_sa, exceptions = [], num_scale = -1, random_state = np.random.randint(100)) : 
        self.df_sa = df_sa
        self.exceptions = exceptions
        np.random.seed(random_state)
        start_num = np.random.randint(100)

        if exceptions :
            self.matching_table_dict = dict(zip(exceptions, np.random.choice([i for i in range(start_num, start_num + len(exceptions))], len(exceptions), replace=False)))

        if num_scale != -1 :
            if num_scale == 0 :
                self.num_scale = self.set_num_scale(num_scale)
            else :
                self.num_scale = num_scale
    
        #print('matching_table_dict : {}'.format(self.matching_table_dict))
        

    def categorizing(self) :
        temp_sa = []

        for element in self.df_sa :
            base_sa = int(element - (element % self.num_scale))

            #new_element = "[" + str(base_age) + " ~ " + str(base_age + self.num_scale - 1) + "]"
            
            locale.setlocale(locale.LC_ALL, 'en_US')
            new_element = locale.format_string("%d", base_sa, grouping=True, monetary=True)
            
            temp_sa.append(new_element)
            
        sr_sa = pd.Series(temp_sa)
        return sr_sa

    def categorizing_date(self, date_scale = 0) :
        temp_sa = []
        new_date_pd = pd.to_datetime(self.df_sa)
        new_date_pd = new_date_pd.dt.strftime('%Y-%m')
        '''
        for element in self.df_sa :
            print('element in categorizing_date : ', element)
            
            if date_scale == 0 :
                new_date_format = pd.to_datetime(element)

                tmp = pd.to_datetime(df['최종구매일자'])
                tmp = tmp.dt.strftime('%Y-%m')
                df['최종구매일자'] = tmp
                df['최종구매일자']

                new_date_format = datetime.datetime.strptime(element, '%Y-%m')
                print('thistime : ', element)

            temp_sa.append(new_date_format)
        '''
        print(type(new_date_pd))
        print(new_date_pd.head(10))
        sr_sa = pd.Series(new_date_pd)
        return sr_sa


    def pseudonymization(self, pseudonym_type = "Counter") :
        if pseudonym_type == "Counter" :
            sr_sa, df_sa_keyInfo = self.counter(self.df_sa)

        return sr_sa, df_sa_keyInfo

    def set_num_scale(self, num_scale) :
        #print(self.df_sa)
        max_digit = max([len(str(int(i))) for i in self.df_sa])
        return 10**(max_digit - 3)

    def counter(self, df_sa) :
        temp_sa = []
        
        for element in df_sa :
            new_element = element
            if element in self.exceptions :
                new_element = self.matching_table_dict[element]

            temp_sa.append(new_element)
        
        sr_sa = pd.Series(temp_sa)
        df_sa_keyInfo = pd.DataFrame({'key' : list(self.matching_table_dict.values()), 
                                    'value' : list(self.matching_table_dict.keys())}, 
                                    index = range(len(self.matching_table_dict.values())))
        return sr_sa, df_sa_keyInfo
