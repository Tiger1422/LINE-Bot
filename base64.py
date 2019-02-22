
import sys
import json

# 1文字が8バイトで表される
BYTE_SIZE = 8

# 文字列textをバイナリの文字列に変換する
def str2bin(s):
    binStr = ""

    #ord関数で文字をASCIIコードへ変換し、
    #シフト演算で各桁のビットを取り出す
    for c in s:
        for i in range(BYTE_SIZE):
            binStr += str((ord(c) >> (BYTE_SIZE - (i + 1))) & 1)
    return binStr

# 文字列sを文字数nで分割したリストを返す
# (例)
# split("abcdef", 2) => [["ab"], ["cd"], ["ef"]]
def split(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]


# 文字列sを文字数nで分割した時に足りない部分を文字cで埋める
# (例)
# fillInBlank("abcd", 6, "=") => "abcd=="
def fillInBlank(s, n, c):
    mod = len(s) % n

    # 割り切れた場合は何も処理をしない
    if mod == 0: return s 

    # 割り切れなかった場合、残りの部分を埋める
    margin = n - mod
    return s + c * margin

# main関数         
def main():

    # コマンドの引数を受け取る
    argvs = sys.argv
    argc = len(argvs)

    # 引数が1つじゃなかったら無かったら、処理をせず終了
    if argc != 2:
        print "Usage:\n$ python %s CONVERT_STRING" % argvs[0]
        quit()

    # 1. 文字列をバイナリ文字列に変換
    binStr = str2bin(argvs[1])

    # 2. バイナリを6ビットづつに分割
    splitCount  =6
    s = split(binStr, splitCount)

    # 最後の2ビットが余るので,6ビットになるように0を追加する
    s[-1] = fillInBlank(s[-1], 6, "0")

    # 変換表の辞書を読み込み
    tableFile = open("base64_table.json", "r")
    base64Dict = json.loads(tableFile.read())

    result = ""

    for i in s:
        result += base64Dict[i]

    print result

    print fillInBlank(result, 4, "=")

if __name__ == '__main__':
    main()