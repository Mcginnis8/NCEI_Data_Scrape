# NCEI_Data_Scrape
Data Scraping for National Centers for Environmental Information

# How to use:
1. get firebase credentials, place "cred_config.json" (firebase creds) file into top level
2. run desired functions from NCEI_Scrape.py in Main.py.

# NCEI_Scrape.py
Current Functions:
  byYearScrape()

# firebase.py
Current Functions:
  fireBaseInit() - get firebase auth
  fireBasePushTest(name: str) - test pushing a name to firebase
  fireBasePushPandasDataFrame(df, dataSetName: str) - push a dataframe to firebase



