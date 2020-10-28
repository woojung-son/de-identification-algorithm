import pandas as pd
import locale
import numpy as np
import datetime

class DROP :
    def __init__(self, df_drop) : 
        self.df_drop = df_drop
        
    def drop(self, df_drop) :
        temp_drop = []
        
        for element in df_drop :
            new_element = ""

            temp_drop.append(new_element)
        
        sr_drop = pd.Series(temp_drop)
        return sr_drop
    

