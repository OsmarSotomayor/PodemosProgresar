import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Redmi9A",
        "automationName": "UiAutomator2",
        "appPackage": "prod.horus.podemos",
        "appActivity": "horus.podemos.horus.MainActivity"

    }
)

appium_server_url = 'http://localhost:4723/wd/hub'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)


def init_element(find_element_by, value):
    time_to_wait = 60
    try:
        element = WebDriverWait(driver, time_to_wait).until(
            EC.presence_of_element_located((find_element_by, value))
        )
        return element
    except:
        print("El elemento:  ", value, " No fue encontrado")


def scroll_screen(start_x, start_y, end_x, end_y):
    touch = TouchAction(driver)
    touch.press(x=start_x, y=start_y).wait(2000).move_to(x=end_x, y=end_y).release().perform()


buttonGetAccess = init_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
buttonGetAccess.click()

time.sleep(15)

buttonInitSessionGoogle = init_element(AppiumBy.XPATH,
                                       '//android.widget.Button[@content-desc="Iniciar sesión con Google"]')
buttonInitSessionGoogle.click()

buttonSelectEmail = init_element(AppiumBy.XPATH,
                                 '//android.widget.TextView[@resource-id=\"com.google.android.gms:id/account_name\" and @text=\"c.pena@podemos.mx\"]')
buttonSelectEmail.click()

buttonMaps = init_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
buttonMaps.click()

buttonQueryByGroup = init_element(AppiumBy.ACCESSIBILITY_ID, "Consulta\nGrupal")
buttonQueryByGroup.click()

addExistingGroup = init_element(AppiumBy.ACCESSIBILITY_ID, "Agregar a un grupo existente")
addExistingGroup.click()

serchGroup = init_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
serchGroup.click()
serchGroup.send_keys("t")
time.sleep(3)

groupOne = init_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc=\"Utilizar\"])[1]")
groupThree = init_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc=\"Utilizar\"])[3]")

scroll_screen(groupThree.location['x'], groupThree.location['y'], groupOne.location['x'], groupOne.location['y'])

groupFive = init_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc=\"Utilizar\"])[4]")

scroll_screen(groupFive.location['x'], groupFive.location['y'], groupThree.location['x'], groupThree.location['y'])

groupT = init_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc=\"Utilizar\"])[4]")
groupT.click()

addMember = init_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]")
addMember.click()

existingProspectus = init_element(AppiumBy.ACCESSIBILITY_ID, "Prospecto existente")
existingProspectus.click()

member = "06 Nov\nLOURDES  PEREZ TALAVERA \nRECHAZADO"
member2 = "06 Nov\nMARIBEL  MEDINA JUAREZ \nRECHAZADO"
selectMember = init_element(AppiumBy.ACCESSIBILITY_ID, member)
selectMember.click()
time.sleep(5)


