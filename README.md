# SummNews for TUI

## What It Is
SummNews summarizes current BBC news articles in a console interface (or TUI — Terminal User Interface). Just run the `__main__.py` script from your console, and SummNews will retrieve recent BBC news articles and list the headlines for selection; select a headline to read the article's summary.

![SummNews's TUI headline menu](/screenshots/SummNewsForTUI-Screenshot_01-Headline_Menu.png)

*List of headlines -- Select one to read the summarized article*

![SummNews's Summarize Article view](/screenshots/SummNewsForTUI-Screenshot_02-Summarized_Article.png)

*View of the summarized article*

## Methodology
The engine behind SummNews makes its summaries based on the frequency of words within an article. The more frequently a word occurs in an article, the more it gets weighted. Sentences are then scored based on the weight of the words each sentence contains — the higher the total weights, the higher the scores. The sentences with the highest scores get selected to make up the summary.

While the weighting method is relatively simple, my experiments showed it to make clear and consistent sentence-selection summaries of news articles. For those more interested in novel summarization — that is, summaries that introduce or consist entirely of sentences not present in the original article — I encourage you to investigate the amazing strides are being made with deep learning neural networks to that end.

## Suggestions for Further Reading
For a summary of text summarization techniques, I recommend the following; note, however, that this article does not give significant coverage to neural networks' capabilities: ["A Survey of Text Summarization Techniques" by Ani Nenkova](https://www.cs.bgu.ac.il/~elhadad/nlp16/nenkova-mckeown.pdf)

For those wanting even more, and especially for those interested in neural network–based Natureal Language Processing, check out the [Publications listing on Stanford's NLP site](https://nlp.stanford.edu/pubs/).
