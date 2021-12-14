import twint

c = twint.Config()
with open("name.txt","r") as fp:
    name=fp.read()
    c.Username = name
    # c.Custom["tweet"] = ["id"]
    # c.Custom["user"] = ["bio"]
    # c.Limit = 10
    c.Store_csv = True

    c.Output = "results.csv"
    c.Lang = "en"

    twint.run.Search(c)

# Run
# print(twint.run.Search(c))