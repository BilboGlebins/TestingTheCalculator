from selenium.webdriver.common.by import By


class CalculatorLocators:

    #Status for state
    STATUSZERO = (By.XPATH,  '//pre[normalize-space()=\'{"statusCode": 0, "state": "O\\u041a"}\']')

    #All status for addition
    STATUSONEADD = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 1, "statusMessage": ": addition - \')]')
    STATUSTWOADD = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 2, "statusMessage": ": addition - \')]')
    STATUSTHREEADD = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 3, "statusMessage": ": addition - \')]')
    STATUSFOURADD = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 4, "statusMessage": ": addition - \')]')
    STATUSFIVEADD = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 5, "statusMessage": ": addition - \')]')

    # All status for multiplication
    STATUSONEMULT = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 1, "statusMessage": ": multiplication - \')]')
    STATUSTWOMULT = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 2, "statusMessage": ": multiplication - \')]')
    STATUSTHREEMULT = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 3, "statusMessage": ": multiplication - \')]')
    STATUSFOURMULT = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 4, "statusMessage": ": multiplication - \')]')
    STATUSFIVEMULT = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 5, "statusMessage": ": multiplication - \')]')

    # All status for division
    STATUSONEDIVIS = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 1, "statusMessage": ": division - \')]')
    STATUSTWODIVIS = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 2, "statusMessage": ": division - \')]')
    STATUSTHREEDIVIS = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 3, "statusMessage": ": division - \')]')
    STATUSDFOURDIVIS = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 4, "statusMessage": ": division - \')]')
    STATUSFIVEDIVIS = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 5, "statusMessage": ": division - \')]')

    # All status for
    STATUSONEREMIN = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 1, "statusMessage": ": remainder - \')]')
    STATUSTWOREMIN = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 2, "statusMessage": ": remainder - \')]')
    STATUSTHREEREMIN = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 3, "statusMessage": ": remainder - \')]')
    STATUSFOURREMIN = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 4, "statusMessage": ": remainder - \')]')
    STATUSFIVEREMIN = (By.XPATH, '//pre[contains(text(),\'{"statusCode": 5, "statusMessage": ": remainder - \')]')






