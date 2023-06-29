import sys
import subprocess as sb

trivyBinary = "trivyBinary/trivy"
# trivySrv = "http://10.70.70.39:1115"
trivySrv = str(sys.argv[1])
token = "H5nF5ywy262wt881ZWpq"
imageURL = "hub.dbrr.lc/test-img/aspnet"
listImgTag = ["5.0-alpine", "5.0-nap-mail-core", "6.0-alpine", "7.0-alpine", "7.0-nap-mail-core"]


for imageTag in listImgTag:
    imageName = f"{imageURL}:{imageTag}"
    command = f"{trivyBinary} client --remote {trivySrv} --ignore-unfixed --token {token} {imageName}"
    sb.run(command,shell=True)
    print()

