# PS5 Digital Edition - Gamestop
import selenium
import random
from selenium import webdriver
import pyautogui
import time


def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)


    browser = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\smith\IdeaProjects\PS5Finder\chromedriver.exe')
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    browser.set_page_load_timeout(10)
    return browser


def selectTab(site, digital):
    tabs = _browser.window_handles
    index = -1
    if site == 'gamestop':
        index = 0
    elif site == 'bestbuy':
        index = 2
    elif site == 'sony':
        index = 4
    elif site == 'walmart':
        index = 6
    elif site == 'adorama':
        index = 8

    if index > -1 and not digital:
        index += 1
    elif site == 'amazon':
        index = 10
    elif site == 'bhphotovideo':
        index = 11

    try:
        _browser.switch_to.window(tabs[index])
        return True
    except Exception as e:
        return False


def verifyHold(walmart):
    x = 942 if walmart else 400
    y = 420 if walmart else 400
    pyautogui.moveTo(x, y, 2)
    time.sleep(1)
    cleared = False
    dur = 2
    while not cleared and dur < 15:
        pyautogui.mouseDown(x, y, duration=dur)
        time.sleep(dur)
        pyautogui.moveTo(random.randint(100, 1500), random.randint(100, 1500), 2)
        time.sleep(5)
        # Check if element exists
        try:
            if walmart:
                if _browser.find_element_by_class_name('heading-d').text == 'Verify your identity':
                    dur += 1
            elif _browser.find_element_by_class_name('page-title').text == 'Please verify you are a human':
                dur += 1
        except Exception as e:
            cleared = True


def gotoLink(link=''):
    try:
        if not link:
            _browser.refresh()
        else:
            _browser.get(link)
    except Exception as e:
        _browser.execute_script('window.stop()')

_urls = {
    "gamestop": {
        True: 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html',
        False: 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New'
    },
    "adorama": {
        True: 'https://www.adorama.com/so3005719.html?sterm=SHU0A7Vm8xyLR%3ANytMUkozQYUkBUfSXBLQ7KRM0&utm_source=rflaid913479',
        False: 'https://www.adorama.com/so3005718.html?sterm=SHU0A7Vm8xyLR%3ANytMUkozQYUkBUfkwxLQ7KRM0&utm_source=rflaid913479'
    },
    "bestbuy": {
        True: 'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161',
        False: 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'
    },
    "sony": {
        True: 'https://direct.playstation.com/en-us/consoles/console/playstation5-digital-edition-console.3005817',
        False: 'https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816'
    },
    "walmart": {
        True: 'https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition-Video-Game-Consoles/979738052',
        False: 'https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/994712501'
    },
    "bhphotovideo": 'https://www.bhphotovideo.com/c/product/1595083-REG/sony_3005718_playstation_5_gaming_console.htmll',
    "amazon": 'https://www.amazon.com/gp/product/B08FC6MR62?tag=georiot-us-default-20&ascsubtag=grd-us-1104673013010889200-20&geniuslink=true'
}



numConsoles = 12
_browser = getBrowser()

for x in range(numConsoles):
    _browser.execute_script("window.open('about:blank', 'tab" + str(x) + "');")

_browser.switch_to.window("")
_browser.close()


def gamestop(digital):
    edition = 'Digital' if digital else 'Standard'
    if not selectTab('gamestop', digital):
        return ''

    if str(_browser.current_url) == "about:blank":
        gotoLink(_urls['gamestop'][digital])
    else:
        gotoLink()

    elementLoaded = False
    timeSlept = 0
    while timeSlept < 10:
        try:
            btn = _browser.find_element_by_id("add-to-cart")
            if btn.text.lower() != "select condition":
                elementLoaded = True
                break
        except Exception as e:
            time.sleep(1)
            timeSlept += 1

    if elementLoaded:
        btnText = _browser.find_element_by_id("add-to-cart").text.lower()
        if btnText != "not available":
            return '\n\nPS5 ' + edition + ' at Gamestop:\n' + _urls['gamestop'][digital]
    return ''


