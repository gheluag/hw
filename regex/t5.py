from re import *

str_log="5.135.134.16GET 5.135.134.16GET 5.135.134.16POST 135.134.16POST 135.134.16POST 13.57.220.172GET13.57.220.172POST 13.57.220.172GET 13.57.220.172POST 13.57.220.17GET 13.57.220.172POST 13.57.220.172GET 13.57.220.172POST 13.57.220.172POST 13.57.233.99GET 18.206.226.75GET 18.206.226.75POST 18.213.10.181GET 18.213.10.181GET 18.213.10.181GET"
def find_log(str_log):
    lst = findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', str_log)
    counnt = {x: lst.count(x) for x in lst}
    return max(counnt.values())
print(find_log(str_log))

