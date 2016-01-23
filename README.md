# language_similarity

This project aims to compare language based on textual similarity. I realize that words can, despite being written in different alphabets for different languages, have the same origin; however, this is just a toy project to start with.

The goal is to:
<br>
1) download the same snippet of Genesis 11: 1-9 from the omniglot.com site in all the various available languages
<br>
2) try to align the words based on a NACLO-like approach (i.e. word frequencies, etc).
<br>
3) calculate by-word string similarity score for the whole passage
<br>
4) graph the languages based on their similarity (calculated in this very limited sense), with similarity equating to edge length

<br>
Obviously for a lot of languages the similarity score will be 0, in which case, we will not add an edge between those nodes. The issue of alignment is still a bit iffy - in machine translation, I would use EM to estimate alignment probabilities based on training data, but alas, there's not nearly enough data here. However, if I use a library like SimMetrics (http://sourceforge.net/projects/simmetrics/), then I can cycle through various string similarity measures to see what works best and maybe stumble onto something that works.

I've always wanted to code up the solutions to some of the NACLO style problems and it would be interesting to visualize language relatedness based on string similarity.
