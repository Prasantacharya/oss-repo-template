from pymongo import MongoClient
import random
import datetime
client = MongoClient()


def random_word_requester(wordList):
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    randWord = random.choice(list(wordList.find()))
    print(randWord)
    wordList.update_one({"word": randWord}, {"$push": {"dates": datetime.datetime.utcnow().isoformat()}})
    return wordList.find_one({"word": randWord})


if __name__ == '__main__':
    print(random_word_requester(client["mongo_db_lab"]["definitions"]))
