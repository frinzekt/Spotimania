from app import db
from app.models import *


# Used To Add Changes To Database
def commitToDatabase(item):
    db.session.add(item)
    db.session.commit()

def commitDelete(item):
    db.session.delete(item)
    db.session.commit()

# User Controllers
def getAdminRole():
    adminRole = Privileges.query.filter_by(name="Administrator").first()
    if (adminRole):
        return adminRole
    adminRole = Privileges("Administrator")
    commitToDatabase(adminRole)
    return adminRole

def createNewUser(username, password, email):
    user = User(username.strip(), email.strip(),password.strip())
    commitToDatabase(user)
    return user

def createNewAdmin(username, password, email):
    adminRole = getAdminRole()
    user = User(username.strip(), email.strip(),password.strip(),adminRole)
    commitToDatabase(user)
    return user

# Gets The User Object Once Validated, otherwise returns false
def validateUserLogin(username, password):
    user = User.query.filter_by(username=username.strip()).first()
    if (user and user.check_password(password)):
        return user

    return False

def isUsernameTaken(username):
    user = User.query.filter_by(username=username.strip()).first()
    return  bool(user)

def isEmailTaken(email):
    user = User.query.filter_by(email=email.strip()).first()
    return bool(user)


# Results Controllers

def getResultsOfUser(userId):
    collection = []
    userPlayedPlaylist = User.query.get(userId).userPlayedPlaylist

    # Parse all Playlist Played By User
    for playlist in userPlayedPlaylist:
        hashMap = playlist.to_dict()
        hashMap["results"] = []

        # Parse all the question sets in the playlist
        individualResultsCollection = playlist.resultsIndividual
        for individualResult in individualResultsCollection:
            individualResultMap = individualResult.to_dict()
            songInQuiz = Song.query.get(individualResult.songId)

            # Get Some Details of the song
            individualResultMap["correctArtist"] = songInQuiz.artist
            individualResultMap["correctSongName"] = songInQuiz.songName
            hashMap["results"].append(individualResultMap)


        collection.append(hashMap)

    return collection

# Deletes a Results for a Specific User result
def deleteResults(resultsId):
    results = Results.query.get(resultsId)
    individualResultsCollection = results.resultsIndividual

    for IndividualResults in individualResultsCollection:
        commitDelete(IndividualResults)

    commitDelete(results)
