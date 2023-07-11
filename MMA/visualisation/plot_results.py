import matplotlib.pyplot as plt

# Podaci za dijagram
algoritam = ['FIFO', 'SB(R)', 'SB(WR)', 'MIN ENG ', 'MAX ENG']
rezultati = [151.98, 171.9, 160.99, 151.07, 184.36]
boje = ['blue', 'red', 'yellow', 'green', 'purple']

# Kreiranje dijagrama
plt.bar(algoritam, rezultati, color=boje)
plt.xlabel('Алгоритам')
plt.ylabel('Резултат')
plt.grid(True)


# Prikazivanje dijagrama
plt.show()
