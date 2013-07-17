dictionary_of_language_names
============================

A dictionary of language names of more than 200 languages in more than 200 languages and a list of language names in English with their counterpart in the respective language. 

The data was scraped from www.jw.org. The encoding is utf-8. 

The easiest way to use it is to load the pickle file in python:


fh = open('dictionary_of_language_names.pickle', 'rb')

dic = pickle.load(fh)

dic['de']['fr']

>>> u'Franz\xf6sisch'



Keywords: NLP, Natural Language Processing, Machine Translation, glossary, language list, python, data, dictionary, multi-language dictionary, English, languages, rare languages

List of languages: 

Kikuyu, Cambodian, Sarnami, Khoekhoegowab, Haitian, Tojolabal, Croatian, Herero, Serbian, Waray-Waray, Kikaonde, Kongo, Lhukonzo, Ukrainian, Kabyle, Aymara, Toba, language_id, Huastec, Hindi, Nzema, Ndonga, language_in_English, Kwanyama, Punjabi, Faeroese, Georgian, Greenlandic, Miskito, Hungarian, Efik, Rapa, Bicol, Afrikaans, Armenian, Wolaita, Huave, Kikamba, Hausa, Amharic, Norwegian, Kisonge, Nahuatl, Nepali, Solomon, Kirghiz, Ndebele, Rarotongan, Korean, Zapotec, Baoule, Dutch, Aukan, Tlapanec, Pangasinan, Russian, Ewe, Mauritian, Uruund, Voru, Spanish, Greek, Lingala, Estonian, Vezo, Rumanyo, Luganda, Lithuanian, Mayo, Lamba, Yoruba, Sepedi, Kinyarwanda, Dangme, Tarascan, Rutoro, Wayuunaiki, Mixtec, Cebuano, Sango, Quechua, Tiv, Guna, Maya, Sranantongo, Acholi, Xhosa, Tetum, Krio, Isoko, Oromo, Saramaccan, Quichua, Azerbaijani, Chin, Romanian, Bulgarian, Quiche, Kalenjin, Lahu, Mbunda, Swati, Tsonga, Kisi, Cinyanja, Shona, Newari, Slovenian, Zande, Tamil, Mambwe-Lungu, Icelandic, Runyankore, Guarani, Mongolian, Kiluba, Tagalog, Ngabere, Kwangali, Italian, Iloko, Portuguese, Hiligaynon, Tzotzil, Myanmar, Ateso, Finnish, Welsh, Zulu, Chol, Sesotho, Otomi, Mazatec, Tajiki, Kekchi, Mam, Lenje, Kalanga, Somali, Tarahumara, Vietnamese, Gujarati, Marathi, French, Sinhala, Frafra, Indonesian, Luvale, Tongan, Danish, Japanese, Niuean, Polish, Tankarana, Czech, Chinese, Garifuna, Maltese, Venda, Nuer, Sidama, Mayangna, Thai, Swahili, Luo, English, Latvian, Kazakh, Irish, Macedonian, Mixe, Tahitian, Samoan, Lugbara, Tatar, Albanian, Turkish, Totonac, Tswana, Slovak, Swedish, Ga, Kurdish, Twi, Tokelauan, Malagasy, Papiamento, Romany, Tzeltal, Cakchiquel, Wichi, German, Igbo, Ossetian, Mapudungun, Tigrinya, Seychelles
