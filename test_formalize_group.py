import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction

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


buttonGetAccessPhotos = init_element(AppiumBy.ID,
                                     'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
buttonGetAccessPhotos.click()
time.sleep(3)
getAccessAudio = init_element(AppiumBy.ID,
                              "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
getAccessAudio.click()
time.sleep(5)

buttonInitSessionGoogle = init_element(AppiumBy.XPATH,
                                       '//android.widget.Button[@content-desc="Iniciar sesión con Google"]')
buttonInitSessionGoogle.click()

buttonSelectEmail = init_element(AppiumBy.XPATH,
                                 '//android.widget.TextView[@resource-id=\"com.google.android.gms:id/account_name\" and @text=\"c.pena@podemos.mx\"]')
buttonSelectEmail.click()

buttonMaps = init_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
buttonMaps.click()


def formalize_group(name_group):
    buttonQueryByGroup = init_element(AppiumBy.ACCESSIBILITY_ID, "Consulta\nGrupal")
    buttonQueryByGroup.click()

    addExistingGroup = init_element(AppiumBy.ACCESSIBILITY_ID, "Agregar a un grupo existente")
    addExistingGroup.click()

    search_group = init_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    search_group.click()
    search_group.send_keys(name_group)
    time.sleep(3)

    select_group = init_element(AppiumBy.ACCESSIBILITY_ID, "Utilizar")
    select_group.click()

    formalizeGroup = init_element(AppiumBy.ACCESSIBILITY_ID, "Formalizar grupo")
    formalizeGroup.click()
    time.sleep(5)

    accept = init_element(AppiumBy.ACCESSIBILITY_ID, "Aceptar")
    accept.click()


def fill_personal_data(number, email_personal):
    numberTelephone = init_element(AppiumBy.XPATH,
                                   "//android.widget.ScrollView/android.view.View[4]/android.view.View/android.widget.EditText[1]")
    numberTelephone.clear()
    numberTelephone.click()
    numberTelephone.send_keys(number)

    estateCivil = init_element(AppiumBy.ACCESSIBILITY_ID, "ESTADO CIVIL*\nSelecciona Opcion")
    estateCivil.click()

    choseEstateCivil = init_element(AppiumBy.ACCESSIBILITY_ID, "Union Libre")
    choseEstateCivil.click()

    scholarshipLevel = init_element(AppiumBy.ACCESSIBILITY_ID, "ESCOLARIDAD*\nSelecciona Opcion")
    scholarshipLevel.click()

    choseScholarshipLevel = init_element(AppiumBy.ACCESSIBILITY_ID, "Licenciatura Incompleta")
    choseScholarshipLevel.click()

    email = init_element(AppiumBy.XPATH,
                         "//android.widget.ScrollView/android.view.View[4]/android.view.View/android.widget.EditText[2]")
    email.click()
    email.clear()
    email.send_keys(email_personal)
    scroll_screen(email.location['x'], email.location['y'], estateCivil.location['y'], estateCivil.location['y'])

    confirmNumber = init_element(AppiumBy.XPATH, "//android.widget.EditText[@text=\"7778291049\"]")
    confirmNumber.clear()
    confirmNumber.send_keys(number)

    save = init_element(AppiumBy.ACCESSIBILITY_ID, "Guardar")
    save.click()


def fill_address_data(spouse_name):
    ageOfResidence = init_element(AppiumBy.ACCESSIBILITY_ID, "ANTIGÜEDAD EN EL DOMICILIO*\nSelecciona Opcion")
    ageOfResidence.click()

    choseOneYear = init_element(AppiumBy.ACCESSIBILITY_ID, "1 año")
    choseOneYear.click()

    typeOfHouse = init_element(AppiumBy.ACCESSIBILITY_ID, "TIPO DE DOMICILIO*\nSelecciona Opcion")
    typeOfHouse.click()

    ownHouse = init_element(AppiumBy.ACCESSIBILITY_ID, "Propia")
    ownHouse.click()

    completeName = init_element(AppiumBy.XPATH,
                                "//android.widget.ScrollView/android.view.View[4]/android.view.View/android.widget.EditText[1]")
    completeName.click()
    completeName.send_keys(spouse_name)

    scroll_screen(completeName.location['x'], completeName.location['y'], ageOfResidence.location['x'],
                  ageOfResidence.location['y'])

    numberPhone = init_element(AppiumBy.XPATH,
                               "//android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText[2]")
    numberPhone.click()
    numberPhone.send_keys("5527822708")

    selectRelationship = init_element(AppiumBy.ACCESSIBILITY_ID, "PARENTESCO*\nSelecciona Opcion")
    selectRelationship.click()

    father = init_element(AppiumBy.ACCESSIBILITY_ID, "Padre")
    father.click()

    selectDependents = init_element(AppiumBy.ACCESSIBILITY_ID, "DEPENDIENTES*\nSelecciona Opcion")
    selectDependents.click()

    zero = init_element(AppiumBy.ACCESSIBILITY_ID, "0")
    zero.click()

    characteristicsOfTheHouse = init_element(AppiumBy.XPATH,
                                             "//android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText[3]")
    characteristicsOfTheHouse.click()
    characteristicsOfTheHouse.send_keys("caracteristicas de la ubicacion")

    scroll_screen(characteristicsOfTheHouse.location['x'], characteristicsOfTheHouse.location['y'],
                  numberPhone.location['x'], numberPhone.location['y'])

    reference = init_element(AppiumBy.XPATH,
                             "//android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText[2]")
    reference.click()
    reference.send_keys("REFERENCIAS")

    nextPage = init_element(AppiumBy.ACCESSIBILITY_ID, "Siguiente")
    nextPage.click()


def fill_economic_data(week_incomes, other_incomes, how_much_can_pay):
    initialData = init_element(AppiumBy.XPATH,
                               "//android.view.View[@content-desc=\"COMERCIANTE\nSi\nNo\n¿VA INICIAR NEGOCIO?*\nSi\nNo\"]/android.widget.RadioButton[1]")
    initialData.click()

    economicActivity = init_element(AppiumBy.ACCESSIBILITY_ID, "ACTIVIDAD ECONÓMICA*\nSelecciona Opcion")
    economicActivity.click()

    choseIndustries = init_element(AppiumBy.ACCESSIBILITY_ID, "Alimentos")
    choseIndustries.click()

    additionalActivity = init_element(AppiumBy.ACCESSIBILITY_ID, "ACTIVIDAD ADICIONAL*\nSelecciona Opcion")
    additionalActivity.click()

    choseActivity = init_element(AppiumBy.ACCESSIBILITY_ID, "Traslado o custodio de dinero o valores")
    choseActivity.click()

    businessTime = init_element(AppiumBy.ACCESSIBILITY_ID, "ANTIGÜEDAD DEL NEGOCIO*\nSelecciona Opcion")
    businessTime.click()

    choseTime = init_element(AppiumBy.ACCESSIBILITY_ID, "6 años")
    choseTime.click()

    daysOfSale = init_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc=\"M\"])[2]")
    daysOfSale.click()

    scroll_screen(daysOfSale.location['x'], daysOfSale.location['y'], initialData.location['x'],
                  initialData.location['y'])

    businessLocation = init_element(AppiumBy.ACCESSIBILITY_ID, "UBICACIÓN DEL NEGOCIO*\nSelecciona Opcion")
    businessLocation.click()

    choseLocation = init_element(AppiumBy.ACCESSIBILITY_ID, "PUESTO IMPROVISADO EN TIANGUIS")
    choseLocation.click()

    businessAddress = init_element(AppiumBy.XPATH,
                                   "//android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText[1]")
    businessAddress.click()
    businessLocation.clear()
    businessAddress.send_keys("VI")

    scroll_screen(businessAddress.location['x'], businessAddress.location['y'], daysOfSale.location['x'],
                  daysOfSale.location['y'])

    weekIncomes = init_element(AppiumBy.XPATH,
                               "//android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText[2]")
    weekIncomes.click()
    weekIncomes.send_keys(week_incomes)

    otherIncomes = init_element(AppiumBy.ACCESSIBILITY_ID, "OTROS INGRESOS SEMANALES")
    otherIncomes.click()
    otherIncomes.send_keys(other_incomes)

    sendIncomes = init_element(AppiumBy.XPATH,
                               "//android.view.View[@content-desc=\"400, OTROS INGRESOS SEMANALES\"]/android.widget.EditText")
    sendIncomes.send_keys(other_incomes)

    scroll_screen(otherIncomes.location['x'], otherIncomes.location['y'], businessAddress.location['x'],
                  businessAddress.location['y'])

    time.sleep(5)

    extraIncome = init_element(AppiumBy.ACCESSIBILITY_ID, "FUENTE DE OTROS INGRESOS*\nSelecciona Opcion")
    extraIncome.click()

    NA = init_element(AppiumBy.ACCESSIBILITY_ID, "NA")
    NA.click()

    howMuchCanPay = init_element(AppiumBy.ACCESSIBILITY_ID,
                                 "Quedan 6 caracteres")
    howMuchCanPay.click()
    howMuchCanPay.send_keys(how_much_can_pay)

    send = init_element(AppiumBy.XPATH,
                        "//android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText[2]")
    send.click()
    send.send_keys(how_much_can_pay)
    time.sleep(10)

    scroll_screen(extraIncome.location['x'], extraIncome.location['y'], otherIncomes.location['x'],
                  otherIncomes.location['y'])

    nextForm = init_element(AppiumBy.ACCESSIBILITY_ID, "Siguiente")
    nextForm.click()


def fill_personal_references(name_of_reference, number_of_reference, number_phone_reference):
    personal_reference_one = init_element(AppiumBy.ACCESSIBILITY_ID, "Referencia personal 1")
    personal_reference_one.click()

    number_local_ = init_element(AppiumBy.XPATH,
                                 value="//android.view.View[@content-desc=\"Referencia personal 1\"]/android.view.View/android.view.View/android.widget.EditText[2]")
    number_local_.click()
    number_local_.send_keys(number_of_reference)

    relationship = init_element(AppiumBy.ACCESSIBILITY_ID, "PARENTESCO\nSelecciona Opcion")
    relationship.click()

    family = init_element(AppiumBy.ACCESSIBILITY_ID, "Familiar")
    family.click()

    name = init_element(AppiumBy.XPATH,
                        "//android.view.View[@content-desc=\"Referencia personal 1\"]/android.view.View/android.view.View/android.widget.EditText[1]")
    name.click()
    name.send_keys(name_of_reference)

    scroll_screen(number_local_.location['x'], number_local_.location['y'], name.location['x'], name.location['y'])
    time.sleep(2)

    number_phone = init_element(AppiumBy.XPATH,
                                "//android.view.View[@content-desc=\"Referencia personal 1\"]/android.view.View/android.view.View/android.widget.EditText[2]")
    number_phone.click()
    number_phone.send_keys(number_phone_reference)

    scroll_screen(number_phone.location['x'], number_phone.location['y'], number_local_.location['x'],
                  number_local_.location['y'])

    personal_reference_two = init_element(AppiumBy.ACCESSIBILITY_ID, "Referencia personal 2")
    personal_reference_two.click()

    scroll_screen(personal_reference_two.location['x'], personal_reference_two.location['y'],
                  number_phone.location['x'], number_phone.location['y'])

    name_two = init_element(AppiumBy.XPATH,
                            "//android.view.View[@content-desc=\"Referencia personal 2\"]/android.view.View/android.view.View/android.widget.EditText[1]")
    name_two.click()
    name_two.send_keys(name_of_reference)

    kin_of_relationship_two = init_element(AppiumBy.ACCESSIBILITY_ID, "PARENTESCO\nSelecciona Opcion")
    kin_of_relationship_two.click()

    friend = init_element(AppiumBy.ACCESSIBILITY_ID, "Amistad")
    friend.click()

    number_phone_two = init_element(AppiumBy.XPATH,
                                    "//android.view.View[@content-desc=\"Referencia personal 2\"]/android.view.View/android.view.View/android.widget.EditText[3]")
    number_phone_two.click()
    number_phone_two.send_keys(number_phone_reference)

    number_local_two = init_element(AppiumBy.XPATH,
                                    "//android.view.View[@content-desc=\"Referencia personal 2\"]/android.view.View/android.view.View/android.widget.EditText[2]")
    number_local_two.click()
    number_local_two.send_keys(number_of_reference)

    scroll_screen(number_local_two.location['x'], number_local_two.location['y'], kin_of_relationship_two.location['x'],
                  kin_of_relationship_two.location['y'])
    scroll_screen(number_phone_two.location['x'], number_phone_two.location['y'], kin_of_relationship_two.location['x'],
                  kin_of_relationship_two.location['y'])

    next = init_element(AppiumBy.ACCESSIBILITY_ID, "Siguiente")
    next.click()


def fill_credit_request():
    isThisYorFirstCredit = init_element(AppiumBy.XPATH,
                                        "//android.view.View[@content-desc=\"¿SERÁ ESTE SU\nPRIMER CRÉDITO?\nSi\nNo\n¿TIENE OTROS CRÉDITOS\nACTIVOS?\nSi\nNo\"]/android.widget.RadioButton[1]")
    isThisYorFirstCredit.click()

    creditAmount = init_element(AppiumBy.XPATH,
                                "//android.widget.ScrollView/android.view.View[4]/android.view.View/android.widget.EditText[1]")
    creditAmount.click()
    creditAmount.send_keys(5000)

    scroll_screen(isThisYorFirstCredit.location["x"], isThisYorFirstCredit.location["y"], creditAmount.location["x"],
                  creditAmount.location["y"])

    isTheOwnerOfTheResources = init_element(AppiumBy.XPATH,
                                            "//android.view.View[@content-desc=\"¿ES PROPIETARIO REAL DE LOS RECURSOS?*\nSi\nNo\"]/android.widget.RadioButton[1]")
    isTheOwnerOfTheResources.click()

    scroll_screen(isTheOwnerOfTheResources.location["x"], isTheOwnerOfTheResources.location["y"],
                  isThisYorFirstCredit.location["x"], isThisYorFirstCredit.location["y"])

    time.sleep(3)
    destinyOfResources = init_element(AppiumBy.XPATH,
                                      "//android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText[3]")
    destinyOfResources.click()
    destinyOfResources.send_keys("negocio")

    originOfResources = init_element(AppiumBy.XPATH,
                                     "//android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText[2]")
    originOfResources.click()
    originOfResources.send_keys("ventas")

    scroll_screen(destinyOfResources.location["x"], destinyOfResources.location["y"],
                  isTheOwnerOfTheResources.location["x"], isTheOwnerOfTheResources.location["y"])

    willPayInAdvance = init_element(AppiumBy.XPATH,
                                    "//android.view.View[@content-desc=\"¿PRETENDE REALIZAR\n PREPAGOS O LIQUIDAR\n ANTICIPADAMENTE?*\nSi\nNo\n¿ES PERSONA FISICA\nCON ACTIDAD\nEMPRESARIAL?\nSi\nNo\"]/android.widget.RadioButton[1]")
    willPayInAdvance.click()

    politicallyExposed = init_element(AppiumBy.XPATH,
                                      "//android.view.View[@content-desc=\"¿ES PERSONA POLITICAMENTE EXPUESTA?\nSi\nNo\"]/android.widget.RadioButton[2]")

    scroll_screen(politicallyExposed.location["x"], politicallyExposed.location["y"], willPayInAdvance.location["x"],
                  willPayInAdvance.location["y"])

    save = init_element(AppiumBy.ACCESSIBILITY_ID, "Guardar")
    save.click()


# formalize_group("PEQUES")

myGroups = init_element(AppiumBy.ACCESSIBILITY_ID, "Mis\nGrupos")
myGroups.click()
time.sleep(12)

# searchGroup = init_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
# searchGroup.click()
# searchGroup.send_keys("PEQUES")
# time.sleep(5)

stendhalGroup = init_element(AppiumBy.ACCESSIBILITY_ID, "5 INTEGRANTE(S)\nSTENDHAL\nEN APROBACION")
galeGroup = init_element(AppiumBy.ACCESSIBILITY_ID, "5 INTEGRANTE(S)\nGALE\nPENDIENTE")

scroll_screen(stendhalGroup.location['x'], stendhalGroup.location['y'], galeGroup.location['x'],
              galeGroup.location['y'])

selectGroup = init_element(AppiumBy.ACCESSIBILITY_ID, "5 INTEGRANTE(S)\nLAS PEQUES\nPENDIENTE")
selectGroup.click()

member = "//android.view.View[@content-desc=\"BERENICE  PALMA PALMA\nINCOMPLETA\"]/android.widget.Button"
severino = "//android.view.View[@content-desc=\"CARROYO  MONDRAGON SEVERINO\nINCOMPLETA\"]/android.widget.Button"
maria = "//android.view.View[@content-desc=\"MARI DEL CARMEN  GARCIA ESQUIVEL\nINCOMPLETA\"]/android.widget.Button"
selectMember = init_element(AppiumBy.XPATH,
                            maria)
selectMember.click()
time.sleep(5)

editSCI = init_element(AppiumBy.ACCESSIBILITY_ID, "Editar SCI")
editSCI.click()
time.sleep(10)


fill_personal_data(7778291049, "oscaromarfloressotomayor@gmail.com")
time.sleep(5)

fill_address_data("GUSTAVO ADOLFO BEQUER")
time.sleep(5)

fill_economic_data(1200, 400, 500)
time.sleep(5)

fill_personal_references("Oscar Wilde", 5559724343, 5527822708)
time.sleep(5)

fill_credit_request()
time.sleep(7)

