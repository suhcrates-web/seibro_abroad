
from bs4 import BeautifulSoup
import requests
import xmltodict
from datetime import date

def check_sibro():

    url = 'https://seibro.or.kr/websquare/engine/proworks/callServletService.jsp'
    today = date.today().strftime('%Y%m%d')
    today = '20210304'
    #당일 나옴.
    #없으면 'result'가 없음.
    #header는 좀 틀려도 됨.
    payload=f"""
    <reqParam action="getImptFrcurStkSetlAmtList" task="ksd.safe.bip.cnts.OvsSec.process.OvsSecIsinPTask"><MENU_NO 
    value="921"/><CMM_BTN_ABBR_NM value="allview,allview,print,hwp,word,pdf,seach,xls,link,link,wide,wide,top,"/><W2XPATH value="/IPORTAL/user/ovsSec/BIP_CNTS10013V.xml"/><PG_START value="1"/><PG_END value="10"/><START_DT value="{today}"/><END_DT value="{today}"/><S_TYPE value="2"/><S_COUNTRY value="ALL"/><D_TYPE value="1"/></reqParam>
    """

    header = {
        'Accept': 'application/xml',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '427',
        'Content-Type': 'application/xml; charset="UTF-8"',
        'Cookie': 'WMONID=VxIxlyB-vOf; '
                  'JSESSIONID=d5bMXrnZYtrwWoFFCdYY5uJcNpRnuDtB-rWLyiKoy4EXvJe9lGhb!-2032988413; lastAccess=1614042102839',
        'Host': 'seibro.or.kr',
        'Origin': "https://seibro.or.kr",
        'Referer': 'https://seibro.or.kr/websquare/control.jsp?w2xPath=/IPORTAL/user/ovsSec/BIP_CNTS10013V.xml'
                   '&menuNo=921',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'submissionid': 'submission_getImptFrcurStkCusRemaList',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    result = requests.post(url, payload, headers=header)
    f = result.content
    d = xmltodict.parse(f, dict_constructor=dict)
    print(d)
    flag = d['vector']['@result']
    if  flag == 0:
        today_bool = False
    else:
        today_bool = True

    if today_bool:
        print('세이브로 나옴')
        return True

    else:
        print('안나옴')
        return False



    if today_bool:
        print('asdf')