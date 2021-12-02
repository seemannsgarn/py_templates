from programming_language_class import Programming_language

lang_1 = Programming_language('Python','PyCharm')
lang_2 = Programming_language('JavaScript','Webstorm')

print(lang_1.name)
print(lang_1.ide)
print(lang_2.name)
print(lang_2.ide)

lang_1.writting()
lang_2.crashes()