import os

x = 1000
for i in range(x):
    os.system(
        "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \--headless --disable-gpu --dump-dom "
    )
