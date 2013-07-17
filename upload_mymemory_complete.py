#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
import codecs
import pickle
import time

""" How to upload the complete dictionary to mymemory.translated.net, using the SET option of the API. """

codes = ['ki', 'km', 'hns', 'naq', 'ht', 'toj', 'hr', 'hz', 'sr_latn', 'war', 'kqn', 'kg', 'koo', 'uk', 'kab', 'ay', 'tob', 'hus', 'hi', 'nzi', 'ng', 'kj', 'pa', 'fo', 'ka', 'kl', 'miq', 'hu', 'efi', 'rap', 'bcl', 'af', 'hy_armn', 'wal', 'huv', 'kam', 'ha', 'am', 'no', 'sop', 'ncj', 'ne', 'pis', 'ky', 'nr', 'rar', 'ko', 'zpg', 'bci', 'nl', 'djk', 'pag', 'ru', 'ee', 'mfe', 'rnd', 'es', 'el', 'ln', 'et', 'lg', 'lt', 'mfy', 'lam', 'yo', 'nso', 'rw', 'ada', 'tsz', 'ttj', 'guc', 'ceb', 'sg', 'que', 'tiv', 'cuk', 'yua', 'srn', 'ach', 'xh', 'tdt', 'kri', 'iso', 'om', 'srm', 'qus', 'az_cyrl', 'cnh', 'ro', 'bg', 'quc', 'kln', 'lhu', 'mck', 'ss', 'ts', 'kiz', 'nya', 'sn', 'new', 'sl', 'zne', 'ta', 'mgr', 'is', 'nyn', 'gug', 'mn', 'lub', 'tl', 'kwn', 'it', 'ilo', 'pt', 'hil', 'tzo', 'mya', 'teo', 'fi', 'cy', 'zu', 'ctu', 'st', 'oto', 'mau', 'tg', 'kek', 'mam', 'leh', 'kck', 'so', 'vi', 'gu', 'mr', 'fr', 'si', 'gur', 'id', 'lue', 'to', 'da', 'ja', 'niu', 'pl', 'xmv', 'cs', 'zh_hant', 'cab', 'mt', 've', 'nus', 'sid', 'yan', 'th', 'sw', 'luo', 'en', 'lv', 'kk_cyrl', 'ga', 'mk', 'mco', 'ty', 'sm', 'lgg', 'tt', 'sq', 'tr', 'tn', 'sk', 'sv', 'gaa', 'kmr_cyrl', 'tw', 'tkl', 'mg', 'pap', 'rmn', 'tzh', 'cak', 'de', 'ig', 'os', 'arn', 'ti']


fh = open('dictionary_of_language_names.pickle', 'rb')
d = pickle.load(fh)
   
for sl in codes:  

    # how long can the server hold an open connection? dont know so start a new one for each source language 
    conn = httplib.HTTPConnection('api.mymemory.translated.net')
    if '_' in sl or sl == 'ki' or sl == 'km':
        continue
    
    source_language = sl
    
    for tl in codes: 

        if '_' in tl or sl == tl or tl == 'ki' or tl == 'km':
            continue 

        target_language = tl 
        print 'Start to upload language pair ' + sl + ' - ' + tl

        for c in codes:
        
            if '_' in c:
                # probably not a valid ISO code?
                continue 

            try:
                source = d[source_language][c].encode('utf-8')
                target = d[target_language][c].encode('utf-8')
            except KeyError:
                print c + ' not found in ' + sl + ' or ' + tl 
                continue 

            print source + " = " + target + ' in ' + sl+ ' - '  + tl

            # add your email like this: 
            #conn.request("GET", "/set?seg=" + source + "&tra=" + target + "&langpair=" + source_language + "|" + target_language + "&de=YOUR_EMAIL_ADDRESS")         
            conn.request("GET", "/set?seg=" + source + "&tra=" + target + "&langpair=" + source_language + "|" + target_language)
            r = conn.getresponse()   
            if not r.status == 200:
                print "WARNING: Status is " + str(r)     
            #print r.status

        print 'target language ' + tl + ' finished.'

    print 'source language ' + sl + ' finished.'
    conn.close()
