def tuplist2HTMLtable(myiter, htmltxt = ""):
    htmltxt += "<table>\n"
    for tup in myiter:
        htmltxt += "\t<tr>\n"
        for item in tup:
            htmltxt += "\t<td>{0}</td>\n".format(item)
        htmltxt += "\t</tr>\n"
    htmltxt += "</table>\n"
    return htmltxt
