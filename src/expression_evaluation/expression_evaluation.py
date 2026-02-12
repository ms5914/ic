class ExpressionEvaluation:
    def __init__(self, expressions):
        self.adj_list = {}
        for expr in expressions:
            variable, rhs = expr.split("=")
            self.adj_list[variable] = rhs
        self.memo = {}
        self.visited = set()

    def evaluate(self, item):
        # 1. Base Case: If it's a number, return it
        if item.isdigit() or (item.startswith('-') and item[1:].isdigit()) or (item.startswith('+') and item[1:].isdigit()) :
            return int(item)

        # 2. Check Memoization
        if item in self.memo:
            return self.memo[item]

        # 3. Check for Cycles or Missing Variables
        if item in self.visited or item not in self.adj_list:
            return "IMPOSSIBLE"

        # 4. Process the Variable
        self.visited.add(item)
        rhs = self.adj_list[item]
        result = "IMPOSSIBLE"

        if "+" in rhs:
            parts = rhs.split("+")
            r1, r2 = self.evaluate(parts[0]), self.evaluate(parts[1])
            if r1 != "IMPOSSIBLE" and r2 != "IMPOSSIBLE":
                result = r1 + r2
        elif "-" in rhs:
            parts = rhs.split("-")
            r1, r2 = self.evaluate(parts[0]), self.evaluate(parts[1])
            if r1 != "IMPOSSIBLE" and r2 != "IMPOSSIBLE":
                result = r1 - r2
        else:
            # Direct reference (e.g., T3=T4)
            result = self.evaluate(rhs)

        # 5. Cleanup and Memoize
        self.visited.remove(item)
        self.memo[item] = result
        return result


# test_cases = [
#     {
#         "name": "Part 1: Basic Reference",
#         "target": "T3",
#         "exprs": ["T1=1", "T2=2", "T3=T4", "T4=T5", "T5=T2"],
#         "expected": 2
#     },
#     {
#         "name": "Part 2: Basic Operators",
#         "target": "T3",
#         "exprs": ["T1=1", "T2=2", "T3=T4+T5", "T4=T1", "T5=T2"],
#         "expected": 3
#     },
#     {
#         "name": "Part 2: Mixed Variable and Literal",
#         "target": "T1",
#         "exprs": ["T2=10", "T1=T2+5"],
#         "expected": 15
#     },
#     {
#         "name": "Part 3: Circular Dependency (Simple)",
#         "target": "T1",
#         "exprs": ["T1=T2", "T2=T1"],
#         "expected": "IMPOSSIBLE"
#     },
#     {
#         "name": "Part 3: Circular Dependency (Complex)",
#         "target": "T3",
#         "exprs": ["T1=1", "T2=2", "T3=T4+T5", "T4=T5", "T5=T4"],
#         "expected": "IMPOSSIBLE"
#     },
#     {
#         "name": "Edge Case: Diamond Dependency",
#         "target": "T4",
#         "exprs": ["T1=5", "T2=T1+2", "T3=T1+3", "T4=T2+T3"],
#         "expected": 15  # (5+2) + (5+3) = 15
#     },
#     {
#         "name": "Edge Case: Missing Definition",
#         "target": "T1",
#         "exprs": ["T1=T99+1"],
#         "expected": "IMPOSSIBLE"
#     }
# ]
#
# print(f"{'TEST NAME':<35} | {'RESULT':<12} | {'EXPECTED'}")
# print("-" * 65)
#
# for tc in test_cases:
#     solver = ExpressionEvaluation(tc["exprs"])
#     actual = solver.evaluate(tc["target"])
#
#     status = "✅ PASS" if actual == tc["expected"] else "❌ FAIL"
#     print(f"{tc['name']:<35} | {str(actual):<12} | {tc['expected']}")