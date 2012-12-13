#!/bin/sh
#
##################################################################
#
# 批量导入鼠须管词库
#
# author: bluffstone@gmail.com / zhifeng.kuang@alipay.com
# date: 2012-10-13
#################################################################

CELLS_DIR=cells
RIME_DIR=~/Library/Rime
TMP_TXT_DIR=$RIME_DIR/tmp_txts
IMPORT_TOOL=rime_dict_manager

# 复制词库导入工具
if [ ! -e $RIME_DIR/$IMPORT_TOOL ] ; then
	echo "复制词库导入工具"
	cp $IMPORT_TOOL $RIME_DIR/
fi

# 复制转化好的txt词库文件
rm -fr $TMP_TXT_DIR
mkdir $TMP_TXT_DIR
cp $CELLS_DIR/*.txt $TMP_TXT_DIR/

cd $RIME_DIR

# 批量把搜狗细胞词库转换为txt格式
for txt_file in `ls $TMP_TXT_DIR/*.txt`
do
	echo "开始导入词库：" $txt_file

	killall Squirrel
	$RIME_DIR/$IMPORT_TOOL -i luna_pinyin $txt_file

	echo "导入词库成功：" $txt_file 

done


# 删除临时的txt词库文件
rm -fr $TMP_TXT_DIR

