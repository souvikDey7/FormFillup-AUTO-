import mechanize as me


url = "https://makaut1.ucanapply.com/smartexam/public/student/week-report-activity/create"
br = me.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
res = br.open(url)
try:
    print("inside try")
    print(br)
    print(len(br.forms()))
    for f in br.forms():
        print(f)
except mechanize._mechanize.FormNotFoundError as e:
    print("Sorry no form found on this page", e)
print("After try catch")
#br.select_form(nr=0)
#br.form['Topic Covered'] = 'xxx'
#req = br.submit()

#print(req)
