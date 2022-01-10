import discogs_client
import re
import math

# results = list
Format = str
list_form = str


token_response = False
while not token_response:
    # print('Invalid format, try again')
    Token = input('Enter Discogs Dev Token')
    try:
        f = discogs_client.Client('uwu', user_token=Token)
        f._get(url='https://api.discogs.com/database/search?release_title=nevermind&artist=nirvana&per_page=3&page=1')
    except:
        print('Invalid Token, Try Again')
        Token = input('Enter Discogs Dev Token')
    else:
        token_response = True
        break


valid_response = False
while not valid_response:
    # print('Invalid format, try again')
    Format = input('What format is your music? (Cd/Vinyl)')
    if Format == "Cd" or Format == "Vinyl":
        valid_response = True
        break

list_response = False
while not list_response:
    # print('Enter a valid number and try again:')
    print('(1) Title,')
    print('(2) Title(Year),')
    print('(3) Title:Condition,')
    print('(4) Title(Year):Condition,')
    list_form = input('How is your list formatted?')
    if list_form == '1' or list_form == '2' or list_form == '3' or list_form == '4':
        list_response = True
        break
end_response = False
while not end_response:
    # print('Invalid format, try again')
    print('(1) Input + Price')
    print('(2) Price Only')
    output = input('How Would You Like The Output Formatted?')
    if output == "1" or output == "2":
        end_response = True
        break

d = discogs_client.Client('cliento', user_token=Token)
list = input("Enter List Here")
if list[-1] == ',':
    list = list[:-1]


Titles = list.split("," or ", ")
# print(Titles)

title = str

for title in Titles:

    condition = title.split(":")
    iserror = False
    iserrortwo = False

    def bruh():
        search = False
        while not search:

            if list_form == '3' or list_form == '4':
                results = d.search(condition[0], type='release', format=Format)
                # search = True
                return results

            else:
                results = d.search(title, type='release', format=Format)
                # search = True
                return results

    # if results[1] is None or condition[1] is None:
    #    break
# else:

    try:
        releaseId = int(re.search(r'\d*\.?\d+', str(bruh()[0]))[0])
    except IndexError:
        correctTitle = [title, 'Not Found']
        print(correctTitle[0] + correctTitle[1])
        iserror = True

    if not iserror:
        correctTitle = str(bruh()[0]).split("'")
        # print(correctTitle)
        releaseInfo = d._get(url='https://api.discogs.com/marketplace/stats/' + str(releaseId))

        # Not Stolen hacky code to take the value value out of the string
        char1 = 'value'
        char2 = 'currency'
        mystr = str(releaseInfo)  # Edgy joke here
        # priceNumber = int(re.search(r'\d+', str(mystr[mystr.find(char1) + 1: mystr.find(char2)]))[0])
        try:
            priceNumber = float(
                math.ceil(float(re.findall(r'\d*\.?\d+', str(mystr[mystr.find(char1) + 1: mystr.find(char2)]))[0])))
        except IndexError:
            priceNumber = ' Price Not Found'
            iserrortwo = True

        if not iserrortwo:
            price = str('$' + str(priceNumber))
            if list_form == '2' or list_form == '4':
                char3 = '('
                char4 = ')'
                ystr = str(title)
                year = ystr[ystr.find(char3) + 1: ystr.find(char4)]

            if list_form == '1' and output == '1':
                print(correctTitle[1] + ' : ' + price)
            elif list_form == '2' and output == '1':
                print(correctTitle[1] + "(" + year + ")" + " : " + price)
            elif list_form == '3' and output == '1':
                print(correctTitle[1] + " : " + price + condition[1])
            elif list_form == '4' and output == '1':
                print(correctTitle[1] + "(" + year + ")" + " : " + price + " " + condition[1])
            elif output == '2':
                print(price)
# print(results[1])
# print(releaseInfo)
# print(correctTitle[1] + "(" + year + ")" + " : " + price + " " + condition[1])
# print(releaseid)
