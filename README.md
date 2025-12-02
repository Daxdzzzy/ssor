# Documentacion tecnica. 

##SSOR (Symmetric Successive Over-Relaxation) es un método iterativo para resolver sistemas de ecuaciones lineales de la forma Ax = b.

Requisitos:
• La matriz debe ser simétrica
• Se recomienda que sea diagonal dominante
• ω debe estar entre 0 y 2

El método realiza dos barridos por iteración: uno hacia adelante (SOR) y otro hacia atrás (SSOR), lo que mejora la convergencia. 
