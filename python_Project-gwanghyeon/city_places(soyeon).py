from selenium import webdriver

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")
#드라이버 활성화
driver = webdriver.Chrome(options=options)

# 장소유형들을 저장할 리스트 선언
places = []


################# 경기-고양시 #################
url = 'http://www.goyang.go.kr/www/emergencyPopup/BD_selectCoronaPopupPath.do'
driver.get(url)

goyang = driver.find_elements_by_css_selector("#dataForm > table > tbody > tr > td:nth-child(2)")

for place in goyang:
    places.append(place.text)

################# 경기-광주시 #################
url = 'https://www.gwangju.go.kr/c19/contentsView.do?pageId=corona30'
driver.get(url)

gwangju = driver.find_elements_by_css_selector("#co_table > tr > td:nth-child(4)")

for place in gwangju:
        places.append(place.text)

################# 경기-부천시 #################
url = 'https://www.bucheon.go.kr/site/main/corona#none'
driver.get(url)

bucheon = driver.find_elements_by_css_selector("#route_slides > section.slide_group.flex-active-slide > div > div:nth-child(2) > table > tbody > tr > td:nth-child(2)")

for place in bucheon:
        places.append(place.text)

################# 경기-수원시 #################
url = 'https://www.suwon.go.kr/web/safesuwon/corona/PD_index.do'
driver.get(url)

driver.find_element_by_xpath("//*[@id='content']/div[1]/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='content-body']/div/div/div/div[2]/ul/li[3]/a").click()

suwon = driver.find_elements_by_css_selector("#confirmListDiv > table > tbody > tr.view_line.active > td > div table > tbody > tr:nth-child(1) > td:nth-child(2)")

for place in suwon:
        places.append(place.text)

################# 경기-시흥시 #################
url = 'https://www.siheung.go.kr/corona_place.jsp'
driver.get(url)

siheung = driver.find_elements_by_css_selector("#listArea > tbody > tr > td:nth-child(2)")

for place in siheung:
        places.append(place.text)


################# 경기-여주시 #################
url = 'https://www.yeoju.go.kr/corona.jsp'
driver.get(url)

yeoju = driver.find_elements_by_css_selector("#tab-a > div:nth-child(3) > div > div.table-responsive > table > tbody > tr > td:nth-child(3)")

for place in yeoju:
        places.append(place.text)

################# 경기-이천시 #################
url = 'https://www.icheon.go.kr/portal/contents.do?key=3568'
driver.get(url)

icheon = driver.find_elements_by_css_selector("#contents > div > table > tbody > tr > th:nth-child(1)")

for place in icheon:
        places.append(place.text)

################# 경기-화성시 #################
url = 'https://www.hscity.go.kr/www/corona/corona.do'
driver.get(url)
hwasung = driver.find_elements_by_css_selector("#board1105 > div.block.table-responsive > table > tbody > tr > td:nth-child(2)")

for place in hwasung:
        places.append(place.text)
        
################# 경기-파주시 #################
url = 'https://www.paju.go.kr/user/board/BD_board.list.do?bbsCd=9049'
driver.get(url)

paju = driver.find_elements_by_css_selector("#dataForm > div > div.board-list.m_scroll.w500 > table > tbody > tr > td:nth-child(4)")

for place in paju:
        places.append(place.text)


################# 인천광역시 #################
url = 'https://www.incheon.go.kr/health/HE020409'
driver.get(url)

driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div/div/section/div[2]/a[2]").click()
incheon = driver.find_elements_by_css_selector("#corona-tab-2 > div.board-wrap > div > div > div > table > tbody > tr > td:nth-child(3)")

for place in incheon:
        places.append(place.text)

################# 집단발생 #################
url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun='
driver.get(url)
many = driver.find_elements_by_css_selector("#content > div > div.box_line2 > div > div > table > tbody > tr > td:nth-child(3)")

for place in many:
        places.append(place.text)

#드라이버 비활성화
driver.quit()


#엑셀파일 만들기
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(places)

filename = 'C:/Users/입학홍보처/Desktop/파이썬/파이썬 프로젝트 팀프젝/장소유형(소연).xlsx' #각자 경로에 맞게 수정
wb.save(filename)