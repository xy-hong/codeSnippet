# https://blog.nowcoder.net/n/7fc67fe568c04937b37f36da9f57d33e?from=nowcoder_improve

def max_score(cards: list) -> int:
    i = 0
    score = 0
    round_scores = [0] * len(cards)
    while i < len(cards):
        card_score = cards[i]
        last_3_score = 0 if i < 3 else round_scores[i-3]
        if card_score + score >= last_3_score:
            score += card_score
            round_scores[i] = score
        else:
            score = last_3_score
            round_scores[i] = score
        i += 1
    
    return score

assert max_score([1,-5,-6,4,3,6,-2]) == 11
assert max_score([1, 2]) == 3 
assert max_score([0, 0, 0, 0]) == 0

        
