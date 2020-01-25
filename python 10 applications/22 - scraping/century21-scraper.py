{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}\n",
    "url = \"http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/\"\n",
    "req = requests.get(url, headers = headers)\n",
    "content = req.content\n",
    "soup = BeautifulSoup(content, \"html.parser\")\n",
    "\n",
    "pages = soup.find_all(\"span\", {\"id\": \"PageNumbers\", \"class\": \"PageNumbers\"})[0]\n",
    "pages = [url] + [url + a['href'] for a in pages.find_all(\"a\", href = True) if \"javascript\" not in a['href']]\n",
    "\n",
    "prop_dict_list = []\n",
    "for page in pages:\n",
    "    req = requests.get(page, headers = headers)\n",
    "    content = req.content\n",
    "    soup = BeautifulSoup(content, \"html.parser\")\n",
    "    all = soup.find_all(\"div\",{\"class\": \"propertyRow\"})\n",
    "    for property in all:\n",
    "        prop_dict = {}\n",
    "        prop_dict[\"address\"] = property.find_all(\"span\", {\"class\": \"propAddressCollapse\"})[0].text + \", \" + property.find_all(\"span\", {\"class\": \"propAddressCollapse\"})[1].text\n",
    "        prop_dict[\"price\"] = property.find(\"h4\", {\"class\": \"propPrice\"}).text.replace(\"\\n\", \"\").replace(\" \", \"\")\n",
    "        try:\n",
    "            prop_dict[\"beds\"] = property.find(\"span\", {\"class\": \"infoBed\"}).find(\"b\").text\n",
    "        except:\n",
    "            prop_dict[\"beds\"] = None\n",
    "        try:\n",
    "            prop_dict[\"fullbaths\"] = property.find(\"span\", {\"class\": \"infoValueFullBath\"}).find(\"b\").text\n",
    "        except:\n",
    "            prop_dict[\"fullbaths\"] = None\n",
    "        try:\n",
    "            prop_dict[\"sqft\"] = property.find(\"span\", {\"class\": \"infoSqFt\"}).find(\"b\").text\n",
    "        except:\n",
    "            prop_dict[\"sqft\"] = None\n",
    "        try:\n",
    "            prop_dict[\"halfbaths\"] = property.find(\"span\", {\"class\": \"infoValueHalfBath\"}).find(\"b\").text\n",
    "        except:\n",
    "            prop_dict[\"halfbaths\"] = None\n",
    "        \n",
    "        cgroup = property.find_all(\"div\", {\"class\": \"columnGroup\"})\n",
    "        for c in cgroup:\n",
    "            if c.find(\"span\", {\"class\": \"featureGroup\"}):\n",
    "                if \"Lot Size:\" in c.find(\"span\", {\"class\": \"featureGroup\"}).text:\n",
    "                    lotsize = [span.text for span in c.find_all(\"span\", {\"class\": \"featureName\"})]\n",
    "                    prop_dict[\"lotsize\"] = \"\".join(lotsize)\n",
    "            else:\n",
    "                prop_dict[\"lotsize\"] = None\n",
    "        prop_dict_list.append(prop_dict)\n",
    "\n",
    "import pandas\n",
    "data = pandas.DataFrame(prop_dict_list)\n",
    "\n",
    "data\n",
    "\n",
    "data.to_csv(\"Output.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
