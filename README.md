# language_similarity

This project aims to compare language based on textual similarity. I realize that words can, despite being written in different alphabets for different languages, have the same origin; however, this is just a toy project to start with.

The goal is to:
1) download the same snippet of Genesis 11: 1-9 from the omniglot.com site in all the various available languages
2) try to align the words based solely on word similarity (perhaps, at first, only within language families, and then outside them)
3) calculate a general string similarity score for the whole passage
4) graph the languages based on their similarity (calculated in this very limited sense), with similarity equating to edge length

Obviously for a lot of languages the similarity score will be 0, in which case, we will not add an edge between those nodes. The issue of alignment is still a bit iffy - in machine translation, I would use EM to estimate alignment probabilities based on training data, but alas, there's not nearly enough data here. However, if I use a library like SimMetrics (http://sourceforge.net/projects/simmetrics/), then I can cycle through various string similarity measures to see what works best and maybe stumble onto something that works.
