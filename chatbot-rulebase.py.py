#--------------------------------PROJECT 1 :CHATBOT ,SUBMIT:DECODELABS -----------------------------
def chatbot():
    #make dictionary 
    response={
        "hello": "hi there!,how i can help u?",
        "hi": "hey, welcome to decodelabs",
        "bye": "good bye,have nice day!",
        "help": "i am here for ur help,I can give u basic question answer.Try :hello ,bye,name,time. ",
        "name": "i am decodebot, Your rule based assistant!",
        "age": "i was just created,so i am just 0 day old",
        "thank": "you r welcome!",
    }
    print("decode labs: Hello type 'exit' to quiet. \n")
    #Infinite loop
    while True:
        #INPUT & SANITIZATION
        user_input=input('you: ').lower().strip()
        clean_input=user_input.lower().strip()
        #Exit startegy
        if clean_input=='exit':
            print("decodebot: goodbye!")
            break
        #dictionary loop+fallback using .get()
        reply=response.get(clean_input, "I don't understand that yet.")
        print(f"decodebot: {reply}\n")
chatbot()
#-------------------------------END--------------------------------------------------------