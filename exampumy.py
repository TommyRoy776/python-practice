import numpy as np

my_list = np.array([[1,2,3],
                    [4,5,6],[7,8,9]])
print(f'shape: {my_list.shape}')
#Vectorizing arithmetic
my_list*2 
#multidimensional index rathe than [0][1]
print(f'pos 0,1: {my_list[0,1]}')
#slicing 
print(f'slice: {my_list[1:3]}')
print(f'get every 2 step of rows and columns: {my_list[::2,::2]}')
#Boolean 
print(f'compare each element: {my_list >=3}')

#broadcasting, only size match or size 1 to be stretched 
arr_1 = np.array([[1,2,3]])
arr_2 = np.array([[1],[2],[3],[4]])
print(f'{arr_1.shape} {arr_2.shape}')
print(f'broadcasting result: {arr_1 + arr_2}')

#aggregate
agg_list = np.array([[1,2,3],[4,5,6]])
print(f'shape of my_list : {agg_list.shape}')
#aggregate see np.shape to figure out which axis   
print(f'aggregate: {np.sum(agg_list,axis=0)}')

#filter boolean indexing 
filtered = agg_list[(agg_list <5) & (agg_list % 2 == 0)]
print(f'filtered: {filtered}')

#Fill array with random values 
ran = np.random.default_rng()
print(f'Random array 3 rows and 2 cols: {ran.integers(low=0,high=9,size=(3,2))}')