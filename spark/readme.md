# QA
## spark python interceptor
> todo
## spark connect to elasticsearch
> spark连接elasticsearch的时候需要elasticsearch-hadoop的jar包
> 可以去官网下载对应的jar, 然后jar保存到`/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pyspark/jars`
> 
>
> 

PUT /my_index
{
 "settings": {
 "number_of_shards": 1,
 "number_of_replicas": 1
 },
 "mappings": {
 "properties": {
 "title": {
 "type": "text"
 },
 "content": {
 "type": "text"
 }
 }
 }
}







PUT /my_index/_doc/1
{
 "title": "The quick brown fox",
 "content": "The quick brown fox jumps over the lazy dog"
}



PUT /my_index/_doc/2
{
 "title": "journey to the west",
 "content": "Chinese story"
}


PUT /person
{
 "settings": {
 "number_of_shards": 1,
 "number_of_replicas": 1
 },
 "mappings": {
 "properties": {
 "name": {
 "type": "text"
 },
 "age": {
 "type": "integer"
 }
 }
 }
}


POST /person/_bulk
{"index":{"_id":"1"}}
{"name":"John Doe","age":30}
{"index":{"_id":"2"}}
{"name":"Jane Smith","age":25}
{"index":{"_id":"3"}}
{"name":"Bob Johnson","age":40}
{"index":{"_id":"4"}}
{"name":"Bob Johnson","age":22}
{"index":{"_id":"3"}}
{"name":"Allen Frank","age":28}
