import sys, os
import pathlib

def getAllLinks(filename):
    with open(filename, 'r') as f:
        line = f.read()
    lines = line.split(",")
    return lines

def makeCurlRequests(links):
    return " & curl -O ".join(links)

def writeToBatFile(filename, data):
    filenamewithoutext = pathlib.Path(filename).stem
    batfilename = filenamewithoutext + "-Downloader.bat"
    dirtbw = pathlib.Path(f"{os.getcwd()}/{batfilename}")
    print(dirtbw)
    with open(dirtbw, 'w') as f:
        print(data)
        print(f"writing to {dirtbw}...")
        f.write(data)
        
if __name__=="__main__":
    filename = sys.argv[1]
    
    links = getAllLinks(filename)
    # print(links)
    curlreq = makeCurlRequests(links)
    # print(curlreq)
    
    writeToBatFile(filename, curlreq)
    