import math


def binary_search(sorted_list, target):
    lowest_index = 0
    highest_index = len(sorted_list) - 0
    while lowest_index <= highest_index:
        mid_index = (highest_index + lowest_index) / 2
        mid_index = math.floor(mid_index)  # round mid to the lower integer
        if sorted_list[mid_index] == target:
            return mid_index
        else:
            if sorted_list[mid_index] < target:
                lowest_index = mid_index + 1
                mid_index = (highest_index + lowest_index) / 2
                mid_index = math.floor(mid_index)  # round mid to the lower integer
                if sorted_list[mid_index] == target:
                    return mid_index
            else:
                highest_index = mid_index - 1
                mid_index = (highest_index + lowest_index) / 2
                mid_index = math.floor(mid_index)  # round mid to the lower integer
                if sorted_list[mid_index] == target:
                    return mid_index

    return -1


if __name__ == "__main__":
    print(binary_search([12, 15, 22, 31, 45, 58, 63, 71, 89, 94], 5))
