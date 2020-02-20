import sqlite3
import pandas as pd

timeframes = ['2008-07']

for timeframe in timeframes:
	connection = sqlite3.connect('{}.db'.format(timeframe))
	c = connection.cursor()
	limit = 5000
	last_unix = 0
	cur_length = limit
	counter = 0
	test_done = False

	while True:
		df = pd.read_sql("select * from parent_reply where unix>{} and parent not null and score>0 order by unix asc limit {}".format(last_unix,limit),connection)
		if len(df) == 0: break
		last_unix = df.tail(1)['unix'].values[0]
		if not test_done:
			with open("test.from","a",encoding="utf8") as f:
				for content in df["parent"].values:
					f.write(content+"\n")
			with open("test.to","a",encoding="utf8") as f:
				for content in df["comment"].values:
					f.write(content+"\n")
			test_done = True
		else:
			with open("train.from","a",encoding="utf8") as f:
				for content in df["parent"].values:
					f.write(content+"\n")
			with open("train.to","a",encoding="utf8") as f:
				for content in df["comment"].values:
					f.write(content+"\n")

		counter += 1
		print(counter*limit," rows completed")			
