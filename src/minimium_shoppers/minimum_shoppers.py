from typing import List, Optional
import heapq


class Solution:

    def evaluate_avg_waiting_time(self, orders, no_of_shoppers):
        waiting_time = 0

        free_shoppers = [(0, i) for i in range(no_of_shoppers)]
        waiting_time = 0

        for order in orders:
            duration, arrival_time = order[0], order[1]
            shopper_free_time, id = heapq.heappop(free_shoppers)
            waiting_time = waiting_time + (max(shopper_free_time, arrival_time) + duration - arrival_time)
            heapq.heappush(free_shoppers, (max(shopper_free_time, arrival_time) + duration, id))

        return waiting_time * 1.0 / len(orders)

    def getMinShoppers(self, orders: List[List[int]], k: float) -> int:
        # TODO: Implement getMinShoppers logic
        if len(orders) == 0:
            return 0
        orders.sort(key=lambda v: v[1])

        min_shoppers = 1
        max_shoppers = len(orders)
        result = -1

        while min_shoppers <= max_shoppers:
            no_of_shoppers = (min_shoppers + max_shoppers) // 2

            avg_waiting_time = self.evaluate_avg_waiting_time(orders, no_of_shoppers)

            if avg_waiting_time <= k:
                result = no_of_shoppers
                max_shoppers = no_of_shoppers - 1
            else:
                min_shoppers = no_of_shoppers + 1

        return result


