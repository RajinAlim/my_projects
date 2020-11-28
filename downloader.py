import os
import sys
from urllib.request import urlopen
from urllib.parse import urljoin

def download(url, path='./'):
    try:
        if "http" not in url:
            url = "https://" + url
        res = urlopen(url)
        if res.status != 200:
            raise Exception
    except:
        print("Download failed!")
        return
    directory = os.path.dirname(path)
    if not directory and path != './' and "." not in path and os.path.exists("./" + path):
        directory = "./" + path
    else:
        directory = "./"
    os.chdir(directory)
    basename = os.path.basename(path)
    if basename and basename not in directory:
        filename = basename.split(".")[0]
    else:
        filename = "random_name"
    content_type = res.getheader("Content-Type")
    if ";" in content_type:
        content_type, *extras = content_type.split("; ")
    extension = content_type.split("/")[1]
    extension = ".txt" if extension == "plain" else '.' + extension
    filename += extension
    if "text" in content_type:
        try:
            encoding = None
            for data in extras:
                if "charset" in data:
                    encoding = data.split("=")[1]
            if encoding:
                text = res.read().decode(encoding)
                with open(filename, 'w', encoding=encoding) as f:
                    f.write(text)
        except:
            done = False
        else:
            done = True
    if not done:
        with open(filename, "wb") as f:
            f.write(res.read())
    filepath = os.path.join(os.getcwd(), filename)
    return filepath


if __name__ == "__main__":
    if len(sys.argv) > 1:
        download(*sys.argv[1:])
    else:
        inp = input("Enter url and download path(optional) separated by space: ")
        download(*inp.split())