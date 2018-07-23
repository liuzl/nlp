import os.path
import sys
import json

try:
  import apiai
except ImportError:
  sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
  )
  import apiai

CLIENT_ACCESS_TOKEN = 'cdf8f736fd444a74ad76a54fb1d17dd9'


def main():
  ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

  print 'Which fruit do you like? Apple or Orange?'
  while True:
    query = sys.stdin.readline()
    request = ai.text_request()
    request.lang = 'en'
    request.resetContexts = True
    request.contexts.append("test")
    request.session_id = "test-id"
    request.query = query
    response = json.loads(request.getresponse().read())
    intent = response["result"]["metadata"]["intentName"]
    speech = response["result"]["fulfillment"]["speech"]
    print '[%s]' % intent
    if intent != 'Selection':
      print speech
    else:
      fruit = response["result"]["parameters"]["fruit"]
      if fruit != '':
        print response["result"]["fulfillment"]["speech"]
      else:
        print "Sorry I don't understand, which fruit do you like?"
    # print request.getresponse().read()


if __name__ == '__main__':
  main()
