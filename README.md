# tw-id-generator

台灣身份證字號字典生成/產生器

![](./demo.png)

## 功能

根據性別與戶籍地資訊生成合法的台灣身分證字號，並存到檔案。

## 目的

許多網站(如: 學校)及電子資料(如: 電子對帳單)的預設密碼為身分證字號或與其相關之組合，

此腳本可幫助紅隊/滲透測試團隊根據目標信息生成合法的身分證字號到字典檔，來檢測此風險。

## 使用方法

### 1. 使用已包裝之執行檔

- [下載連結](https://github.com/opabravo/tw-id-generator/releases/download/latest/tw_id_gen.exe)

### 2. 使用 Python 執行

- 安裝 Python 3.6 以上版本

```bash
# Build c extension module
$ python setup.py build_ext --inplace
# Run The Script
$ python tw_id_gen.py
```

## 身分證字號規律說明

中華民國國民身分證字號共有10碼，

其中第1碼英文字母代表為縣市，

而第1個數字為性別碼。1為男生、2為女生。

第3碼至第9碼為依照出生登記順序編號之流水號碼。

最後一碼也就是最後一個數字為驗證碼，

用來檢驗身分證字號是否正確。

詳細資訊參考: https://wisdom-life.in/article/taiwain-id-explanation

## License

[MIT](./LICENSE)