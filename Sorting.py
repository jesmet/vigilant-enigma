movies =['Memento', 'Goodfellas', 'Scarface', 'Heat', 'La La Land', 'The Departed', 'Dune', 'Psycho', 'Utharam', 'Fight Club', 'Irakal', 'Whiplash', 'Manichitrathazhu', 'Pulp Fiction'
]

print("Original list:", movies)

n = len(movies)

for i in range(n):
  
    for j in range(0, n - i - 1):
      
        if len(movies[j]) > len(movies[j + 1]):

          
            movies[j], movies[j + 1] = movies[j + 1], movies[j]

print("Sorted by length:", movies)
