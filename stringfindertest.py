"""created and tested for https://dictionaryapi.dev/"""
"""I did not find other really free API """
"""deserilazation problem needs more efficient way to find what i want"""

s1="{'audio': 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3','sourceUrl': "
s2="ləʊ/', 'audio': 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-uk.mp3', həˈloʊ/', 'audio': ''}],"
s3="[{'word':'irreducible','phonetic':'/ˌɪɹɪˈdjuːsɪbəl/','phonetics':[{'text':'/ˌɪɹɪˈdjuːsɪbəl/','audio':''}],'meanings':"
s4="[{'word':'ameliorated','phonetics':[],'meanings':[{'partOfSpeech':'verb','definitions':[{'definition':'To make better, or improve, something perceived to be in a negative condition.','synonyms':[],'antonyms':[],'example':'They offered some compromises in an effort to ameliorate the situation.'},{'definition':'To become better; improve.','synonyms':[],'antonyms':[]}],'synonyms':[],'antonyms':['deteriorate','worsen']},{'partOfSpeech':'adjective','definitions':[{'definition':'Having had problem(s) improved upon; having been the subject of amelioration.','synonyms':[],'antonyms':[]}],'synonyms':[],'antonyms':[]}],'license':{'name':'CC BY-SA 3.0','url':'https://creativecommons.org/licenses/by-sa/3.0'},'sourceUrls':['https://en.wiktionary.org/wiki/ameliorate','https://en.wiktionary.org/wiki/ameliorated']}]"


#too complicated to deal with all possibility -> isinstance?
https://stackoverflow.com/questions/39216533/how-to-extract-only-the-key-value-from-this-list-dict-json-response

