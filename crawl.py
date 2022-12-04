import requests
from bs4 import BeautifulSoup
import time, sys

def letter(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
while (True):
    print("""
    ||   ||
     \\\()//
    //(__)\\\\
    ||    || let's crawling
    """)

    run = input('run[y/n] ')
    if run == 'n':
        break
    try:
        datainp = input('ulink : ')
        x = requests.get(datainp)
        letter('crawling is starting!!!\n')

        x_content = x.content
        def status():
            print(f"""
            link\t: {datainp}
            status\t: {x.status_code}
            """)
        if x.status_code == 200:
            soup = BeautifulSoup(x_content, 'lxml').find_all('a', href=True)
            count = 0

            status()

            for i in soup:
                count+=1
                print(count, i['href'])
                time.sleep(0.2)

        else:
            status()
            print('cannot crawling!')

    except requests.exceptions.MissingSchema:
        print('invalid scheme, using http or https first!')

    except KeyboardInterrupt:
        print('close (CTRL+C)')
        break
    
    else:
        (
            'exit!!!'
        )


    time.sleep(2)
