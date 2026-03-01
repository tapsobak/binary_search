def binary_search(sorted_list, target):
    lowest_index = 0
    highest_index = len(sorted_list) - 1
    while lowest_index <= highest_index:
        mid_index = (highest_index + lowest_index) // 2
        if sorted_list[mid_index] == target:
            return f"target: {target} - index: {mid_index}"
        else:
            if sorted_list[mid_index] < target:
                lowest_index = mid_index + 1

            else:
                highest_index = mid_index - 1

    return f"target: {target} - index: -1"


if __name__ == "__main__":
    print(binary_search([12, 15, 22, 31, 45, 58, 63, 71, 89, 94], 12))
    print(binary_search([12, 15, 22, 31, 45, 58, 63, 71, 89, 94], 58))
    print(binary_search([12, 15, 22, 31, 45, 58, 63, 71, 89, 94], 94))
    print(binary_search([12, 15, 22, 31, 45, 58, 63, 71, 89, 94], 2))
    print(binary_search([], 2))
    print(binary_search([1], -4))
