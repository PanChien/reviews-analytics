# reviews-analytics
# 留言分析

# 讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0: # %運算符號，是用來求餘數的，如果count/1000餘數為0時，
            print(len(data))  # 就印出來
print('檔案讀取完了，總共有', len(data), '筆資料。')



# 文字計數
word_count = {} # 作成字典
for d in data: 
    words = d.split() # .split(' ')將每個字分開，並用單清的型式存放，如果不輸入值時，預設為空白鍵且不會將多個space再分切
    for word in words:
        if word in word_count: # 如果word在word_count裡，
            word_count[word] += 1
        else:
            word_count[word] = 1 # 新增key裡wrod_count字典

for word in word_count: # 當字典用for loop迴圈讀取時，只會提取key，value不會被拿出來
    if word_count[word] > 1000000:
        print(word, '： ', word_count[word]) # 印出word、再去word_count[word]字典來查次數

print(len(word_count)) # 印出字典的長度


# 文字查詢功能
while True:
    word = input('請問你想查什麼字： ')
    if word == 'q':
        break
    elif word in word_count:
        print(word, '出現過的次數為：',word_count[word])
    else:
        print(word, '沒有出現過。')
print('感謝使用本查詢功能。')

# # 算出data[]的平半均長度
sum_len = 0
for d in data: # 使用for loop來分別確認每個資料的長度
    sum_len += len(d) # sum_len存入每行的長度
print('留言的平均長度為', sum_len/len(data)) # 算出平均長度


# # 清單篩選，篩選留言小於100的數目
new = []
for d in data: # for loop一筆一筆將data[]中的清的拿出來
    if len(d) < 100: # 如果d的長度小於100時，
        new.append(d) # 將d存入new[]清單裡
print('一共有', len(new), '筆留言長度小於100。')
print(new[0])
print(new[1])


# 篩選留言有good文字的留言
good = []
for d in data:
    if 'good' in d: # 如果'good'有在d裡面
        good.append(d)
print('一共有', len(good), '筆留言提到good。')
print(good[0]) # 印出第一個清單



good_01 = [d for d in data if 'good' in d] # 篩選留言有good文字的留言的快寫法，list comprehension (清單快寫法)
print('進階寫法：一共有', len(good_01), '筆留言提到good。')
print(good_01[0])


bad = ['bad' in d for d in data] # 'bad' in d 是判別式，結果為true/false
print(bad[0]) # 看看清單的內容
print(bad[1]) # 是true/false


