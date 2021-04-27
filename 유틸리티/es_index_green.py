import requests
import json

esHostName = es_ip
esPort = es_port
# X-Pack use
#auth = (id,pwd)
schema = "https"

rawResponse = requests.get("http://"+esHostName+":"+esPort+"/_cat/shards?h=index,state")

textResponse = rawResponse.text

#responseList[0]: arduino-2019-03-24          UNASSIGNED
#responseList[1]: arduino-2019-03-25          UNASSIGNED
#responseList[2]: arduino-2019-03-26          STARTED

responseList = textResponse.split('\n')

unassignedList = []   

for idxInfo in responseList:
        idxInfoList = idxInfo.split(" ") #쌩으로 일단 스페이스별로 분리한다
        idxName = idxInfoList[0] #일단 확실하게 첫 번째 원소는 무조건 인덱스의 >이름임

        #이름을 걸러냈으면 그 이름을 가진 인덱스의 상태가 UNASSIGNED 인지 판별해야함
        for state in idxInfoList:
                #어차피 공백이 수천지라 태반이 "" 일거고, 그러거나 말거나 인덱스 이름 뒤에 무조건
                #UNASSIGNED기만 하면 레플리카를 조정해야 하는 샤드니까 간단하게 문자열 비교
                if state == "UNASSIGNED":
                        unassignedList.append(idxName)
                        
unassignedList = list(set(unassignedList))

header = {"Content-Type":"application/json; charset=utf-8"}

for unassignedIdxName in unassignedList:
        workResponse = requests.put("http://"+esHostName+":"+esPort+"/"+unassignedIdxName+"/_settings", data=json.dumps({"number_of_replicas":0,"index.max_result_window":100000}), headers=header)
        print("idxName: "+unassignedIdxName+", result: "+workResponse.text) 
