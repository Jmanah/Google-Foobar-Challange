def solution(s):
    s = s.replace('-', '')
    return sum(s[:i].count('>') if s[i] == '<' else s[i:].count('<') for i in range(len(s)))

print(solution(">----<"))
print(solution("<<>><"))
