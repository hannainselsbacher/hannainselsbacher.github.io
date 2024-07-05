# Lemma von Bézout 

Das Lemma von Bézout (nach [Étienne Bézout](https://de.wikipedia.org/wiki/%C3%89tienne_B%C3%A9zout) (1730-1783)) besagt, dass:  
$$\forall a, b \in \mathbb{Z}\; \exists \; x, y \in \mathbb{Z}: ggT(a,b) = x \cdot a + y \cdot b $$ 


>**Beweis** 
>O.B.d.A sei $a \neq 0$. Sei d die kleinste positive Zahl aus $S = \{z = x \cdot a + y \cdot b \;|\; x,y \in \mathbb{Z}\}$ mit $d = x \cdot a + y \cdot b$. 
Da $ggt(a,b)$ $a$ und $b$ teilt, teilt $ggt(a,b)$ auch die Summe, also d. Daraus folgt $ggt(a,b) \leq d$.
Nach Division mit Rest gilt: $a = q \cdot d + r$, wobei $0 \leq r \lt d$. Nach Einsetzen dieser Darstellung von $a$ in die Gleichung $d = x\cdot a + y \cdot b$ und Umformung nach $r$ erhalten wir $r = (1-qs)a + (-qt)b$. 
Da d die kleinste solche zahl ist, folgt $r = 0$. Damit gilt: $d|a \; \land \; d|b$. Somit gilt $d \leq ggt(a,b)$
Insgesamt gilt dementsprechend $ggt(a,b) = d$. $\square$ 


