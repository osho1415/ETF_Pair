import itertools
import statsmodels.api as sm
import pandas as pd 
import numpy as np 

ETF_PATH = "./data/ETF.xlsx"
FED_FUND_PATH = "./data/DFF.xlsx"
BORROW_PATH = "./data/BORROW_RATE.xlsx"
VIX_PATH = "./data/VIXCLS.xlsx"

IN_SAMPLE_BEGIN = '2012-08-07'

OUT_SAMPLE_BEGIN = '2023-08-07'

OUT_SAMPLE_END = '2025-08-08'

# In sample testing parameters
HOLDING_PERIOD = [21,63,84,126]
LOOKBACK_WINDOW = [21, 63, 126, 252]
ERROR_PCT = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.5]
VIX_WEIGHT = [1, 1.25, 1.5]


PARAMETER_GRID = list(itertools.product(
    HOLDING_PERIOD, 
    LOOKBACK_WINDOW, 
    ERROR_PCT,  
    VIX_WEIGHT
))

in_sample_results = []
return_series_dict = {}


# This gives the list of underlying and their related Tickers 
SPEC = {
    "Silver":        {"underlying": "SLV", "long": "AGQ", "short": "ZSL", "others": []},
    "Gold":          {"underlying": "GLD", "long": "UGL", "short": "GLL", "others": []},
    "Natural Gas":   {"underlying": "UNG", "long": "BOIL","short": "KOLD","others": []},
    "Oil":           {"underlying": "USO", "long": "UCO", "short": "SCO", "others": []},
    "Euro":          {"underlying": "FXE", "long": "ULE", "short": "EUO", "others": []},
    "Japanese Yen":  {"underlying": "FXY", "long": "YCL", "short": "YCS", "others": []},
    "Nasdaq-100":    {"underlying": "QQQ", "long": "QLD", "short": "QID", "others": ["PSQ"]},
    "S&P 500":       {"underlying": "SPY", "long": "SSO", "short": "SDS", "others": ["SH"]},
    "US 20+ Year Treasuries": {"underlying": "TLT", "long": "UBT","short": "TBT","others": ["TBF"]},
    }



