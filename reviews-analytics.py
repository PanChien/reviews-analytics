data = []
count = 0

#開始檔案，並顯示讀取進度後，再顯示data內有幾筆資料
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  # count = count + 1
		if count % 1000 == 0:	#如果count除1000的餘數 等於 0
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

#計算留言的平均長度
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))


#留言長度小於100的有幾筆資料
new = []
for d in data:	#d是字串、data是清單
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

#留言有提到'good'的有幾筆
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])


# good = [1 for d in data if 'good' in d] #快寫法
# print(good)

# bad = ['bad' in d for d in data]	#快寫法
# print(bad)


# 文字計數
wc = {}    # 字典 word_count
for d in data:            #清單data
	words = d.split(' ')  #split()預設為空白鍵，將d分割後(又變成清單)再存入words
	for word in words:
		if word in wc:  #if word not in wc 否定用法
			wc[word] += 1 #找到wc用的key，value + 1
		else:
			wc[word] = 1  #新增新的key進wc字典


# 顯示 wc字點內，value超過100萬筆的字
for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])


#字典的長度
print('字典的長度：',len(wc))


# 查字功能
while True:
	word = input('請問你想查什麼字： ')
	if word == 'q':  #跳出迴圈
		break
	if word in wc:
		print(word, '出現過的次數為： ', wc[word])
	else:
		print('沒有出現這個字。')
print('感謝使用查尋功能。')

