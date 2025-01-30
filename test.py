from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome WebDriver 실행 (직접 경로 지정)
service = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")  # Google 페이지 열기
print(driver.title)  # 페이지 제목 출력

driver.quit()  # 브라우저 닫기
