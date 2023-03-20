#Import libraries
import streamlit as st
st.set_page_config(layout="wide")

import os # os is a standard Python module, there's no need install it. https://stackoverflow.com/questions/48010748/how-to-install-the-os-module-on-windows
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
import pandas as pd # import for the dataframe creation
import googlesearch # imports the search api
import random # random2 # for random time frames
import sys # ? maybe there's no need install it #for sys variables
import time # standard, maybe don't need to install
from oauth2client.client import GoogleCredentials
from http.client import HTTPSConnection #. #http.client is part of the python3 standard library and does not need to be installed https://stackoverflow.com/questions/44986195/i-cant-install-httpclient-for-python
from base64 import b64encode
from json import loads #. # json is a built-in module, you don't need to install it with pip.
from json import dumps #. #https://stackoverflow.com/questions/41466431/pip-install-json-fails-on-ubuntu
import requests
from st_aggrid import AgGrid

from dotenv import load_dotenv
#from python_dotenv import load_dotenv as dotenv
load_dotenv()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("src/style.css")
##################################################################

header = st.container()
input_data = st.container()
# set_keywords = st.container()
is_keyword_empty = False

keyword_list = []

with header:
    # st.title('International Search Overlap')
    st.header('How to use this tool?')
    # st.text('''You have to run every cell by yourself, but:\nIf your input is needed, you must enter/select it first before you run the cell. \nEvery other cell can be run directly.\nRun the cells from top to bottom.''')
    st.subheader('In order to calculate overlapscore, enter the data and click the button')

with input_data:
    st.header('Input Data')
    # form = st.form("my_form")
    # col1, col2 = form.columns(2, gap="large")

# with st.form("my_form"):
with input_data.form("my_form"):
    col1, col2 = st.columns(2, gap="large")
    submitted = st.form_submit_button("Calculate Overlapscore")
    col3, col4, col5 = st.columns([1, 2, 1])
    # Now add a submit button to the form:
    # submitted = st.form_submit_button(label="Calculate Overlapscore", help=None, on_click=calculate_overlapscore)
    


