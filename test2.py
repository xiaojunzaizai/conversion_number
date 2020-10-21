import re
import conversion
string = "123我123456abcdefgABCVDFF？/ ，。,.:;:''';'''[]{}()（）《》"
print(string)
# 123我123456abcdefgABCVDFF？/ ，。,.:;:''';'''[]{}()（）《》
sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",string)
print(sub_str)


def clean(n):
    c = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",n)
    return c