def bestbuy(digital):
    edition = 'Digital' if digital else 'Standard'
    if not selectTab('bestbuy', digital):
        return ''

    if str(_browser.current_url) == "about:blank":
        gotoLink(_urls['bestbuy'][digital])
    else:
        gotoLink()

    # Wait until price loads
    try:
       btn = _browser.find_element_by_class_name("add-to-cart-button")
       if btn.text == "Sold Out":
           return ''
       else:
           return '\n\nPS5 ' + edition + ' at Best Buy:\n' + _urls['bestbuy'][digital]
    except Exception as e:
        print('Best Buy Detected Bot')


def sony(digital):
    edition = 'Digital' if digital else 'Standard'
    if not selectTab('sony', digital):
        return ''

    if str(_browser.current_url) == "about:blank":
        gotoLink(_urls['sony'][digital])
    else:
        try:
            if _browser.find_element_by_class_name('page-title').text == 'Please verify you are a human':
                input("Verify Sony, Then press enter")
        except Exception as e:
            pass
        finally:
            gotoLink()

    try:
        schema = _browser.find_element_by_css_selector("div.button-placeholder div link")
        if str(schema.get_attribute('href')) == 'https://schema.org/OutOfStock':
            return ''
        else:
            return '\n\nPS5 ' + edition + ' at Sony Direct:\n' + _urls['sony'][digital]
    except Exception as e:
        print('Sony Direct Detected Bot')
        return ''


def adorama(digital):

    edition = 'Digital' if digital else 'Standard'
    if not selectTab('adorama', digital):
        return ''

    if str(_browser.current_url) == "about:blank":
        gotoLink(_urls['adorama'][digital])
    else:
        try:
            if _browser.find_element_by_class_name('page-title').text == 'Please verify you are a human':
                verifyHold(False)
        except Exception as e:
            pass
        finally:
            gotoLink()

    try:
        if _browser.find_element_by_class_name('add-to-cart').text == 'Temporarily not available':
            return ''
        else:
            return '\n\nPS5 ' + edition + ' at Adorama:\n' + _urls['adorama'][digital]
    except:
        print('Adorama detected bot')


def amazon():
    edition = 'Digital'
    if not selectTab('amazon', True):
        return ''

    if str(_browser.current_url) == "about:blank":
        gotoLink(_urls['amazon'])
    else:
        gotoLink()

    try:
        _browser.find_element_by_id('buy-now-button')
        print('Available At Amazon')
        return '\n\nPS5 ' + edition + ' at Amazon:\n' + _urls['amazon']
    except Exception as e:
        try:
            _browser.find_element_by_class_name('a-list-item')
        except Exception as e:
            print('Amazon Detected Bot')

        return ''


# Bot Blocked
def bhphotovideo():
    edition = 'Standard'
    if not selectTab('bhphotovideo', False):
        return ''

    if str(_browser.current_url) == "about:blank":
        gotoLink(_urls['bhphotovideo'])
    else:
        try:
            if _browser.find_element_by_class_name('page-title').text == 'Please verify you are a human':
                verifyHold(False)
        except Exception as e:
            pass
        finally:
            gotoLink()
    try:
        stock = str(_browser.find_element_by_css_selector('[data-selenium="stockStatus"]').text)
        print(stock)
        if stock == "In Stock":
            return '\n\nPS5 ' + edition + ' at Adorama:\n' + _urls['bhphotovideo']
    except Exception as e:
        print('B&H Photo Video Detected Bot')
        return ''


def walmart(digital):
    edition = 'Digital' if digital else 'Standard'
    if not selectTab('walmart', digital):
        return ''

    if str(_browser.current_url) == "about:blank":
        gotoLink(_urls['walmart'][digital])
    else:
        try:
            if _browser.find_element_by_class_name('heading-d').text == 'Verify your identity':
                verifyHold(True)
        except Exception as e:
            pass
        finally:
            gotoLink()

    # Wait until price loads
    try:
        element = _browser.find_element_by_class_name('spin-button-children')
        if element.text == "Add to cart":
            return '\n\nPS5 ' + edition + ' at Sony Direct:\n' + _urls['walmart'][digital]
        return ''
    except:
        print('Walmart Detected Bot')
        return ''


def scrapeAll():
    return [
        gamestop(True), gamestop(False),
        bestbuy(True),  bestbuy(False),
        sony(True),     sony(False),
        walmart(True),  walmart(False),
        adorama(True),  adorama(False),
        amazon(),
        bhphotovideo()
    ]

