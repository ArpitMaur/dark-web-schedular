from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import start_xvfb, stop_xvfb
from os.path import join, dirname, realpath
from driverpath import torPath

def headless_visit():
    # out_img = join(dirname(realpath(_file_)), "headless_screenshot.png")
    # start a virtual display
    xvfb_display = start_xvfb()
    with TorBrowserDriver(torPath) as driver:
    # with TorBrowserDriver("/home/tor-browser") as driver:
        driver.load_url("https://check.torproject.org")
        print(driver.page_source)
        # driver.get_screenshot_as_file(out_img)
        # print("Screenshot is saved as %s" % out_img)

    stop_xvfb(xvfb_display)

headless_visit()