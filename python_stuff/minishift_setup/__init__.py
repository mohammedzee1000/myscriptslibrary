from urllib2 import urlopen


def request_url(url):
    try:
        req = urlopen(url)
    except Exception:
        req = None
    return req

git_api_url = "https://api.github.com/repos"
repo = "minishift/minishift"
releases = "releases"
latest = "latest"
down_loc = "minishift.zip"
app_loc = "minishift"

if __name__ == '__main__':
    info_url = git_api_url + "/" + repo + "/" + releases + "/" + latest
    data = request_url(info_url)
    if data:
        assets = info_url["assets"]
        for asset in assets:
            if "linux" in asset["name"] and "amd64" in asset["name"]:
                tarball = request_url(str(asset["browser_download_url"]))
                if tarball:
                    with open(down_loc, "w+") as tarball_file:
                       tarball_file.write(tarball.read())

