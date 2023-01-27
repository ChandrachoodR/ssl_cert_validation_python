import requests
import pandas as pd
import time

def check_latency(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=20)
        end_time = time.time()
        latency = end_time - start_time
        print("Latency to " + url + ": " + str(latency))
        data = {'URL': url, 'Time': end_time, 'Latency': latency}
        df = pd.DataFrame(data, index=[0])
        with pd.ExcelWriter('output.xlsx', mode='a') as writer:
            df.to_excel(writer, sheet_name='Sheet1', index=False, header=False)
    except requests.exceptions.RequestException as e:
        print(e)

urls = ["https://www.example.com", "https://www.google.com", "https://www.youtube.com"]
for url in urls:
    check_latency(url)
    time.sleep(5) # sleep for 5 seconds before checking the latency for the next url
