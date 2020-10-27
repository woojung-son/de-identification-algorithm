import pandas as pd

class Name :
    def __init__(self, df_name) : 
        self.df_name = df_name

    def masking(self, masking_digit = 2) :
        #print(self.df_name)
        temp_name = []
        
        for element in self.df_name :
            #print('original name : ', element)
            element = element.replace(element[1:], "*" * (len(element) - 1))
            temp_name.append(element)
            

        sr_name = pd.Series(temp_name)
        return sr_name
        
