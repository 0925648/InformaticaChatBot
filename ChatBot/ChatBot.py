def main():
    userInput = ""
    question = "Parrot: hello, whats your question?\n"
    informatie = "\n" + "We leiden je op tot software engineer. Je gaat aan de slag met het ontwikkelen van software voor diverse toepassingen. Je bent in staat complexe ICT-systemen te analyseren, ontwerpen en implementeren." + "\n\n" +  "Software is overal om ons heen te vinden. Jij bent de specialist in het maken van grote en complexe software informatiesystemen die snel, efficiënt en veilig werken. Zo kun je denken aan het ontwikkelen van een functionele app, maar ook aan het analyseren van grote hoeveelheden data van social media. Bij het ontwikkelen van deze systemen kom je in aanraking met verschillende programmeertalen. Zo leer je in het eerste jaar programmeren in Python en Java/C#. Vanaf het tweede jaar kies je zelf welke programmeertaal je wilt gebruiken. Naast het programmeren en ontwikkelen van verschillende toepassingen leer je ook samenwerken." + "\n\n" +  "Na het volgen van de opleiding Informatica ben je breed inzetbaar binnen het vakgebied. Vanuit functies als programmeur of applicatieontwikkelaar kun je verder groeien binnen de ICT." + "\n\n" + "Ben jij geïnteresseerd in nieuwe techno logische ontwikkelingen, nieuwsgierig, een beetje eigenzinnig en een doorzetter, dan is de opleiding Informatica iets voor jou!" + "\n\n"
    proefstuderen = "\n" + "Heb je al een open dag bezocht? Opleidingsinformatie online bekeken? Maar twijfel je nog welke voltijd opleiding je wilt gaan volgen? Kom dan proefstuderen!" + "\n\n" +  "Proefstuderen is bedoeld voor iedereen die een opleiding in voltijd wil gaan volgen op Hogeschool Rotterdam. Je gaat gedurende 3,5 uur colleges (lessen) volgen, in groepjes werken of meedoen aan een practicum. Zo krijg je een indruk van de opleiding, de sfeer en het beroep waarvoor je wordt opgeleid" + "\n\n"
    opendag = "\n" + "De open dag en avond is een ideaal startpunt om kennis te maken met Hogeschool Rotterdam en alvast sfeer te proeven. Studenten en docenten staan voor je klaar om al je vragen te beantwoorden." + "\n" 
    check = False; 
    while True:
        userInput = input(question + "You: ")
        userInputArray = userInput.split()
        userInput = userInput.replace("?", "")
        if userInput == "bye":
            check = True;
            print("Bot: bye ;-;")
            break
        if userInput.strip() == "": 
            check = True;
            continue
        for word in userInputArray:
            word = word.replace("?", "")
            if word == "informatie" or word == "informatica":
                 print(informatie) 
                 check = True;
            if word == "proefstuderen":
                print(proefstuderen)
                check = True;
        for word, nextword in zip(userInputArray, userInputArray[1:]):
            word = word.replace("?", "")
            if word == "open" and nextword == "dag":
                print(opendag)
                check = True;
        if (check == False):
           print("Bot: I don't understand your question" + "\n")

main()

