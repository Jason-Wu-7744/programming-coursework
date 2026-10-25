# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import akshare as ak
sz50 = ak.index_stock_cons("000016")  # 最新 50 只代码
sz50.to_csv("sz50_codes.csv", index=False, encoding="utf-8")