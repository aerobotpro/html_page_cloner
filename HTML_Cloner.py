#dr.lixxard
import requests
def main():
    inp=input("Welcome!\n\nEnter A Url To Pull Source From: ")
    try:
        r=requests.get(inp)
        html=r.text
    except Exception as E:
        print(str(E))
        setup()
    ask=input("Would You Like To Save To HTML File?(Y/N):")
    if "y" or "Y" in ask:
        print("Writing File...")
        f=open("Leeched_Source.html","+w")
        f.write(str("""<!--LEECHED FROM"""+inp+"""\n\n-------------------------------------\n\n"""+html))
        f.close()
        wait=input("DONE")
        main()
    else:
        print("""<!--LEECHED FROM"""+inp+"""\n\n-------------------------------------\n\n"""+html)
        wait=input("\n\nDONE")
        main()
def setup():
    main()
setup()
