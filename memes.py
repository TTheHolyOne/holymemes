#holymods.dev
import requests
import urllib

#Auth

# create your imgflip account and put credientials here
username = ''
password = ''

# search up on google MY USER AGENT then copy the text into here
userAgent = ''

# Welcome
def main():

    print("""
    Welcome to HolyMemes

    1: Generate a Meme
    2: Help
    3: Quit
    """)
    option = input("Enter a number: ")

    if option == '1':
        # Fetching Memes

        #Fetch the available memes
        data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
        images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

        #List all the memes
        print('Memes available: \n')
        ctr = 1
        for img in images:
            print(ctr,img['name'])
            ctr = ctr+1

        #Take input from user -- Meme, Text0 and Text1
        id = int(input('Enter the number of the meme: '))
        text0 = input('Enter first text: ')
        text1 = input('Enter second text: ')

        #Fetch the generated meme
        URL = 'https://api.imgflip.com/caption_image'
        params = {
            'username':username,
            'password':password,
            'template_id':images[id-1]['id'],
            'text0':text0,
            'text1':text1
        }
        response = requests.request('POST',URL,params=params).json()
        print(response)

        #Save the meme
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', userAgent)
        filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+'.jpg')
        main()
    elif(option == '2'):
        print('A meme generator with imgflip.com api!\nJust choose a meme format and add the text\nOpen this folder and view the meme!')
        x = input("Press Any key to go back")
        main()

    elif(option == '3'):
        exit()



main()
x = input("Press Any key to exit")
