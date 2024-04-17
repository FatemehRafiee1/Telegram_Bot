conversation_topics = {
    "Hobbies and Interests": [
        "What are your hobbies and interests?",
        "What do you do in your free time?",
        "Do you enjoy reading?",
        "Do you read or write stories or poems?",
        "Do you play a musical instrument?",
        "Would you like to learn to play a musical instrument?",
        "What hobbies are popular in your country?",
        "Do you like computer games?",
        "Do you have any creative hobbies like painting, writing, or music?",
        "Do you have any active hobbies like sports, hiking, or dancing?",
        "Do you prefer to do your hobbies alone or with other people?"
    ],
    "Studying": [
        "What do/did you study?",
        "Why do/did you want to study that?",
        "What subject do you enjoy studying most?",
        "Do you prefer to study alone or with other people?",
        "What was your worst subject at school?",
        "Do/Did you have a favourite teacher?",
        "Are you planning to take any courses soon?",
        "How long have you been studying English?",
        "Do you think English will be important for you in the future?",
        "Would you like to learn any other languages?"
    ],
    "Work": [
        "What do you do?",
        "What is the most important part of your job?",
        "Do you work with other people or alone?",
        "What do you like about your job?",
        "What do you not like about your job?",
        "Why did you choose your job?",
        "Do you work long hours?",
        "Do you think work-life balance is important?",
        "What is your journey like to and from work?",
        "What is your dream job?"
    ],
    "Your Home, Neighbourhood, and Country": [
        "Do you live in a house or an apartment?",
        "What is your favourite room in your house?",
        "Which room do you spend the most time in?",
        "Do you like the area where you live?",
        "What facilities do you have in your neighbourhood? (cafés, restaurants, shops etc.)",
        "What would you like to change about your neighbourhood?",
        "What do you like about your country?",
        "Tell me about the people in your country.",
        "Is your country popular with tourists?",
        "Where is a good place to visit in your country?"
    ],
    "Technology and the Internet": [
        "How often do you use a computer?",
        "What do you use computers for?",
        "Do you use a mobile phone a lot?",
        "Is it OK for children to have mobile phones?",
        "Do you like modern technology?",
        "What modern technology dont you like?",
        "How often do you use the Internet?",
        "Do you use social media sites?",
        "What is your favourite website?",
        "Is it bad to use the Internet too much?"
    ],
    "Sports and Leisure Activities": [
        "How often do you play sports or do exercise?",
        "What sports are popular in your country?",
        "Did you play sports at school?",
        "Do you prefer playing sports or watching them?",
        "How often do you watch sports?",
        "Have you ever been part of a sports team or club?",
        "What type of exercise do you enjoy doing?",
        "Do you have a favourite sportsperson?",
        "Do you like watching the Olympics?",
        "What new sport do you want to try?"
    ],
    "Food and Healthy Living": [
        "What is your favourite food?",
        "Do you normally eat healthy food?",
        "Do you enjoy cooking?",
        "What meals can you cook?",
        "What is a traditional meal in your country?",
        "Do you eat fast food?",
        "What foods do you like from other countries?",
        "What fruit and vegetables do you like?",
        "Do you think you are a healthy person?",
        "Have you ever been on a diet?"
    ],
    "Family": [
        "Do you have any brothers or sisters?",
        "Tell me about somebody in your family.",
        "Do you live with your family?",
        "How often do you spend time with your family?",
        "What do you do with your family?",
        "Do you prefer chatting with family or friends?",
        "How often do you talk on the phone with your family?",
        "Is family important to you?",
        "Have you celebrated something special with your family recently?",
        "Who do you admire in your family?"
    ],
    "Your Childhood": [
        "Tell me about your school when you were a child.",
        "What was your favourite subject?",
        "Who was your favourite teacher?",
        "Were you a good student?",
        "Where did you live as a child?",
        "Do you have the same friends now as your childhood?",
        "What did you do with your friends?",
        "What did you do during the summer holidays?",
        "What was your favourite toy as a child?",
        "Tell me about a birthday you remember from your childhood."
    ],
    "Shopping and Fashion": [
        "Do you enjoy shopping?",
        "How often do you go shopping?",
        "Do you like going to shopping centres?",
        "What do you think about online shopping?",
        "Do you enjoy shopping at traditional markets?",
        "How much money do you spend on clothes?",
        "What types of clothes do you enjoy wearing?",
        "Do you prefer summer clothes or winter clothes?",
        "What would you wear to a formal event like a wedding?",
        "Are you a fashionable person?"
    ],
    "Daily Routines": [
        "What do you normally do in the morning?",
        "Do you prefer the morning or the evening?",
        "What is your breakfast routine?",
        "Is exercise part of your daily routine?",
        "Is your routine similar every day?",
        "What do you normally do for lunch?",
        "What do you like doing after work/school?",
        "How much time do you spend relaxing every day?",
        "What do you like doing on weekends?",
        "Do you have enough free time?"
    ],
    "Entertainment": [
        "What is your favourite type of music?",
        "Do you enjoy listening to music?",
        "Where do you normally listen to music?",
        "How often do you watch television?",
        "Do you normally watch television alone or with other people?",
        "What television programmes do you like?",
        "Do you prefer watching television series or films?",
        "What types of films do you like watching?",
        "What types of films are popular in your country?",
        "How often do you go to the cinema?"
    ]
}


# c = 0
# for key, value in conversation_topics.items():
#     for v in value:
#         c += 1
#         q_data = {
#             "qid": c,
#             "topic": key,
#             "question": v
#         }
#         Question.objects.create(**q_data)