"""
Github: https://github.com/opabravo

## 功能

可根據性別與戶籍地資訊生成合法的台灣身分證字號，並存到檔案。

## 目的

許多網站(如: 學校)及資料(如: 電子對帳單)的預設密碼為身分證字號或與其相關之組合，
此腳本可幫助滲透測試團隊根據目標信息生成身分證字號到字典檔，來檢測此風險。

## 身分證字號規律說命

中華民國國民身分證字號共有10碼，
其中第1碼英文字母代表為縣市，
而第1個數字為性別碼。1為男生、2為女生。

第3碼至第9碼為依照出生登記順序編號之流水號碼。

最後一碼也就是最後一個數字為驗證碼，
用來檢驗身分證字號是否正確。

詳細資訊參考: https://wisdom-life.in/article/taiwain-id-explanation
"""
from typing import List
from pathlib import Path
import utils


BASE_DIR = Path(__file__).resolve().parent

# "L": "台中縣", "R": "台南縣", "S": "高雄縣", "Y": "陽明山管理局" has been removed
CITY_CODE_MAPPING = {
    'A': {'name': '台北市', 'code': '10'},
    'B': {'name': '台中市', 'code': '11'},
    'C': {'name': '基隆市', 'code': '12'},
    'D': {'name': '台南市', 'code': '13'},
    'E': {'name': '高雄市', 'code': '14'},
    'F': {'name': '新北市', 'code': '15'},
    'G': {'name': '宜蘭縣', 'code': '16'},
    'H': {'name': '桃園市', 'code': '17'},
    'I': {'name': '嘉義市', 'code': '34'},
    'J': {'name': '新竹縣', 'code': '18'},
    'K': {'name': '苗栗縣', 'code': '19'},
    'M': {'name': '南投縣', 'code': '21'},
    'N': {'name': '彰化縣', 'code': '22'},
    'O': {'name': '新竹市', 'code': '35'},
    'P': {'name': '雲林縣', 'code': '23'},
    'Q': {'name': '嘉義縣', 'code': '24'},
    'T': {'name': '屏東縣', 'code': '27'},
    'U': {'name': '花蓮縣', 'code': '28'},
    'V': {'name': '台東縣', 'code': '29'},
    'W': {'name': '金門縣', 'code': '32'},
    'X': {'name': '澎湖縣', 'code': '30'},
    'Z': {'name': '連江縣', 'code': '33'}
}


def get_output_path(cities: List[str], genders: List[int]) -> Path:
    filename = f'tw_ids_{"".join(map(str, genders))}_{"".join(cities)}.txt'
    output_path = BASE_DIR / "output" / f"{filename}"
    # Make sure output directory exist
    if not output_path.parent.exists():
        output_path.parent.mkdir()
    return BASE_DIR / "output" / f"{filename}"


def get_city(city: str):
    """Get city object"""
    return CITY_CODE_MAPPING.get(city.upper())


def get_gender_name(gender_num: int) -> str:
    return "男生" if gender_num == 1 else "女生"


def generate_ids(genders: List[int], cities: List[str]):
    output_path = get_output_path(cities, genders)
    if output_path.exists():
        confirm = input(f"檔案 {output_path} 已存在，\n請確認是否要覆蓋! (y/n): ")
        if confirm.lower() not in {'y', 'yes'}:
            return
        output_path.unlink()

    print(f"\n[!] 正在產生身分證字號到 {output_path.resolve()}")

    for gender in genders:
        print(f"[!] 正在產生 {get_gender_name(gender)} 的身分證字號...")
        for city in cities:
            print(f"    [!] 正在產生 {get_city(city)['name']} 的身分證字號...")
            city_code = get_city(city)['code']
            utils.generate_id(gender, city, int(city_code), str(output_path))
    print(
        f"\n[+] 完成，檔案名稱的格式為 tw_ids_<性別代號>_<戶籍地代號>，請查看 {output_path.resolve()}")


def show_city_code_table():
    print("城市代碼表\n----------")
    for k, v in CITY_CODE_MAPPING.items():
        print(f"{k} : {v['name']}")
    print("----------\n")


def main():
    if genders_input := input("請輸入 性別 [1 = 男生, 2 = 女生] (選填 | 可用此格式指定多項 : 1,2) -> "):
        genders = list(map(int, genders_input.split(",")))
    else:
        genders = [1, 2]
    genders_parsed = ", ".join(get_gender_name(g) for g in genders)
    print(f"性別 => {genders_parsed}\n")

    show_city_code_table()
    if cities_input := input("請輸入 戶籍地之代號 (選填 | 可用此格式指定多項 : a,f) -> "):
        cities = [x.upper() for x in cities_input.split(",")]
    else:
        cities = list(CITY_CODE_MAPPING.keys())
    cities_parsed = ", ".join(get_city(c)['name'] for c in cities)
    print(f"戶籍 => {cities_parsed}\n")

    generate_ids(genders, cities)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n程式已被中斷.")
    finally:
        input("按任意鍵結束程式...")
