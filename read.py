# reviews-analytics

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0: # %運算符號，是用來求餘數的，如果count/1000餘數為0時，
            print(len(data))  # 就印出來
print(len(data)) # 確認data清單長度
print(data[0])
print('--------------')
print(data[1])