stroka = "artr,aytsuyats,asyas,disd,osid"
list = stroka.split(",")
print(list)

for i in range(len(list)):
    if(list[i][:1]=="a"):
        print(list[i])

array = ["sd","dsds","sdsds"]
string2 = ",".join(array)
print(string2)


def Split(data):
    result = 0
    list = data.split(',')
    for i in range(len(list)):
        result += int(list[i])
    return result//len(list)