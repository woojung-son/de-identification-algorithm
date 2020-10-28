import pandas as pd

class AGE :
    def __init__(self, df_age, scale = 10) : 
        self.df_age = df_age
        self.scale = scale

    def categorizing(self) :
        temp_age = []
        
        for element in self.df_age :
            base_age = int(element - (element % self.scale))

            if self.scale == 10 :
                if base_age >= 70 :
                    new_element = "[70,100)"
                else : # base_age < 70
                    new_element = str(base_age) + "대"
            else :
                new_element = "[" + str(base_age) + "," + str(base_age + self.scale) + ")"

            temp_age.append(new_element)
            
        sr_age = pd.Series(temp_age)
        return sr_age
        
