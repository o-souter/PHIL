# cm2110-coursework-2021-22-bean-team - P.H.I.L

###### By Adam Govier, Navya Shiju, Oliver Souter, Aida Ovalle

### What does P.H.I.L do - 

	The purpose of P.H.I.L is to monitor the inputs gathered by various sensors (microphones, temperature, panic button, humidity, movement, light) and process this data to allow an 
	appropriate response to be called upon, depending on the situation. It will alert selected family members/carers and emergency services so that in case of danger, aid can be 
	provided substantially faster which will minimise fatalities in a household. P.H.I.L can also change the display of the "face" to correspond to different situations which allows for
	more emotional engagement with the device.

### Why is P.H.I.L useful - 

	P.H.I.L is a beneficial piece of software as it provides aid and comfort to the vulnerable and elderly as they can be isolated memebers of society. If assistence is ever required,
	family members may live too far away to provide fast aid so P.H.I.L will meet this need and by doing so, minimise household fatalities. As a companion, P.H.I.L will provide news, a 
	comforting prescence in the user's home and alert them of the weather to allow them to plan their daily activities.

### Hardware Requirements - 
	During manufacture, the hardware that is required is:

	-Speakers
	-Microphone
	-Sense Hat
	-Monitor
	-Rasberry Pi 4  - encased in plastic when manufactured

### P.H.I.L Setup for Users- 

	Ideally, the system would be 'Plug and Play' but that is to be implemented for future versions. For now, the users will have to download a couple third party libaries/software before P.H.I.L can be put to use:

	-Pocketsphinx is an Open Source Toolkit used for Speech Recognition and it provides a Python interface. To download, simply open a new terminal when the P.H.I.L program is run and 
	type in the following command:
		`pip install --upgrade pocketsphinx`

	-eSpeak is a compact open source software speach synthesizer that allows text to speech commands to be implemented. To download, simply open a new terminal when the P.H.I.L program
	is run and type in the following commands consequetively:
		`pip3 install pyttsx3` `sudo apt install espeak` `pip3 install pyaudio`

	-Paho Python is a Python language client library, which can connect to MQTT Broker to publish messages and receive published messages. To download, simply open a new terminal when 
	the P.H.I.L program is run and type in the following command:
		`pip install paho-mqtt`

	The user will also have to run the bash file before running the Main file. This can be done by proceeding to the terminal and changing into the *lib* folder by the command `cd lib`.
	Once in the folder, run the command `bash start.sh`

	When the Gateway file is run, the system requires for the user to enter their name so that they can be addressed correctly when P.H.I.L is in use.
		
### Web/Cloud Services used by P.H.I.L - 

	An MQTT broker is a server that allows P.H.I.L to receives all messages/data from the MQTT "clients", which in this case is the other sensors used to collect data and then routes 
	the messages/data to the appropriate subscribing clients(or others nodes). If you visit (https://www.hivemq.com/public-mqtt-broker/) you can see details of the HiveMQ broker that 
	is in use:

		-Broker: broker.hivemq.com

### Additional Features - 

	For legal requirements, our data collected within the user's home is not stored after being processed. This allows us to comply with the GDPR principles and allow the user to rest assured that their information is not being sold for commericial purposes and is held within total confidentiality.

	P.H.I.L intelligently adapts its behaviour to respond to changes within its environement. It outputs the logged data in a message to the user, to confirm that the data has been receieved and processed. The software allows P.H.I.L to alert the user, not only with an audio signal but also with a visual representation that corresponds to the appropriate event.
	
