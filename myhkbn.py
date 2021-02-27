#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import datetime

from common.sendemail import SendEmail

driver = webdriver.Chrome(executable_path=&quot;/usr/local/bin/chromedriver&quot;)
driver.set_window_size(1720,1000)
wait = WebDriverWait(driver, 120)
# sendEmail = SendEmail(&quot;test email&quot;)
# sendEmail.send()
ErrorCount = {&apos;Login&apos;: 0, &apos;DashBoard&apos;: 0, &apos;AccountOverView&apos;: 0, &apos;PlanList&apos;: 0, &apos;CouponList&apos;: 0, &apos;Logout&apos;: 0}
Errormessage = &apos;&apos;
ErrorTitle = &apos;&apos;

