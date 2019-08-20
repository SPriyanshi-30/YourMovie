# bs4 imports BeautifulSoup as SOUP 
# import requests as HTTP 
  
# Main function to perform scraspping
def main(emotion): 
  
    # Sad = Drama
    if(emotion == "Sad"): 
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
  
    # Disgust = Musical
    elif(emotion == "Disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
  
    # Anger = Family
    elif(emotion == "Anger"): 
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
    # Anticipation = Thriller
    elif(emotion == "Anticipation"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # Fear = Sport 
    elif(emotion == "Fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    # Enjoyment = Thriller
    elif(emotion == "Enjoyment"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # Trust = Western
    elif(emotion == "Trust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
  
    # Surprise = Film-Noir
    elif(emotion == "Surprise"): 
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
  
    # HTTP request to get the data of 
    # the whole page 
    response = HTTP.get(urlhere) 
    data = response.text 
  
    # Parsing the data using 
    # BeautifulSoup 
    soup = SOUP(data, "lxml") 
  
    # Extract movie titles from the 
    # data using regex 
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    return title 
  
# Driver Function 
if __name__ == '__main__': 
  
    emotion = input("Enter your current emotion: ") 
    a = main(emotion) 
    count = 0
  
    if(emotion == "Disgust" or emotion == "Anger"
                           or emotion=="Surprise"): 
  
        for i in a: 
  
            # Splitting each line of the 
            # IMDb data to scrape movies 
            tmp = str(i).split('>;') 
  
            if(len(tmp) == 3): 
                print(tmp[1][:-3]) 
  
            if(count > 13): 
                break
            count += 1
    else: 
        for i in a: 
            tmp = str(i).split('>') 
  
            if(len(tmp) == 3): 
                print(tmp[1][:-3]) 
  
            if(count > 11): 
                break
            count+=1
