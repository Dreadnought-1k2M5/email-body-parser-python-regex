import re

fileObj = open('body.txt', 'r')
source = fileObj.read()

#Find ID
id_pattern = r'(Event ID: ([A-Z0-9]+))'
id_var = re.search(id_pattern, source)

#Find Date
date_pattern = r'(([Jj]une)|([jJ]uly)|([aA]ugust)|([sS]eptember)|([oO]ctober)|([nN]ovember)|([dD]ecember)|([jJ]anuary)|([fF]ebruary)|([mM]arch)|([aA]pril)|([mM]ay))\s\d\d,\s\d\d\d\d'
date_var = re.search(date_pattern, source)

#Find Time
time_pattern = r'\d+:\d+(\w\w) - \d+:\d+(\w\w) ([A-Z]{,8})'
time_var = re.search(time_pattern, source)

#Find Guest Count
guest_count_pattern = r'(\d+) guests \(estimated\)'
guest_count_var = re.search(guest_count_pattern, source)

#Find Link
link_pattern = r"https://a.boompop.com/h/manage/tinyb/events/([\w.-]+)/([\w-]+) "
link_var = re.search(link_pattern, source)

#Find Event Type
event_pattern = r"\*Request Summary\*(\s+\n+)(.+)(\s+\n+)(([Jj]une)|([jJ]uly)|([aA]ugust)|([sS]eptember)|([oO]ctober)|([nN]ovember)|([dD]ecember)|([jJ]anuary)|([fF]ebruary)|([mM]arch)|([aA]pril)|([mM]ay))"
event_var = re.search(event_pattern, source)

#Find Company Name

company_name_pattern = r"(\d+:\d+(\w\w) - \d+:\d+(\w\w) [A-Z]{,8}) ([\w\s\!\@\#\$\%\^\&\*\(\)\-\+\;\"\'\>\<\?\/\\]+) ((.+)(\d+) guests)"
company_name_var = re.search(company_name_pattern, source)

print(id_var.group(2))
print(date_var.group())
print(time_var.group())
print(guest_count_var.group())
print(link_var.group())
print(event_var.group(2))
print(company_name_var.group(4))

