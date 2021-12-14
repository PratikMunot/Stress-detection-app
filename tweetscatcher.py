# import twint
# import subprocess
# Configure
# c = twint.Config()
# c.Username = "now"
# c.Search = "fruit"
#
# # Run
# print(twint.run.Search(c))
# subprocess.call('start',shell=True)

import subprocess
import twint
# subprocess.call('start',shell=True)
# print(2+7)
# Configure


import twint

c = twint.Config()

c.Username = "ShrutiMath2"
# c.Custom["tweet"] = ["id"]
# c.Custom["user"] = ["bio"]
# c.Limit = 10
c.Store_csv = True
c.Output = "none.csv"
c.Lang = "en"
# c.Output = "none"

# twint.run.Search(c)

# Run
print(twint.run.Search(c))
