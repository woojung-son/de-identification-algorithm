import pandas as pd
import hashlib
#from openpyxl import Workbook

class SSN :
    def __init__(self, df_ssn) : 
        self.df_ssn = df_ssn

    def masking(self, masking_digit = 13) :
        temp_name = []
        #write_wb = Workbook()
        
        for element in self.df_ssn :
            element = element.replace(element[1:], "*" * (len(element) - 1))
            temp_name.append(element)
            

        sr_name = pd.Series(temp_name)
        return sr_name

    def pseudonymization(self, pseudonym_type = "HASH") :
        if pseudonym_type == "HASH" :
            sr_ssn, df_ssn_keyInfo = self.hashing(self.df_ssn)
        
        return sr_ssn, df_ssn_keyInfo

    def hashing(self, df_ssn) :
        table_key = {}
        table_hash = {}
        temp_ssn = []
        
        for idx, element in enumerate(df_ssn) :
            data = element.encode()
            hash_object = hashlib.sha1()
            hash_object.update(data)
            hex_dig = hash_object.hexdigest()

            table_key[idx] = element
            table_hash[idx] = hex_dig

            temp_ssn.append(hex_dig)
        
        sr_ssn = pd.Series(temp_ssn)
        df_ssn_keyInfo = pd.DataFrame({'key' : list(table_hash.values()), 'value' : list(table_key.values())}, index = range(len(table_hash)))

        return sr_ssn, df_ssn_keyInfo

        
