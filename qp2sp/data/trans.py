#!/usr/bin/python

#忠哲专用词库转换脚本

import struct

files = ['wbx.txt'];


data={};
count=0;

for db in files:
	file = open(db, 'r',encoding='utf-8');
	for lines in file:
		column = lines.split();
		
		if len(column[0])!=0 :
			if column[0] in data :
				data[column[0]].append(column[1]);
			else:
				data[column[0]]=[];
				data[column[0]].append(column[1]);
			count+=1;
			if count%1000==0 :
				print(count//1000);
			
	file.close();

keyfile = [open('a.sky', 'wb'),open('b.sky', 'wb'),open('c.sky', 'wb'),open('d.sky', 'wb'),open('e.sky', 'wb'),open('f.sky', 'wb'),open('g.sky', 'wb'),open('h.sky', 'wb'),open('i.sky', 'wb'),open('j.sky', 'wb'),open('k.sky', 'wb'),open('l.sky', 'wb'),open('m.sky', 'wb'),open('n.sky', 'wb'),open('o.sky', 'wb'),open('p.sky', 'wb'),open('q.sky', 'wb'),open('r.sky', 'wb'),open('s.sky', 'wb'),open('t.sky', 'wb'),open('u.sky', 'wb'),open('v.sky', 'wb'),open('w.sky', 'wb'),open('x.sky', 'wb'),open('y.sky', 'wb'),open('z.sky', 'wb')];
wordfile = open('words.dbz', 'wb');


# key file structure:
# [4bytes] keyStringChunkLength
# [*bytes] actual keyStringChunk ( 4 bytes align needed )
# [4bytes] keys count
# 	[4bytes] pointer to keyString, (the offset of keyStringChunk)
#	[4bytes] pointer to wordString, (the offset of word file, positive value for system db, negative value for user db)
#	loop the above two lines

# word file structure:
#	words are organized by groups. eg. for pinyin 'zhong', the word group contains '中忠钟……'
# 	groups are placed one by one
# 	a single group's structure is like below:
# 	[*bytes] actual CN words, utf-8 encoded, \0 terminated
# 	[4bytes] used count of this word, for dynamic sorting
# 	repeat the above two lines for every CN word of this group
#   [1byte] a '\ff' termination means the ending of this words group
#	repeat the above four lines for a new group

#prepare to write keyFile and actually write word file
keyStringChunks = [b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b''];
keyValues = [b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b'',b''];
keyCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
for key in sorted(data.keys()) :
	index=ord(key[0:1])-ord('a');
	keyString=key.encode('utf-8');
	keyValues[index]+=struct.pack('I',len(keyStringChunks[index]))+struct.pack('I',wordfile.tell());
	keyCount[index]+=1;
	keyStringChunks[index]+=struct.pack(str(len(keyString))+'s', keyString)+struct.pack('B',0);
	#write to word file
	for i in data[key]:
		b = i.encode('utf-8');
		wordfile.write(struct.pack(str(len(b))+'s', b)+struct.pack('B',0));#the CN word
		wordfile.write(struct.pack('I', 0));#the use count
	wordfile.write(struct.pack('B',255));#the terminator
	
wordfile.close();
#actually write keyFile
serial=0;
for f in keyfile :
	lengthOfChunk = len(keyStringChunks[serial]);
#for 4 byte align
	mod = lengthOfChunk % 4;
	if mod!=0 :
		mod = 4-mod;
	lengthOfChunk+=mod;
	
	f.write(struct.pack('I', lengthOfChunk));#keyStringChunkLength
	f.write(keyStringChunks[serial]);#keyStringChunk
#for 4 byte align
	for i in range(0,mod):
		f.write(struct.pack('B',0));
		
	f.write(struct.pack('I',keyCount[serial]));#keyCount
	f.write(keyValues[serial]);#keyValues
	f.close();
	serial+=1;
	


