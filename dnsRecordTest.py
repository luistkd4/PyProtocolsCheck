import dns.resolver
import pymysql


class dnsRecordTest:
    __record = str()
    __dnstype = str()

    def getRecord(self, record, dnstype):
        self.record = record
        self.dnstype = dnstype
        result = []
        try:
            if dnstype == 'NS' or dnstype == 'ns' :
                answer = dns.resolver.query(record,dnstype)
                for data in answer: 
                    dnsresult = {
                        'Type':dnstype,
                        'Value':str(data)
                    }               
                    result.append(dnsresult)

            elif dnstype == 'MX' or dnstype == 'mx':
                answer = dns.resolver.query(record,dnstype)
                for data in answer:
                    dnsresult = {
                        'Type':dnstype,
                        'Weight':str(data).split(" ")[0],
                        'Value':str(data).split(" ")[1]
                    }              
                    result.append(dnsresult)

            elif dnstype == 'TXT' or dnstype == 'SPF' or dnstype == 'txt' or dnstype == 'spf':
                answer = dns.resolver.query(record,dnstype)
                for data in answer:
                    dnsresult = {
                        'Type':dnstype,
                        'Value':str(data)
                    }               
                    result.append(dnsresult)                    

            elif dnstype == 'PTR' or dnstype == 'ptr':
                answer = dns.resolver.query(record,dnstype)
                for data in answer:                    
                    dnsresult = {
                        'Type':dnstype,
                        'Value':str(data)
                    }               
                    result.append(dnsresult)
            else:
                return "Invalid type or record"             
        except dns.resolver.NoAnswer:
            return "No answer"
        except dns.resolver.NXDOMAIN:
            return "Can't find domain"
        except dns.resolver.NoMetaqueries:
            return "No queries"
        except dns.resolver.NoNameservers:
            return "Erro in our dns serevers"

        return result