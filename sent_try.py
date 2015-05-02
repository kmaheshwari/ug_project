
from corenlp import *
import jsonrpc
from simplejson import loads
server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
                             jsonrpc.TransportTcpIp(addr=("127.0.0.1", 8080)))

result = loads(server.parse("Hello world.  It is so beautiful"))
print "Result", result
corenlp = StanfordCoreNLP()  # wait a few minutes...
print corenlp.parse("you is very good")
