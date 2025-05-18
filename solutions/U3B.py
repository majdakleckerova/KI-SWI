def is_palindrom(s: str) -> bool:
    s_clean = s.replace(" ", "").lower()
    return s_clean == s_clean[::-1]