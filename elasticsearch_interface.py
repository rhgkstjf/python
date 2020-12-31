import pathlib

from elasticsearch import Elasticsearch
import json


class ElaAPI:
    es = Elasticsearch(hosts="es_ip", port=es_port)  # 객체 생성

    def allIndex(cls):
        # Elasticsearch에 있는 모든 Index 조회
        print(cls.es.cat.indices())

    def search(cls, start, num):
        json_array = []
        # ===============
        # 데이터 조회 [전체]
        # ===============

        res = cls.es.search(
            index="logstash-log",
            body={
                "from": start,
                "size": start + 9999,
                "query": {"match_all": {}}
            }
        )
        data = json.dumps(res)
        data = json.loads(data)
        json_array = []
        for i in range(len(data["hits"]["hits"])):
            try:
                # print(json.dumps(data["hits"]["hits"][i]["_source"],indent="\t"))
                user = data["hits"]["hits"][i]["_source"]["user_agent"]
                os = data["hits"]["hits"][i]["_source"]["os"]
                clientip = data["hits"]["hits"][i]["_source"]["clientip"]
                timestamp = data["hits"]["hits"][i]["_source"]["timestamp"]
                geoip = data["hits"]["hits"][i]["_source"]["geoip"]
                request = data["hits"]["hits"][i]["_source"]["request"]
                message = data["hits"]["hits"][i]["_source"]["message"]
                body = {
                    "user_agent": user,
                    "os": os,
                    "clientip": clientip,
                    "timestamp": timestamp,
                    "geoip": geoip,
                    "request": request,
                    "message": message,
                }
                json_array.append(body)

            except KeyError:
                continue

        with open('json_file' + str(num) + '.json', 'a', encoding='utf-8') as make_file:
            for i in range(len(json_array)):
                json.dump(json_array[i], make_file)
                if i != len(json_array) - 1:
                    make_file.write(",\n")

    def createIndex(cls):
        cls.es.indices.create(
            index="logstash-bot",
            body={
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0
                },
                "mappings": {
                    "properties": {
                        "geoip": {
                            "properties": {
                                "city_name": {"type": "keyword"},
                                "country_code": {"type": "keyword"},
                                "country_code2": {"type": "keyword"},
                                "country_code3": {"type": "keyword"},
                                "country_name": {"type": "keyword"},
                                "dma_code": {"type": "keyword"},
                                "ip": {"type": "ip"},
                                "latitude": {"type": "float"},
                                "location": {"type": "geo_point"},
                                "longitude": {"type": "float"},
                                "postal_code": {"type": "keyword"},
                                "region_code": {"type": "keyword"},
                                "region_name": {"type": "keyword"},
                                "timezone": {"type": "keyword"}
                            }
                        },
                        "user_agent": {"type": "keyword"},
                        "os": {"type": "keyword"},
                        "bot": {"type": "keyword"}
                    }
                }
            }
        )

    def deleteIndex(cls, index_name):
        cls.es.indices.delete(index=index_name)

    def srvHealthCheck(cls):
        health = cls.es.cluster.health()
        print(health)

    def dataInsert(cls):
        data = []
        with open('botDF.json', 'r') as f:
            for line in f:
                data.append(json.loads(line))

        for i in range(len(data)):
            res = cls.es.index(index="logstash-bot", body=data[i], request_timeout=30)
            if i % 1000 == 0:
                print("1000개완료")

            # print(res)


es = ElaAPI()

es.allIndex()
#es.createIndex()
# es.deleteIndex("logstash-hacking-bot")
# es.deleteIndex("logstash-bot")
#es.dataInsert()
'''
k = 0
for i in range(400):
    if k % 99 == 0:
        k += 1
        print("100 만개 로그 처리 완료 -- ")
    elif k % 49 == 0:
        print("50만개 로그 처리 완료")
    else:
        print(str(i)+" 만번째 로그 처리 완료")
    es.search(i * 10000,k)
    '''
# es.search(0)
