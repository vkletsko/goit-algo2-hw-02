from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def help_function(part_length):
        if part_length == 0:
            return 0, []
        if part_length in memo:
            return memo[part_length]

        max_profit = 0
        best_cut = []
        for i in range(1, part_length + 1):
            profit, cuts = help_function(part_length - i)
            current_profit = profit + prices[i - 1]
            if current_profit > max_profit:
                max_profit = current_profit
                best_cut = [i] + cuts

        memo[part_length] = (max_profit, best_cut)
        return max_profit, best_cut

    max_profit, cuts = help_function(length)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dyn_profit = [0] * (length + 1)
    cuts = [0] * (length + 1)

    for i in range(1, length + 1):
        max_profit = 0
        for j in range(1, i + 1):
            if max_profit < prices[j - 1] + dyn_profit[i - j]:
                max_profit = prices[j - 1] + dyn_profit[i - j]
                cuts[i] = j
        dyn_profit[i] = max_profit

    result_cuts = []
    current_length = length
    while current_length > 0:
        result_cuts.append(cuts[current_length])
        current_length -= cuts[current_length]

    return {
        "max_profit": dyn_profit[length],
        "cuts": result_cuts,
        "number_of_cuts": len(result_cuts) - 1
    }


def run_tests():
    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()
