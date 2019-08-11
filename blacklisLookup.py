import pymysql
import threading
import dns.resolver
import queue

client = pymongo.MongoClient("mongodb://")
db = client.sysMonitor
col = db.blacklists
blacklists = []
for obj in col.find():
 blacklists.append(obj['dns'])

class blacklistLookup:
    __record = str()

    def getLookup(self, ip, blacklist):
        self.ip = ip
        self.blacklist = blacklist
        myIP = ip
        bl = blacklist
        result=[]
        try:
            query = '.'.join(reversed(str(myIP).split("."))) + "." + bl
            answer = dns.resolver.query(query, "A")
            answer_txt = dns.resolver.query(query, "TXT")
            result.append(myIP+":"+bl+":LISTED")                   
        except dns.resolver.NXDOMAIN:
            result.append(myIP+":"+bl+":NOT LISTED")
        except dns.resolver.NoAnswer:
            result.append(myIP+":"+bl+":NO ANSWER")
        return result

    def setAnswerJsonFormat(self, lookupresult):
        self.lookupresult = lookupresult
        jsonAnswer = []
        for res in lookupresult:
            bresult = {
                'IP':res.split(":")[0].replace("['",""),
                'BLACKLIST':res.split(":")[1],
                'STATUS':res.split(":")[2].replace("']","")
            }
            jsonAnswer.append(bresult)
        return jsonAnswer

    def setLookupParam(self, record):
        self.record = record
        record = record
        threads = []
        my_queue = queue.Queue()
        blresult = []
        for bl in blacklists:
            bl = str(bl).replace("('","").replace("',)","")
            process = threading.Thread(target=my_queue.put(self.getLookup(record, bl)))
            threads.append(process)
            process.start()
            process.join()
        while not my_queue.empty():
            blresult.append(str(my_queue.get()))
        return self.setAnswerJsonFormat(blresult)