# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#第一小题：
ICBC = {"stockcode": 601398, "field": "商业银行", "listingdate": "2006-10-27", "EPS": 0.82, "NPL": 1.52, "PCR": 175.76, "CAR": 15.39, "ROA": 1.11, "ROE": 13.79}
CCB = {"stockcode": 601939, "field": "商业银行", "listingdate": "2007-09-25", "EPS": 1., "NPL": 1.46, "PCR": 208.37, "CAR": 17.19, "ROA": 1.16, "ROE": 14.04}
BOC = {"stockcode": 601988, "field": "商业银行", "listingdate": "2006-07-05", "EPS": 0.59, "NPL": 1.42, "PCR": 181.97, "CAR": 14.97, "ROA": 0.94, "ROE": 12.06}
ABC = {"stockcode": 601288, "field": "商业银行", "listingdate": "2010-07-15", "EPS": 0.59, "NPL": 1.59, "PCR": 252.18, "CAR": 15.12, "ROA": 0.93, "ROE": 13.66}

#第二小题：
if ICBC["field"] == CCB["field"]:
    print("工商银行建设银行所处的行业一致")
else:
    print("工商银行建设银行所处的行业不一致")

if ICBC["listingdate"] == BOC["listingdate"]:
    print("工商银行与中国银行上市日期相同")
else:
    print("工商银行与中国银行上市日期不同")

#第三小题：
if CCB["EPS"] > ABC["EPS"]:
    print("建设银行的每股收益大于农业银行")
else:
    print("建设银行的每股收益不大于农业银行")

if ABC["NPL"] >= CCB["NPL"]:
    print("农业银行的不良贷款率大于等于建设银行")
else:
    print("农业银行的不良贷款率小于建设银行")
if ABC["PCR"] >= CCB["PCR"]:
    print("农业银行的拔备覆盖率大于等于建设银行")
else:
    print("农业银行的拔备覆盖率小于建设银行")

#第四小题：
if ICBC["CAR"] < ABC["CAR"]:
    print("工商银行的资本充足率小于农业银行")
else:
    print("工商银行的资本充足率大于等于农业银行")

if ICBC["ROA"] < CCB["ROA"]:
    print("工商银行的总资产率收益率小于建设银行")
else:
    print("工商银行的总资产率收益率大于等于建设银行")

if BOC["ROE"] <= CCB["ROE"]:
    print("中国银行的净资产收益率小于等于建设银行")
else:
    print("中国银行的净资产收益率大于建设银行")