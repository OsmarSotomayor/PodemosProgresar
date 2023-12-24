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

buttonQuery = init_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')
buttonQuery.click()

buttonManual = init_element(AppiumBy.ACCESSIBILITY_ID,
                            'RECOMENDADO\nManualmente\nLlena la información de\nforma manual')
buttonManual.click()

textboxCURP = init_element(AppiumBy.XPATH,
                           '//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[4]')
textboxCURP.click()
textboxCURP.send_keys("PESC050101HMCXRR06")

textboxFatherName = init_element(AppiumBy.XPATH,
                                 '//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[2]')
textboxFatherName.click()
textboxFatherName.send_keys("PEÑA")

textboxMotherName = init_element(AppiumBy.XPATH,
                                 '//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[3]')
textboxMotherName.click()
textboxMotherName.send_keys("SERRANO")

textboxName = init_element(AppiumBy.XPATH,
                           '//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[1]')
textboxName.click()
textboxName.send_keys("CRISTIAN IVAN")

end_x = textboxName.location['x']
end_y = textboxName.location['y']
start_x = textboxMotherName.location['x']
start_y = textboxMotherName.location['y']

scroll_screen(start_x, start_y, end_x, end_y)

textboxDateBirth = init_element(AppiumBy.XPATH, '//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.view.View')
textboxDateBirth.click()

confirmBirthDay = init_element(AppiumBy.ACCESSIBILITY_ID, "Confirmar")
confirmBirthDay.click()

selectEdo = init_element(AppiumBy.ACCESSIBILITY_ID, "Seleccione Estado")

scroll_screen(selectEdo.location['x'], selectEdo.location['y'], textboxDateBirth.location['x'], textboxDateBirth.location['y'])

confirmNumber = init_element(AppiumBy.XPATH, "//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[3]")
confirmNumber.click()
confirmNumber.send_keys("5578291049")

Number = init_element(AppiumBy.XPATH, "//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[1]")
Number.click()
Number.send_keys("5578291049")

selectEdo.click()

edoMex = init_element(AppiumBy.ACCESSIBILITY_ID, "MÉXICO")
edoMex.click()

Continue = init_element(AppiumBy.ACCESSIBILITY_ID, "Continuar")
Continue.click()

street = init_element(AppiumBy.XPATH, "//android.view.View[@content-desc=\"CALLE\nNO. EXTERIOR\nNO. INTERIOR\nCÓDIGO POSTAL\nCOLONIA/POBLACIÓN\nALCALDÍA/ MUNICIPIO\nESTADO\"]/android.widget.EditText[1]")
street.click()
street.send_keys("FRANCISCO IMADERO")

InternNumber = init_element(AppiumBy.XPATH, "//android.view.View[@content-desc=\"CALLE\nNO. EXTERIOR\nNO. INTERIOR\nCÓDIGO POSTAL\nCOLONIA/POBLACIÓN\nALCALDÍA/ MUNICIPIO\nESTADO\"]/android.widget.EditText[2]")
InternNumber.click()
InternNumber.send_keys("1")

ExternNumber = init_element(AppiumBy.XPATH, "//android.view.View[@content-desc=\"CALLE\nNO. EXTERIOR\nNO. INTERIOR\nCÓDIGO POSTAL\nCOLONIA/POBLACIÓN\nALCALDÍA/ MUNICIPIO\nESTADO\"]/android.widget.EditText[3]")
ExternNumber.click()
ExternNumber.send_keys("1")

scroll_screen(InternNumber.location['x'], InternNumber.location['y'], street.location['x'], street.location['y'])

postalCode = init_element(AppiumBy.XPATH, "//android.view.View[@content-desc=\"CALLE\nNO. EXTERIOR\nNO. INTERIOR\nCÓDIGO POSTAL\nCOLONIA/POBLACIÓN\nALCALDÍA/ MUNICIPIO\nESTADO\"]/android.widget.EditText[4]")
postalCode.click()
postalCode.send_keys("56577")

scroll_screen(postalCode.location['x'], postalCode.location['y'], InternNumber.location['x'], InternNumber.location['y'])

colonia = init_element(AppiumBy.ACCESSIBILITY_ID, "SELECCIONE COLONIA")
colonia.click()

selectColonia = init_element(AppiumBy.ACCESSIBILITY_ID, "AMPLIACIÓN SANTA CRUZ TLAPACOYA")
selectColonia.click()

continueToCode = init_element(AppiumBy.ACCESSIBILITY_ID, "Continuar")
continueToCode.click()

sendNip = init_element(AppiumBy.ACCESSIBILITY_ID, "Enviar NIP")
sendNip.click()
