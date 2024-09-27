def shuffle(cards):
    n = len(cards) // 2  # Calculate n
    first_half = cards[:n]  # Get the first half
    second_half = cards[n:]  # Get the second half
    shuffled = []

    # Interleave the two halves
    for i in range(n):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])

    return shuffled

# Example Usage
cards1 = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards1))  # Output: ['Joker', 3, 'Queen', 'Ace', 2, 7]

cards2 = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards2))  # Output: [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]

cards3 = [10, 10, 2, 2]
print(shuffle(cards3))  # Output: [10, 2, 10, 2]
