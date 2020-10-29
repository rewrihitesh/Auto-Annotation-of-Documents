# Auto-Annotation-of-Documents
# IRE Major Project

## Abstract:

In this project we genrated the comments from nyt articles+comments. we have used the GPT2 (open-source, a stat-of-art model) to generate context specifc keywords targetted comments.

## Dataset used:
1. NYT articles
2. Comments on aformentioned articles.

## Methodologies Tried:
1. Intially we trained the GPT2 on comments alone to get hands on the library, we tweaked the model to look for best hyperparameter and generated uncodintional comments.
2. We then extracted the keywords from the article and passed them as prompt to our model, in order to genrate the conditional comments.

## Findings from the current implementation:
1. **Greedy search** selects the word with the highest probability as its next word,but in this we found out that words start repeaing itself and other major drawback is that it misses high probability words hidden behind a low probability word.
2. **Top-k sampling** Top-K sampling produces very coherent comments and show very good resuls. 
3. **Top-k and Top-p sampling** Top-k and Top-p sampling produces argubaly the best result and look very human like.

## Notes: 

The methodologies used so far are in correspondence to the initial scope document we prepared. We are in sync with the proposed timeline.
1. Our future objective is to restrain the context further by using extractive summarization on the article text or to improve dataset spo that comment wont deviate from the context.
2. We wiil try beam searching and n-gram penality to further finetune our model. 





