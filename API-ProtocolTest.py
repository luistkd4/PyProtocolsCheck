from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from protocolsTest import *
from dnsRecordTest import *
from blacklisLookup import *

app = Flask(__name__)
api = Api(app)


class Imap(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user")
        parser.add_argument("password")
        parser.add_argument("server")        
        args = parser.parse_args()

        imap = protocolsTest()
        imap = imap.imapTest(args["user"], args["password"], args["server"])

        return jsonify(
            email=args["user"],
            response=imap
        )

class Pop(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user")
        parser.add_argument("password")
        parser.add_argument("server")
        args = parser.parse_args()

        pop = protocolsTest()
        pop = pop.popTest(args["user"], args["password"], args["server"])

        return jsonify(
            email=args["user"],
            response=pop
        )

class Smtp(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user")
        parser.add_argument("password")
        parser.add_argument("recipient")
        parser.add_argument("server")
        args = parser.parse_args()

        smtp = protocolsTest()
        smtp = smtp.smtpTest(args["user"], args["password"], args["recipient"], args["server"])
        
        return jsonify(
            email_from=args["user"],
            email_to=args["recipeint"],
            response=smtp
        )

class Dns(Resource):
    def get(self, record, dnstype):
        dns = dnsRecordTest()
        dns = dns.getRecord(record,dnstype)
        return jsonify(dns)

class Blacklist(Resource):
    def get(self, record):
        blacklist = blacklistLookup()
        blacklist = blacklist.setLookupParam(record)
        return jsonify(blacklist)

api.add_resource(Imap, "/imap")
api.add_resource(Pop, "/pop")
api.add_resource(Smtp, "/smtp")
api.add_resource(Dns, "/dns/<string:record>/<string:dnstype>")
api.add_resource(Blacklist, "/blacklist/<string:record>")
#app.run(ssl_context='adhoc')
app.run(debug=True,host='0.0.0.0', port=80)
