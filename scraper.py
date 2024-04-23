from requests_html import HTMLSession

def matchStats(team):
    url = f'https://www.google.com/search?q={team}+last+score'
    response = HTMLSession().get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'})
    data = {
        "team1": {
            "name": response.html.find('div.liveresults-sports-immersive__hide-element')[0].text,
            "score": response.html.find('div.imso_mh__l-tm-sc', first=True).text 
        },
        "team2": {
            "name": response.html.find('div.liveresults-sports-immersive__hide-element')[1].text,
            "score": response.html.find('div.imso_mh__r-tm-sc', first=True).text 
        },
    }
    if response.html.find('span.imso_mh__ft-mtch'): 
        data['status'] = response.html.find('span.imso_mh__ft-mtch', first=True).text 
        data["time"] = response.html.find('div.imso-hide-overflow', first=True).text
    else: 
        data['status'] = response.html.find("div.imso_mh__lv-m-stts-cont", first=True).text
        data["time"] = response.html.find('span.imso-hide-overflow', first=True).text
    return data
