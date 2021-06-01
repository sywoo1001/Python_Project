import openpyxl

pcroom = 0
cafe = 0
playpark = 0
transportation = 0
resturant = 0
com_center = 0
hospital = 0
publicSanitation = 0
pleasure = 0
gym = 0
church = 0
society = 0
store = 0
songroom = 0
work = 0
school = 0
academy = 0
etc = 0

sum = 0

file = openpyxl.load_workbook("코로나.xlsx")

sheet = file.active

if "업소" in sheet["B1"].value or "장소유형" in sheet["B1"].value or "경로" in sheet["B1"].value:
    i = 1
    while True:
        i += 1
        if sheet["B" + str(i)].value is None:
            break
        if "pc방" in sheet["B" + str(i)].value:
            pcroom += 1
            sum += 1
        elif "카페" in sheet["B" + str(i)].value:
            cafe += 1
            sum += 1
        elif "놀이공원" in sheet["B" + str(i)].value:
            playpark += 1
            sum += 1
        elif "식당" in sheet["B" + str(i)].value or "음식점" in sheet["B" + str(i)].value:
            resturant += 1
            sum += 1
        elif "주민센터" in sheet["B" + str(i)].value:
            com_center += 1
            sum += 1
        elif "병원" in sheet["B" + str(i)].value or "의원" in sheet["B" + str(i)].value\
                or "의료" in sheet["B" + str(i)].value:
            hospital += 1
            sum += 1
        elif "무궁화호" in sheet["B" + str(i)].value or "지하철" in sheet["B" + str(i)].value \
                or "KTX" in sheet["B" + str(i)].value or "택시" in sheet["B" + str(i)].value \
                or "버스" in sheet["B" + str(i)].value:
            transportation += 1
            sum += 1
        elif "미용실" in sheet["B" + str(i)].value or "이발소" in sheet["B" + str(i)].value or "공중위생업" in sheet["B" + str(i)].value or "목욕" in sheet["B" + str(i)].value or "남탕" in sheet["B" + str(i)].value \
                or "여탕" in sheet["B" + str(i)].value or "사우나" in sheet["B" + str(i)].value:
            publicSanitation += 1
            sum += 1
        elif "유흥업소" in sheet["B" + str(i)].value or "주점" in sheet["B" + str(i)].value or "클럽" in sheet["B" + str(i)].value:
            pleasure += 1
            sum += 1
        elif "헬스장" in sheet["B" + str(i)].value or "체육시설" in sheet["B" + str(i)].value:
            gym += 1
            sum += 1
        elif "종교" in sheet["B" + str(i)].value or "교회" in sheet["B" + str(i)].value:
            church += 1
            sum += 1
        elif "동호회" in sheet["B" + str(i)].value or "지인" in sheet["B" + str(i)].value or "모임" in sheet["B" + str(i)].value:
            society += 1
            sum += 1
        elif "마트" in sheet["B" + str(i)].value or "판매점" in sheet["B" + str(i)].value or "시장" in sheet["B" + str(i)].value or "기계공구" in sheet["B" + str(i)].value or "육가공업" in sheet["B" + str(i)].value:
            store += 1
            sum += 1
        elif "오락문화" in sheet["B" + str(i)].value or "노래방" in sheet["B" + str(i)].value or "노래연습장" in sheet["B" + str(i)].value:
            songroom += 1
            sum += 1
        elif "직장" in sheet["B" + str(i)].value or "사무시설" in sheet["B" + str(i)].value or "회사" in sheet["B" + str(i)].value:
            work += 1
            sum += 1
        elif "학교" in sheet["B" + str(i)].value or "어린이집" in sheet["B" + str(i)].value:
            school += 1
            sum += 1
        elif "학원" in sheet["B" + str(i)].value:
            academy += 1
            sum += 1
        else: # 장소유형 미공개 데이터 기타로 처리
            etc += 1

loc = [["PC방", pcroom],
       ["카페", cafe],
       ["놀이공원", playpark],
       ["교통수단", transportation],
       ["음식점", resturant],
       ["주민센터", com_center],
       ["병원", hospital],
       ["공중위생업(목욕탕, 미용실 등)", publicSanitation],
       ["유흥업소(술집, 나이트, 클럽 등)", pleasure],
       ["체육시설(헬스장, 농구장 등)", gym],
       ["종교시설", church],
       ["모임", society],
       ["판매점(마트, 가게, 시장 등)", store],
       ["오락문화(노래방 등)", songroom],
       ["직장", work],
       ["학교(어린이집, 초·중·고등학교)",school],
       ["학원", academy]
       ]
