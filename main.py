import re
import long_responses as long

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Counts how many words are in the predefined message
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    
    #Calculates the percent of recognized words in a user message
    precentage = float(message_certainty)/float(len(recognized_words))

    for word in recognized_words:
        if word not in user_message:
            has_required_words = False
            break
    
    if has_required_words or single_response:
        return int(precentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Responses -------------------------------------------------------
    response('Hello', ['hello', 'hi', 'yo', 'sup', 'hey', 'howdy'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['you', 'are', 'so', 'cool'], required_words=['so', 'cool'])
    response('So goooooood!!!', ['good'], single_response=True)

    response(long.R_EATING, ['what', 'are', 'you', 'eating'], required_words=['you', 'eating'])
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_responses(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Testing the response system
while True:
    print('Bot: ' + get_responses(input('You: ')))