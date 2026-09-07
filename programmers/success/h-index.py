# 2026-09-07


def solution(citations):
    citations.sort(reverse=True)
    for rank, citation in enumerate(citations, start=1):
        if citation < rank:
            return rank - 1

    return len(citations)
