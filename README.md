# SummNews for TUI

## What It Is
This is a Python program that summarizes current BBC news articles, presenting the headlines and summaries in a console interface (or TUI -- Terminal User Interface).

Just run the "\__main\__.py" script from your console -- the program will retrieve the BBC news articles and provide you a list of headlines. Select a headline to read its summary.

![SummNews's TUI headline menu](/screenshots/SummNewsForTUI-Screenshot_01-Headline_Menu.png)

*List of headlines -- Select one to read the summarized article*

![SummNews's Summarize Article view](/screenshots/SummNewsForTUI-Screenshot_02-Summarized_Article.png)

*View of the summarized article*

## Methodology
The engine behind the summarizing -- the SummNews core -- makes its summaries based on the frequency of words within an article. The more frequently a word occurs in an article, the more it's weighted. Sentences with more of these words score higher, and the highest scores determine what sentences from the original article will make up the summary.

It's a relatively simple weighting method, but my experiments with summarizing news articles found this approach to bring the most consistency and effectiveness for sentence-selection summary.

If you're interested in novel summarization -- that is, summaries that introduce or consist entirely of sentences not present in the original article -- major strides are being made with Deep Learning, specifically in the use of neural networks.

## Suggestions for Further Reading
For a summary of text summarization techniques, I recommend the following -- though note that it does not include significant coverage of neural networks for summarization: ["A Survey of Text Summarization Techniques" by Ani Nenkova](https://www.cs.bgu.ac.il/~elhadad/nlp16/nenkova-mckeown.pdf)

For those interested in further reading, especially on neural networks in text summarization, check out the [Publications listing on Stanford's NLP site](https://nlp.stanford.edu/pubs/).
