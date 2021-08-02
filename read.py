# reviews-analytics

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0: # %運算符號，是用來求餘數的，如果count/1000餘數為0時，
            print(len(data))  # 就印出來
# print(len(data)) # 確認data清單長度
# print(data[0]) # 印出data[0]的內容
# print('--------------')
# print(data[1]) # 印出data[1]的內容
print('檔案讀取完了，總共有', len(data), '筆資料。')


# 算出data[]的平半均長度
sum_len = 0
for d in data: # 使用for loop來分別確認每個資料的長度
    sum_len += len(d) # sum_len存入每行的長度
print('留言的平均長度為', sum_len/len(data)) # 算出平均長度