import glob, os

os.chdir("/Users/christianmock/test_app")
for file in glob.glob("*.txt"):
    print(file)

