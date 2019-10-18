# trigram-similarity

A trigram algorithm is a case of n-gram, a contiguous sequence of n (three, in this case) items from a given sample. In our case, an application name is a sample and a character is an item.

So The sequence “martha” has 4 trigrams { mar art rth tha }

Taking for example “martha” and the same word with a typo, “marhta”, and we can compute their trigrams:
Trigrams “martha”: { mar art rth tha }
Trigrams “marhta”: { mar arh rht hta }

To measure similarity we divide the number of matching trigrams in both strings: 1 { mar } by the number of unique trigrams: 7 { mar art rth tha arh rht hta }

The result is 1/7 = 14%

To balance the disadvantage of the outer characters (somewhat to reinforce the similarity of strings starting and ending with the same trigrams), we pad the string with blanks on either side resulting in these case in three more trigrams “_ma”, “ha_“ and “ta_”.

Trigrams “ martha ”: { _ma mar art rth tha ha_ }
Trigrams “ marhta ”: { _ma mar arh rht hta ta_ }

Having done that, the number of matching trigrams is up to: 2 { _ma mar }
The number of all unique trigrams: 9 { _ma mar art rth tha arh rht hta ha_ }

The result is now 2/9 = 22%

Using this method to compare “Twitter v1” and “Twitter v2” we have:
The number of matching trigrams: 7 { _tw twi wit itt tte ter er_ }
The number of all unique trigrams: 11 { tw twi wit itt tte ter er_ _v1 _v2 v1_ v2_ }
The result is 7/11 = 63%
The limit of the Trigram method to compare strings is that short strings with one (or two..) different trigrams tend to produce a lower similarity than long ones.
That is how we get a 0.2 similarity between “ShazamAndroid” and “ShazamIphone”, as they have more different trigrams.

The number of matching trigrams is: 5 { _sh sha haz aza zam }
The number of all unique trigrams: 20
As there is a strong dependency with string length, it does not yield a good comparison for us.
