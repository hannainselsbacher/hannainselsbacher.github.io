---
layout: post 
author: H.I. 
---

If a prime p divides the product of the integers ab, then it must divide at least one factor. 

## Claim 

$$p \in \mathbb{P}; \; a, b \in \mathbb{Z}: p \mid ab \implies p \mid a \; \lor \; p \mid b \;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;$$

## Proof

Suppose $$p \mid ab \land p \nmid a$$. We have to show, that p divides b.<br>

$$ \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;  \;\;\;\;\;\;\;\;\;\;\;\;  p \mid ab \;\; \Leftrightarrow \;\; p \cdot x = ab , \;\; x \in \mathbb{Z}
\;\;\;\;\;\;$$ 
<br><br>
Since p does not divide a, it follows from Bézout's Lemma: <br><br> 
$$ \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;s \cdot p + t \cdot a = 1$$
<br><br>
Now we multiply by b: <br><br>
$$ \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; b \cdot s \cdot p + (a \cdot b) \cdot t = b$$
<br><br>
Then we can substitute $$a \cdot b$$ by $$p \cdot x$$: <br><br>
$$ \;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; b \cdot s \cdot p + p \cdot x \cdot t = b = p \cdot (b \cdot s + x \cdot t) $$ 
<br><br>
That means that p actually divides b. 