import random

R_EATING = "I will eat all of your code ;) so make your variables private!"


def unknown():
    response = ['Could you please re-phrase that?',
                "....", 
                "Sounds about right",
                "What does that mean?",
                "You're not making any sense??"][random.randrange(5)]
    return response