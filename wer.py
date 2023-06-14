import jiwer

from jiwer import wer

reference = "well in my free time since i lived in a in an agricultural town mostly what we did after school was just go to the mall get pizza and go get boba there wasn’t really much to do other than going out on a twenty minute drive to go to monterey because that was the place where a lot of most tourist attractions were and we didn’t necessarily do a lot of things in my hometown but the surrounding area yeah"
hypothesi = "well in my free time since i lived in a in an agricultural town um mostly what we did after school is just go to the mall get pizza and go get boba there isn't really much to do other than going out on a 20 minute drive to go to monterey because that was the place where a lot of most tourist attractions were and we didn't necessarily do a lot of things in my hometown but the surrounding area yeah"

error = wer(reference, hypothesi)

print(error)