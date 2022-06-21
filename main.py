import os
import openai
import pyttsx3

openai.api_key = os.getenv("OPENAI_ENV_KEY")

print("\n")
print("Welcome to Interface for interacting with an Artificial Intelligence")
print("\n")
print("You can ask me questions about the weather, or you can say 'quit' to exit.\n\n")

while True:
	question = input("»")	
	if question == "quit":
		break
	else:
		response = openai.Completion.create(
		model="text-davinci-002",
		prompt="»:{text}\nAI:".format(text=question),
		temperature=0.9,
		max_tokens=150,
		top_p=1,
		frequency_penalty=0.0,
		presence_penalty=0.6,
		stop=["»:", "AI:"]
		).choices[0].text

		print("»", response)
		engine = pyttsx3.init()
		engine.setProperty('voice', 'english_rp+f3') #my preference
		#print("Generating text-to-speach...")
		engine.say(response)
		engine.runAndWait()



