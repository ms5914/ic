from typing import List, Optional
from collections import defaultdict

class DataWarehouse:
    def __init__(self, data: List[List[str]]):
        self.data = data
        self.column_index_map = dict()
        for i, col_name in enumerate(self.data[0]):
            self.column_index_map[col_name] = i


    def getMostProfitable(self, column: str, startDate: str) -> str:
        profit_map = defaultdict(int)
        max_profit = -float("inf")
        pivot_value = None
        for row in self.data[1:]:
            if row[self.column_index_map["date"]] >= startDate:
                if column in self.column_index_map:
                    profit_map[row[self.column_index_map[column]]]+=(int(row[self.column_index_map["sell_price"]])-int(row[self.column_index_map["cost"]]))
                else:
                    return ""
        for key in sorted(profit_map.keys()):
            if profit_map[key] > max_profit:
                pivot_value = key
                max_profit = profit_map[key]

        return pivot_value if pivot_value else ""

    # ["DataWarehouse", "getMostProfitable", "getMostProfitable", "getMostProfitable"]
    # [[[["order_id", "cost", "sell_price", "product", "date", "category"],
    #    ["200", "10", "20", "laptop", "2024-06-01", "electronics"],
    #    ["201", "5", "15", "mouse", "2024-06-01", "accessories"],
    #    ["202", "15", "25", "keyboard", "2024-06-02", "accessories"],
    #    ["203", "20", "30", "monitor", "2024-06-02", "electronics"],
    #    ["204", "8", "12", "cable", "2024-06-03", "accessories"],
    #    ["205", "25", "29", "tablet", "2024-06-03", "electronics"]]], ["product", "2024-06-01"],
    #  ["category", "2024-06-01"], ["category", "2024-06-03"]]