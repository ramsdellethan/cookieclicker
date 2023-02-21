import keyboard
import pyautogui
import time

def main():
    oppgradere_farge = (211, 165, 123)
    #oppgradere_pos = (2210, 107)

    kjøpe_mer_farge = (102, 255, 102)
    #kjøpe_mer_bredde = (2250,2380)
    #kjøpe_mer_høyde = (285, 1435)

    gull_kjeks_farge = (187, 150, 70)
    #gull_kjeks_bredde = (30,2100)
    #gull_kjeks_høyde = (40, 1420)

    Q_trykket = False
    A_trykket = False
    Z_trykket = False
    E_trykket = False

    nedtelling = 0
    O_nedtelling = 0


    ###########
    #Hoved loop
    ###########

    while True:

        #######################################
        #Sjekke om du har trykkket ned en knapp
        #######################################

        if keyboard.is_pressed("å"):
            exit()


        if keyboard.is_pressed("q"):
            Q_trykket = True

        elif keyboard.is_pressed("w"):
            Q_trykket = False


        if keyboard.is_pressed("a"):
            A_trykket = True

        elif keyboard.is_pressed("s"):
            A_trykket = False


        if keyboard.is_pressed("z"):
            Z_trykket = True

        elif keyboard.is_pressed("x"):
            Z_trykket = False


        if keyboard.is_pressed("e"):
            E_trykket = True

        elif keyboard.is_pressed("r"):
            E_trykket = False


        ####################
        #Se etter gull kjeks
        ####################
        if nedtelling <= 0:
            Cookie_screenshot = pyautogui.screenshot()

            for x in range(2100, 30, -1):
                for y in range(1420, 40, -1):

                    if Cookie_screenshot.getpixel((x, y)) == gull_kjeks_farge:
                        pyautogui.click(x, y)
                        time.sleep(0.1)
                        pyautogui.click(380, 600)
            nedtelling = 100


        ######################################
        #Sjekke om du kan kjøpe oppgraderinger
        ######################################

        if Z_trykket == True or E_trykket == True:
            Cookie_screenshot = pyautogui.screenshot()
            if Cookie_screenshot.getpixel((2210, 107)) == oppgradere_farge:
                pyautogui.click(2210, 107)


        ##################################
        #Sjekke om du kan kjøpe mer av noe
        ##################################

        if A_trykket == True or E_trykket == True:
            if O_nedtelling <= 0:

                Cookie_screenshot = pyautogui.screenshot()

                for x in range(2250, 2380):
                    for y in range(1435, 285, -1):

                        if Cookie_screenshot.getpixel((x, y)) == kjøpe_mer_farge:
                            pyautogui.click(x, y)
                            time.sleep(0.1)
                            pyautogui.click(380, 600)
                            Cookie_screenshot = pyautogui.screenshot()
                O_nedtelling = 10


        if Q_trykket == True or E_trykket == True:
            pyautogui.tripleClick(380, 600)


        nedtelling -= 1
        O_nedtelling -= 1*1


if __name__ == '__main__':
    main()