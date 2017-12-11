#!/bin/bash
INPUT=access.log
INPUT_DIR=/input
OUTPUT=result.dat
OUTPUT_DIR=/output
hdfs dfs -rm -r /input
hdfs dfs -mkdir /input
hdfs dfs -put $INPUT $INPUT_DIR
#hdfs dfs -put file2 $INPUT_DIR
hdfs dfs -rm -r -f $OUTPUT_DIR
hadoop jar wc.jar LogCountsPerHour $INPUT_DIR $OUTPUT_DIR
hdfs dfs -cat $OUTPUT_DIR/part* > $OUTPUT