from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import os
import time

def fetch_real_estate_listings():
    print(f"🚀 Thu thập dữ liệu bắt đầu lúc {datetime.now().strftime('%H:%M:%S')}")
    listings = []
    chrome = webdriver.Chrome()
    chrome.get("https://alonhadat.com.vn/")
    chrome.maximize_window()
    wait = WebDriverWait(chrome, 10)

    # Thiết lập tìm kiếm
    try:
        Select(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "province")))).select_by_visible_text("Đà Nẵng")
        Select(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "demand")))).select_by_visible_text("Cho thuê")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btnsearch"))).click()
        time.sleep(3)
    except Exception as e:
        print("❌ Không thể thiết lập bộ lọc:", e)
        chrome.quit()
        return

    def collect_page_data():
        try:
            titles = chrome.find_elements(By.CSS_SELECTOR, ".ct_title a")
            descriptions = chrome.find_elements(By.CSS_SELECTOR, ".content_description")
            areas = chrome.find_elements(By.CSS_SELECTOR, ".ct_dt span")
            prices = chrome.find_elements(By.CSS_SELECTOR, ".price")
            addresses = chrome.find_elements(By.CSS_SELECTOR, ".address")
            images = chrome.find_elements(By.CSS_SELECTOR, ".thumb img")

            for i in range(len(titles)):
                item = {
                    "Tiêu đề": titles[i].text,
                    "Mô tả": descriptions[i].text if i < len(descriptions) else "",
                    "Diện tích": areas[i].text if i < len(areas) else "",
                    "Giá": prices[i].text if i < len(prices) else "",
                    "Địa chỉ": addresses[i].text if i < len(addresses) else "",
                    "Hình ảnh": images[i].get_attribute("src") if i < len(images) else "",
                    "Link": titles[i].get_attribute("href")
                }
                listings.append(item)
        except Exception as err:
            print(f"⚠️ Lỗi khi thu thập dữ liệu trang: {err}")

    page_count = 0
    max_page = 5

    while page_count < max_page:
        collect_page_data()
        page_count += 1
        try:
            next_btn = wait.until(EC.presence_of_element_located((By.LINK_TEXT, ">>")))
            if not next_btn.is_enabled() or "disabled" in next_btn.get_attribute("class"):
                break
            next_btn.click()
            time.sleep(3)
        except Exception as e:
            print("⛔ Không thể chuyển trang hoặc đã đến trang cuối:", e)
            break

    # Lưu dữ liệu
    today = datetime.now().strftime("%Y-%m-%d")
    output_dir = "C:\\Users\\Admin\\OneDrive\\Documents\\BAITAPLON"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"bai_tap_{today}.xlsx"
    filepath = os.path.join(output_dir, filename)
    pd.DataFrame(listings).to_excel(filepath, index=False, engine='openpyxl')

    print(f"✅ Đã lưu {len(listings)} mục vào file: {filepath}")
    chrome.quit()

def schedule_crawling(hour=6, minute=00):
    print("🕓 Đang đợi tới giờ quy định để bắt đầu crawler...")
    while True:
        current = datetime.now()
        if current.hour == hour and current.minute == minute:
            fetch_real_estate_listings()
            time.sleep(65)
        else:
            time.sleep(20)

if __name__ == "__main__":
    schedule_crawling()
