import requests
from bs4 import BeautifulSoup

URL = "http://www.veracruz.gob.mx/trabajo/junta-local-de-conciliacion-y-arbitraje/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find(id="ResultsContainer")
#print(soup)
job_elements = soup.find_all("div", class_="nota-contenido-page")
#print(job_elements)
count = 0
for job_element in job_elements:
    links = job_element.find_all("a")
    
    for link in links:
        count = count + 1
        if count==4:
            link_url = link["href"]
            page1 = requests.get(link_url)
            soup1 = BeautifulSoup(page1.content, "html.parser")
            #print(soup1)
            job_elements1 = soup.find_all("div", class_="nota-contenido-page")
            count1 = 0
            for job_element1 in job_elements1:
                links1 = job_element1.find_all("a")
                for link1 in links1:
                    count1 = count1 + 1
                    if count1==2:
                        link_url1 = link1["href"]
                        print(f"{link_url1}\n")
        #break        
#for job_element in job_elements:
#    title_element = job_element.find("h2", class_="title")
#    company_element = job_element.find("h3", class_="company")
#    location_element = job_element.find("p", class_="location")
    #print(title_element.text.strip())
    #print(company_element.text.strip())
    #print(location_element.text.strip()) 
    #print()
#python_jobs = results.find_all("h2", string="Python")
#python_jobs = results.find_all(
#    "h2", string=lambda text: "python" in text.lower()

#)
#python_job_elements = [
#    h2_element.parent.parent.parent for h2_element in python_jobs
#]
#strip removes all html tags    
#for job_element in python_job_elements:
    # -- snip --
#    links = job_element.find_all("a")
#    for link in links:
#        link_url = link["href"]
#        print(f"Apply here: {link_url}\n")
    #for link in links:
    #    print(link)
#for job_element in python_job_elements:
#    print(job_element)    