with col1:
    #@title Select Language, Country & Device
    # setting the parameters for tld, language, country and device
    #google_tld = 'de' #@param ["ad", "ae", "am", "as", "at", "az", "ba", "be", "bf", "bg", "bi", "bj", "bs", "by", "ca", "cat", "cd", "cf", "cg", "ch", "ci", "cl", "cm", "co.ao", "co.bw", "co.ck", "co.cr", "co.id", "co.il", "co.im", "co.in", "co.je", "co.jp", "co.ke", "co.kr", "co.ls", "co.ma", "co.mw", "co.mz", "co.nz", "co.pn", "co.th", "co.tt", "co.tz", "co.ug", "co.uk", "co.uz", "co.ve", "co.vi", "co.za", "co.zm", "co.zw", "com", "com.af", "com.ag", "com.ai", "com.ar", "com.au", "com.bd", "com.bh", "com.bn", "com.bo", "com.br", "com.bz", "com.co", "com.cu", "com.cy", "com.do", "com.ec", "com.eg", "com.et", "com.fj", "com.gh", "com.gi", "com.gr", "com.gt", "com.hk", "com.jm", "com.kh", "com.kw", "com.kz", "com.lb", "com.lv", "com.ly", "com.mt", "com.mw", "com.mx", "com.my", "com.na", "com.nf", "com.ng", "com.ni", "com.np", "com.om", "com.pa", "com.pe", "com.ph", "com.pk", "com.pl", "com.pr", "com.py", "com.qa", "com.ru", "com.sa", "com.sb", "com.sg", "com.sl", "com.sv", "com.tj", "com.tn", "com.tr", "com.tt", "com.tw", "com.ua", "com.uy", "com.vc", "com.ve", "com.vn", "cv", "cz", "de", "dj", "dk", "dm", "dz", "ee", "es", "fi", "fm", "fr", "ga", "ge", "gg", "gl", "gm", "gp", "gr", "gy", "hk", "hn", "hr", "ht", "hu", "ie", "iq", "is", "it", "je", "jo", "jp", "kg", "ki", "kz", "la", "li", "lk", "lt", "lu", "lv", "md", "me", "mg", "mk", "ml", "mn", "ms", "mu", "mv", "mw", "ne", "ne.jp", "nl", "no", "nr", "nu", "off.ai", "ph", "pl", "pn", "ps", "pt", "ro", "rs", "ru", "rw", "sc", "se", "sg", "sh", "si", "sk", "sm", "sn", "so", "st", "td", "tg", "tk", "tl", "tl", "tm", "tn", "to", "tt", "us", "vg", "vn", "vu", "ws"]
    st.subheader('Select Language, Country & Device')
    language = st.selectbox(
    'Select language',
    ("Afrikaans","Albanian","Amharic","Arabic","Armenian","Azerbaijani","Basque","Belarusian","Bengali","Bosnian","Bulgarian","Catalan","Cebuano","Chinese (Simplified)","Chinese (Traditional)","Corsican","Croatian","Czech","Danish","Dutch","English","Esperanto","Estonian","Finnish","French","Frisian","Galician","Georgian","German","Greek","Gujarati","Haitian Creole","Hausa","Hawaiian","Hebrew","Hindi","Hmong","Hungarian","Icelandic","Igbo","Indonesian","Irish","Italian","Japanese","Javanese","Kannada","Kazakh","Khmer","Kinyarwanda","Korean","Kurdish","Kyrgyz","Lao","Latvian","Lithuanian","Luxembourgish","Macedonian","Malagasy","Malay","Malayalam","Maltese","Maori","Marathi","Mongolian","Myanmar (Burmese)","Nepali","Norwegian","Nyanja (Chichewa)","Odia (Oriya)","Pashto","Persian","Polish","Portuguese (Portugal","Punjabi","Romanian","Russian","Samoan","Scots Gaelic","Serbian","Sesotho","Shona","Sindhi","Sinhala (Sinhalese)","Slovak","Slovenian","Somali","Spanish","Sundanese","Swahili","Swedish","Tagalog (Filipino)","Tajik","Tamil","Tatar","Telugu","Thai","Turkish","Turkmen","Ukrainian","Urdu","Uyghur","Uzbek","Vietnamese","Welsh","Xhosa","Yiddish","Yoruba","Zulu"),
    index=28)
    country = st.selectbox(
    'Select country',
    ("Afghanistan", "Albania", "Antarctica", "Algeria", "American Samoa", "Andorra", "Angola", "Antigua and Barbuda", "Azerbaijan", "Argentina", "Australia", "Austria", "The Bahamas", "Bahrain", "Bangladesh", "Armenia", "Barbados", "Belgium", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Belize", "Solomon Islands", "Brunei", "Bulgaria", "Myanmar (Burma)", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Sri Lanka", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Republic of the Congo", "Democratic Republic of the Congo", "Cook Islands", "Costa Rica", "Croatia", "Cyprus", "Czechia", "Benin", "Denmark", "Dominica", "Dominican Republic", "Ecuador", "El Salvador", "Equatorial Guinea", "Ethiopia", "Eritrea", "Estonia", "South Georgia and the South Sandwich Islands", "Fiji", "Finland", "France", "French Polynesia", "French Southern and Antarctic Lands", "Djibouti", "Gabon", "Georgia", "The Gambia", "Germany", "Ghana", "Kiribati", "Greece", "Grenada", "Guam", "Guatemala", "Guinea", "Guyana", "Haiti", "Heard Island and McDonald Islands", "Vatican City", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Kazakhstan", "Jordan", "Kenya", "South Korea", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Lesotho", "Latvia", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Monaco", "Mongolia", "Moldova", "Montenegro", "Morocco", "Mozambique", "Oman", "Namibia", "Nauru", "Nepal", "Netherlands", "Curacao", "Sint Maarten", "Caribbean Netherlands", "New Caledonia", "Vanuatu", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Norway", "Northern Mariana Islands", "United States Minor Outlying Islands", "Federated States of Micronesia", "Marshall Islands", "Palau", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn Islands", "Poland", "Portugal", "Guinea-Bissau", "Timor-Leste", "Qatar", "Romania", "Rwanda", "Saint Helena, Ascension and Tristan da Cunha", "Saint Kitts and Nevis", "Saint Lucia", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Vietnam", "Slovenia", "Somalia", "South Africa", "Zimbabwe", "Spain", "Suriname", "Eswatini", "Sweden", "Switzerland", "Tajikistan", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "United Arab Emirates", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "North Macedonia", "Egypt", "United Kingdom", "Guernsey", "Jersey", "Tanzania", "United States", "Burkina Faso", "Uruguay", "Uzbekistan", "Venezuela", "Wallis and Futuna", "Samoa", "Yemen", "Zambia"),
    index=69)
    device = st.selectbox(
    'Select device',
    ("mobile", "desktop"),
    index=1)

#with set_keywords:
with col2:
    st.subheader('Enter the keywords you want to compare')
    # schadenversicherung haftpflichtversicherung
    keyword1 = st.text_input('keyword1', 'kfzversicherung')
    keyword_list.append(keyword1)
    keyword2 = st.text_input('keyword2', 'autoversicherung deutschland')
    keyword_list.append(keyword2)
    keyword3 = st.text_input('keyword3', 'kfzversicherung deutschland')
    keyword_list.append(keyword3)
    if (len(keyword1) * len(keyword2) == 0):
        is_keyword_empty = True
    st.text('Your keywords: ' + ', '.join(keyword_list))




##################################################################

# creating the Restclient
class RestClient:
    domain = "api.dataforseo.com"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def request(self, path, method, data=None):
        connection = HTTPSConnection(self.domain)
        try:
            base64_bytes = b64encode(
                ("%s:%s" % (self.username, self.password)).encode("ascii")
                ).decode("ascii")
            headers = {'Authorization' : 'Basic %s' %  base64_bytes, 'Content-Encoding' : 'gzip'}
            connection.request(method, path, headers=headers, body=data)
            response = connection.getresponse()
            return loads(response.read().decode())
        finally:
            connection.close()

    def get(self, path):
        return self.request(path, 'GET')

    def post(self, path, data):
        if isinstance(data, str):
            data_str = data
        else:
            data_str = dumps(data)
        return self.request(path, 'POST', data_str)

##################################################################
def calculate_overlapscore(**kwargs):
    with st.spinner(text="Wait for it..."):
        params = {key: value for key, value in kwargs.items()}
        # calculate_overlapscore(keyword_list=keyword_list, language_name=language, location_name=country, device=device)

        keywords = pd.DataFrame(keyword_list, columns=["keyword"])
        #@title Run this cell to get your Overlapscore!
        keywordlist = list(set(list(keywords["keyword"].values.tolist())))
        try:
            keywordlist.remove('')
        except:
            a=1

        # simple way to set a task
        # post_data = dict()
        results=[]
        errors=[]
        for keyword in keywordlist:
            # post_data[len(post_data)] = dict(
            post_data = [dict(
                #se_domai = "google."+ google_tld,
                location_name = country,
                language_name = language,
                keyword = keyword,
                device = device,
            )]
            # post_data = [post_data]

            #1
            #request dataforseo api
            client = RestClient(os.environ.get('REST_CLIENT_USERNAME'), os.environ.get('REST_CLIENT_PASSWORD'))
            response = client.post("/v3/serp/google/organic/live/advanced", post_data)
            #you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
            if response["status_code"] != 20000:
                print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
                return
            # print("response['tasks']")
            # print(response['tasks'])
            for task in response['tasks']:
                if (task['result'] and (len(task['result']) > 0)):
                    for resultTaskInfo in task['result']:
                        results.append(resultTaskInfo)
                    else:
                        errors.append(task)
        #print('-----------------------results-------------------------------')
        #print(results)

        # put serps into dataframes 
        df = pd.DataFrame(results)
        organic = pd.DataFrame()
        for j in range(len(df["items"])):
            organic_result = 1
            for i in range(len(df["items"][j])):
                if df["items"][j][i]["type"] == "organic" and organic_result<11:
                    df["items"][j][i]["rank_organic"] = organic_result
                    df["items"][j][i]["keyword"] = df["keyword"][j]
                    organic = organic.append([df["items"][j][i]])
                    organic_result += 1
        organic = organic.reset_index()
        organic = organic[['url', 'keyword', 'rank_organic', 'title']]

        #getting the overlap score
        result = pd.merge(organic[organic["keyword"]==keyword1], organic[organic["keyword"]==keyword2], how="inner", on="url")
        if (len(keywordlist) > 2):
            result = pd.merge(result, organic[organic["keyword"]==keyword3], how="inner", on="url")

        overlapscore = 0 + 10*len(result) #if the lenght is 10 it will be 100%
        for i in range(len(result)):
            # 100% is the max
            if overlapscore < 100:
                if (len(keywordlist) > 2):
                    delta1 = 1/3 if (result.rank_organic_x[i] == result.rank_organic_y[i]) else 1/abs(result.rank_organic_x[i] - result.rank_organic_y[i])/3
                    delta2 = 1/3 if (result.rank_organic_x[i] == result.rank_organic[i]) else 1/abs(result.rank_organic_x[i] - result.rank_organic[i])/3
                    delta3 = 1/3 if (result.rank_organic[i] == result.rank_organic_y[i]) else 1/abs(result.rank_organic[i] - result.rank_organic_y[i])/3
                    overlapscore = overlapscore + delta1 + delta2 + delta3
                else:
                    delta = 1 if (result.rank_organic_x[i] == result.rank_organic_y[i]) else 1/abs(result.rank_organic_x[i] - result.rank_organic_y[i])
                    overlapscore = overlapscore + delta
            else:
                break

        

        fig = plt.figure(figsize=(10, 10))

        if (len(keywordlist) > 2):
            value_ABC = round(overlapscore, 2)

            if (overlapscore == 0):
                value_AB_list = []
                keywordpair_list = [
                    [keyword1, keyword2],
                    [keyword1, keyword3],
                    [keyword2, keyword3]
                ]
                for j in range(len(keywordlist)):
                    #getting the overlap score
                    result = pd.merge(organic[organic["keyword"]==keywordpair_list[j][0]], organic[organic["keyword"]==keywordpair_list[j][1]], how="inner", on="url")

                    value_AB = 0 + 10*len(result) #if the lenght is 10 it will be 100%
                    for i in range(len(result)):
                        if value_AB < 100:
                            delta = 1 if (result.rank_organic_x[i] == result.rank_organic_y[i]) else 1/abs(result.rank_organic_x[i] - result.rank_organic_y[i])
                            value_AB = value_AB + delta
                        else:
                            break
                    value_AB_list.append(round(value_AB, 2))

                value_AB = value_AB_list[0]
                value_AC = value_AB_list[1]
                value_BC = value_AB_list[2]
            else:                    
                value_AC = value_BC = value_AB = round((100 - value_ABC) / 20, 2)
                
            value_A = round(100 - value_AB - value_AC - value_ABC, 2)
            value_B = round(100 - value_AB - value_BC - value_ABC, 2)
            value_C = round(100 - value_BC - value_AC - value_ABC, 2)

            # venn3(subsets = (round(100 - overlapscore,2), round(100 - overlapscore,2), round(overlapscore,2), round(100 - overlapscore,2), round(overlapscore,2), round(overlapscore,2), 1), set_labels = ('Group A', 'Group B', 'Group C'), alpha = 0.5);
            colors = ['darkviolet','deepskyblue','blue']
            subsets_venn3 = (value_A, value_B, value_AB, value_C, value_AC, value_BC, value_ABC)
            vd = venn3(subsets = subsets_venn3, set_labels = (keyword1, keyword2, keyword3), alpha = 0.5, set_colors=colors);
            labels = ['100', '101', '110', '010', '001', '011']
            for label in labels:
                vd.get_label_by_id(label).set_text('')
            
            if (overlapscore == 0):
                lbl = vd.get_label_by_id("B")
                x, y = lbl.get_position()
                lbl.set_position((x+0.4, y+0.9))
                lbl = vd.get_label_by_id("A")
                x, y = lbl.get_position()
                lbl.set_position((x-0.2, y))
        else:
            colors = ['blue', 'deepskyblue']
            v2 = venn2(subsets = (round(100 - overlapscore,2), round(100 - overlapscore,2), round(overlapscore,2)), set_labels = (keyword1, keyword2), alpha = 0.5, set_colors=colors)
            for label in ['10', '01']:
                v2.get_label_by_id(label).set_text('')

        plt.show()        
        print("")
        print("Your overlapscore is:", round(overlapscore,2),"%")
        print("")
        # display(result)
        #with st.spinner('Wait for it...'):
        #    time.sleep(5)


        ##################################################################

        with col4:
            get_overlapscore = st.container()

            with get_overlapscore:
                st.header('Your Overlapscore')
                st.pyplot(fig)
                # st.table(result)
        AgGrid(result)

    st.success('Done!')


##################################################################

# print('if submitted:', submitted)
if submitted:
    submited = False
    # st.wtrite("slider", slider_val, "checkbox", checkbox_val)
    #st.write({
    #    'keyword_list': keyword_list,
    #    'language': language,
    #    'country': country,
    #   'device': device
    #})
    # st.text(keyword_list)
    if is_keyword_empty:
        st.error("keyword1 and keyword2 cannot be empty")
        is_keyword_empty = False
    else:
        calculate_overlapscore(keyword_list=keyword_list, language_name=language, location_name=country, device=device)