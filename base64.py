
import sys
import json

# 1������8�o�C�g�ŕ\�����
BYTE_SIZE = 8

# ������text���o�C�i���̕�����ɕϊ�����
def str2bin(s):
    binStr = ""

    #ord�֐��ŕ�����ASCII�R�[�h�֕ϊ����A
    #�V�t�g���Z�Ŋe���̃r�b�g�����o��
    for c in s:
        for i in range(BYTE_SIZE):
            binStr += str((ord(c) >> (BYTE_SIZE - (i + 1))) & 1)
    return binStr

# ������s�𕶎���n�ŕ����������X�g��Ԃ�
# (��)
# split("abcdef", 2) => [["ab"], ["cd"], ["ef"]]
def split(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]


# ������s�𕶎���n�ŕ����������ɑ���Ȃ������𕶎�c�Ŗ��߂�
# (��)
# fillInBlank("abcd", 6, "=") => "abcd=="
def fillInBlank(s, n, c):
    mod = len(s) % n

    # ����؂ꂽ�ꍇ�͉������������Ȃ�
    if mod == 0: return s 

    # ����؂�Ȃ������ꍇ�A�c��̕����𖄂߂�
    margin = n - mod
    return s + c * margin

# main�֐�         
def main():

    # �R�}���h�̈������󂯎��
    argvs = sys.argv
    argc = len(argvs)

    # ������1����Ȃ������疳��������A�����������I��
    if argc != 2:
        print "Usage:\n$ python %s CONVERT_STRING" % argvs[0]
        quit()

    # 1. ��������o�C�i��������ɕϊ�
    binStr = str2bin(argvs[1])

    # 2. �o�C�i����6�r�b�g�Âɕ���
    splitCount  =6
    s = split(binStr, splitCount)

    # �Ō��2�r�b�g���]��̂�,6�r�b�g�ɂȂ�悤��0��ǉ�����
    s[-1] = fillInBlank(s[-1], 6, "0")

    # �ϊ��\�̎�����ǂݍ���
    tableFile = open("base64_table.json", "r")
    base64Dict = json.loads(tableFile.read())

    result = ""

    for i in s:
        result += base64Dict[i]

    print result

    print fillInBlank(result, 4, "=")

if __name__ == '__main__':
    main()