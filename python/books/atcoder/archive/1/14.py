"""
PAST1回目 F
問題
文字列 S が与えられる。これは、1 つ以上の単語を (間に空白などを挟まずに) 連結したものである。ここで、各単語は 2 文字以上であり、最初の文字と最後の文字のみが英大文字、それ以外の文字は全て英小文字である。

これらの単語を辞書順に並べ (大文字小文字の違いは無視する)、同様に連結して出力するプログラムを作成せよ。

例えば、S= FisHDoGCaTAAAaAAbCAC とする。これは FisH, DoG, CaT, AA, AaA, AbC, AC の 7 つの単語を連結したものである。これらを辞書順に並べると AA, AaA, AbC, AC, CaT, DoG, FisH となるため、AAAaAAbCACCaTDoGFisH と出力すればよい。
"""

def tokenize(s):
    tokens = []
    n = len(s)
    i = 0
    while i < n:
        j = i + 1
        while j < n and s[j].islower():
            j += 1
        tokens.append(s[i:j+1])
        i = j + 1


    return tokens


s = input()
tokens = tokenize(s)
tokens.sort(key=str.lower)
print("".join(tokens))
