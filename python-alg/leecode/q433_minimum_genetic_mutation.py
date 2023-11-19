from collections import deque


def minMutation(start, end, bank):
    if end not in bank:
        return -1

    valid_mutations = set(bank)
    queue = deque([(start, 0)])
    print(queue)

    while queue:
        curr, mutations = queue.popleft()

        if curr == end:
            return mutations

        for i in range(len(curr)):
            for char in "ACGT":
                mutation = curr[:i] + char + curr[i + 1 :]
                if mutation in valid_mutations:
                    valid_mutations.remove(mutation)
                    queue.append((mutation, mutations + 1))
    return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

print(minMutation(startGene, endGene, bank))
