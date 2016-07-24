rm -rf data
echo "-----Make Data make_data.py----"
python make_data.py


rm -rf out_data*

echo "-----Single Threaded json_mapper.py----"
mkdir out_data1
time cat data/* | python json_mapper.py > out_data1/out.json
echo "-----Single Threaded json_mapper.py----"

echo "-----Parallel json_mapper.py----"
mkdir out_data
time find data/* | parallel 'cat {} | python json_mapper.py > out_data/file_{#}.json'
echo "-----Parallel json_mapper.py----"

echo "-----Single Threaded Luigi----"
time luigi --module luigi_multiprocess LotsOTasks --local-scheduler
rm -rf out_data2/
echo "-----Single Threaded Luigi----"

echo "-----4-worker Luigi----"
time luigi --module luigi_multiprocess LotsOTasks --workers 4
echo "-----4-worker Luigi----"

echo "-----Pyspark----"
time python pyspark_mapper.py
echo "-----Pyspark----"

echo "-----Pyspark Luigi----"
time luigi --module luigi_pyspark TestTaskPS --local-scheduler
echo "-----Pyspark Luigi----"

echo "-----Luigi Hadoop----"
time luigi --module luigi_hadoop TestTaskMR --local-scheduler
echo "-----Luigi Hadoop----"

echo "-----jq----"
mkdir out_data4
time cat data/* | jq -c -f map.jq > out_data4/out.json
echo "-----jq----"

echo "-----jq parallel----"
mkdir out_data5
time cat data/* | parallel --pipe 'jq -c -f map.jq > out_data5/file_{#}.json'
echo "-----jq parallel----"
