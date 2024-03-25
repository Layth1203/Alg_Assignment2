import pygame

# Pygame mixer initialization
pygame.mixer.init()

# Load Sound
merge_sound = pygame.mixer.Sound('merge_audio.wav')

def merge(left, right):
    merged_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1
            merge_sound.play()  
            pygame.time.wait(int(merge_sound.get_length() * 1000))

    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    return merged_array

def merge_sort(product_id):
    if len(product_id) <= 1:
        return product_id


    mid = len(product_id) // 2
    L = merge_sort(product_id[:mid])
    R = merge_sort(product_id[mid:])


    merged = merge(L, R)
    print(f"Merge: {L} and {R} to get {merged}")
    return merged

# Tests the merge sort
product_id = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Product IDs:", product_id)
sorted_arr = merge_sort(product_id)
print("Sorted array:", sorted_arr)

pygame.time.delay(1000)

# Quit Pygame
pygame.quit()
