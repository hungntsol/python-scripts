def solution(A):
    A_max = max(A)
    hash_set = [0]*A_max

    for i in range(0, len(A)):
        if A[i] <= 0:
            continue
        hash_set[A[i] - 1] += 1

    for i in range(0, len(hash_set)):
        if hash_set[i] == 0:
            return i + 1


if __name__ == "__main__":
    A = [1, 3, 7, 5, 6, 2]
    print(solution(A))
