from micropi import OLED

def main():
    o = OLED()
    ip = o.get_ip_address()
    o.stats()

if __name__ == "__main__":
    # execute only if run as a script
    main()

