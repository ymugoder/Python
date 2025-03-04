# trggering the process
import os
import subprocess
import sys


def instasubprocess(user, tags, type, productId):
    try:
        child_env = sys.executable
        file_pocessing = (
            os.getcwd()
            + "/insta_datafetcher.py "
            + user
            + " "
            + tags
            + " "
            + type
            + " "
            + productId
        )
        command = [child_env, os.path.join(os.getcwd(), "insta_datafetcher.py"), user, tags, type, productId]
        result = subprocess.Popen(command)
        result.wait()
    except:
        print("error::instasubprocess>>", sys.exc_info()[1])


if __name__ == "__main__":
    instasubprocess(user="u2", tags="food", type="hashtags", productId="abc")
