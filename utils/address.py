import pandas as pd
import re

class ADDRESS :
    def __init__(self, df_address, addr_type = "지번") : 
        self.df_address = df_address
        self.addr_type = addr_type

    def categorizing(self) :
        #land_addr_form = "([가-힣]{2,}도[ ]?)?([가-힣]{1,}시[ ]?)?([가-힣]{1,}군[ ]?)?([가-힣]{1,}구[ ]?)?([가-힣]{1,}읍[ ]?)?([가-힣]{1,}면[ ]?)?([가-힣]{1,}동[ ]?)?([가-힣]{1,}리[ ]?)?"
        land_addr_form = "([가-힣]{2,}도[ ]?)?([가-힣]{1,}시[ ]?)?([가-힣]{1,}군[ ]?)?([가-힣]{1,}구[ ]?)?([가-힣]{1,}(읍|면)[ ]?)?([가-힣][가-힣1-9]*(동|리)[ ]?)?"
        road_addr_form = "([가-힣]{2,}도[ ]?)?([가-힣]{1,}시[ ]?)?([가-힣]{1,}군[ ]?)?([가-힣]{1,}구[ ]?)?([가-힣]{1,}(읍|면)[ ]?)?([가-힣0-9]+(로|길)[ ]?){1,3}"

        addr_regex = re.compile(land_addr_form) if (self.addr_type == "지번") else re.compile(road_addr_form)
        temp_addr = []

        # 도로명주소는 '동', '리'를 표기하지 않음.
        #si_exceptions = ["시흥시"] # 군산시, 군포시 , ... 
        #gun_exceptions = ["완도군", "청도군", "진도군"] # 동천동 # 완도군, 청도군, 진도군 
        #gu_exceptions = ["구로구"]
        #dong_exceptions = ["동천동", "성동동"] # 목동, 번동, 동천동 ... 장전1동, ... 
        #li_exceptions = ["오류1리"]
        # 구 밑에도 '읍'이 올 수 있음. e.g. 창원시 의창구 동읍 .. 
        # 시 밑에도 '군'이 올 수 있음. e.g. 부산광역시 기장군 기장읍 ... 
        # 동 아래에는 '리'가 없으며, 대신 '통'이 있다.

        # (알고리즘1) '동' 만 들어가는걸 찾아서 split한 다음, 그 앞에까만 취하는 방법 
        #  -> 동천동과 같이 '동'이 두번 들어가면 '경상북도 경주시 동' 까지만 될 수 있다.
        # (알고리즘2) 공백 단위로 split해서 앞에서 몇번째까지만 취하는 방법 
        # -> 경상북도 경주시 현곡면 이라고 적을 수도 있지만, 경주시 현곡면 섭들1길 이라고 적을 수도 있고, 경주시 현곡면 섭들 1길 이라고 적을 수도 있다.
        # (알고리즘3) '시', '군', '구', '읍', '면', '동' 이 들어가는 단어를 각각 찾아서, '시', '구', .. 정보를 따로 뽑아냈다가, 나중에 한꺼번에 조합한다.
        # -> 
        # (알고리즘4) '동' 이 들어가는 횟수를 세서 1개이면 그 앞까지 split한다. 
        # -> 두개 이상이면 어떡하지 ?
        
        for element in self.df_address :
            match_arr = addr_regex.search(element) # 경상북도, 동천동 과 같이 단일 구역 단위만 매칭되는 것을 막기 위해 시 or 군은 꼭 들어가게 만들자 !! 
            match_string = match_arr.group()

            temp_addr.append(match_string)
        
        sr_addr = pd.Series(temp_addr)
        return sr_addr
        
