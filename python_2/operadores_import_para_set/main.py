# operações úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  #{1, 2, 3, 4}
s3 = s1 & s2 #{2, 3}
s3 = s1 - s2 #intens que estão apenas no primeiro set #{1}
s3 = s2 - s1 #{4}
s3 = s1 ^ s2 #itens que não estão em ambos #{1, 4}
print(s3) 
