#dr.lixxard
import requests
def main():
    inp=input("\n\nWelcome!\n\nEnter A Url To Pull Response From\n\n---------->>>:")
    try:
        r=requests.get(inp)
        html=r.text
    except Exception as E:
        print(str(E))
        setup()
    ask=input("[SUCCESS] Would You Like To Save To HTML File?(Y/N):")
    if "y" or "Y" in ask:
        print("Writing File...")
        f=open("Captured_Response.html","w+")
        f.write(str("""<!--SAVED FROM """+inp+"-->"+"""\n\n-------------------------------------\n\n"""+html))
        f.close()
        wait=input("\n\nDONE\n\nPRESS ENTER")
        main()
    else:
        print("""<!--SAVED FROM """+inp+"-->"+"""\n\n-------------------------------------\n\n"""+html)
        wait=input("\n\nPRESS ENTER")
        main()
def setup():
    main()
setup()
