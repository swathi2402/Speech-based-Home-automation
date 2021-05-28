import os
from flask import Flask,render_template, request,json
import socket
import sys
#flask is justa microweb framework. We are using it to set up a client server architecture between js and python

app = Flask(__name__)
@app.route('/') #binding this url to default() function #decorator
def default():
    return 'Speech Based Home Automation System' 

@app.route('/voiceWebInterface')
def webInterface(): 
    return render_template('voiceWebInterface.html') #using jinja2 to render voiceWebInterface.html template at this url



@app.route('/voiceWebInterfacePost', methods=['POST'])
def webInterfacePost():
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #making a socket

	host = "192.168.43.214"
	port = 8888
	soc.connect((host, port))
    
	command =  request.form['command'] 
	#Flask request object contains the data that the client (eg a browser) has sent to your app - ie the URL parameters, any POST data
	message="mic:"+command
	#message we are sending to main server
	soc.sendall(message.encode("utf8"))
	#send message to main server
	reply=soc.recv(2048)
	#recieve message from server
	reply=reply.decode()
	return json.dumps({'status':'OK','command':command,'reply':reply,'amidoing':"amidgoingsomething"})
	#use json to send this data to the js file 
if __name__=="__main__":

		app.run("127.0.0.1","4200",debug=True)
