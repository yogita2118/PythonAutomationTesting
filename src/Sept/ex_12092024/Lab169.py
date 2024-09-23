from browserPackage.OpenBrowser import start_Browser
from browserPackage.CloseBrowser import close_Browser

def test_case():
    start_Browser()
    print("I am executing a Code TC 1")
    close_Browser()

test_case()