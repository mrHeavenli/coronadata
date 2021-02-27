def get_global_data():
    import requests as r

    site = r.get("https://www.worldometers.info/coronavirus")
    data = site.text

    start = data.find("<title>")
    end = data.find("</title>")

    title = ""



    i = start
    while i != end:
        title += str(data[i])
        i += 1


    title = title.replace("Coronavirus Update (Live):", "")
    title = title.replace(" Deaths from COVID-19 Virus Pandemic - Worldometer", "")
    title = title.replace(",", "")
    title = title.replace(" ", "")
    title = title.replace("Cases", "")
    title = title.replace("Deaths", "")
    title = title.replace("<title>", "")

    list = title.split("and")

    list[0] = int(list[0])
    list[1] = int(list[1])

    returnval = {"cases" : list[0], "deaths" : list[1]}
    return returnval
