# Scraping the following site:
# https://www.ncei.noaa.gov/pub/data/ghcn/daily/

import requests
import os
import pandas
from firebase import fireBasePushPandasDataFrame

def byYearScrape():
    for i in range(3, 24):
        fixed_i = i if i > 9 else f"0{i}"
        yearStr = f"https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_year/20{fixed_i}.csv.gz"
        print(yearStr)
        currDf = pandas.read_csv(yearStr, compression='gzip', header=0, sep=',', quotechar='"')
        """ Column info:
            ID = 11 character station identification code
            YEAR/MONTH/DAY = 8 character date in YYYYMMDD format (e.g. 19860529 = May 29, 1986)
            ELEMENT = 4 character indicator of element type 
            DATA VALUE = 5 character data value for ELEMENT 
            M-FLAG = 1 character Measurement Flag 
            Q-FLAG = 1 character Quality Flag 
            S-FLAG = 1 character Source Flag 
            OBS-TIME = 4-character time of observation in hour-minute format (i.e. 0700 =7:00 am)
        """
        currDf.columns = ["ID", "YEAR/MONTH/DAY", "ELEMENT", "DATA VALUE", "M-FLAG", "Q-FLAG", "S-FLAG", "OBS-TIME"]
        fireBasePushPandasDataFrame(currDf, f"ncei_20{fixed_i}")
