from bs4 import BeautifulSoup

s = requests.Session()

r = s.get("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(r.text)
viewstate_element = soup.find(id="__VIEWSTATE")
viewstate = viewstate_element["value"]
eventvalidation_element = soup.find(id="__EVENTVALIDATION")
eventvalidation = eventvalidation_element["value"]

r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
           data = (
                   ("__EVENTTARGET", ""),
                   ("__EVENTARGUMENT", ""),
                   ("__VIEWSTATE", viewstate),
                   ("__VIEWSTATEGENERATOR",viewstategenerator),
                   ("__EVENTVALIDATION", eventvalidation),
                   ("CarrierList", "VX"),
                   ("AirportList", "BOS"),
                   ("Submit", "Submit")
                  ))

f = open("virgin_arg_airport.html", "w")
f.write(r.text)