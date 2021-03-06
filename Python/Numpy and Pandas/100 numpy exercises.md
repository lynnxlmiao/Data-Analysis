## 100 numpy exercises ##
#### 1. Import the numpy package under the name np (★☆☆) ####
```python
import numpy as np
```
#### 2. Print the numpy version and the configuration (★☆☆) ####
```python
print(np.__version__)
np.show_config()
```
#### 3. Create a null vector of size 10 (★☆☆) ####
```python
Z = np.zeros(10)
print(Z)
```
[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]

#### 4. ? How to get the documentation of the numpy add function from the command line? (★☆☆) ####
```python
python -c "import numpy; numpy.info(numpy.add)"
```
#### 5. Create a null vector of size 10 but the fifth value which is 1 (★☆☆) ####
```python
Z = np.zeros(10)
Z[4] = 1
print(Z)
```
[ 0.  0.  0.  0.  1.  0.  0.  0.  0.  0.]
#### 6. Create a vector with values ranging from 10 to 49 (★☆☆) ####
```python
Z = np.arange(10,50)
print(Z)
```
[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]
#### 7. Reverse a vector (first element becomes last) (★☆☆) ####
```python
Z = np.arange(50)
Z = Z[::-1]
```
[49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25
 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0]
#### 8. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆) ####
```python
Z = np.arange(9).reshape(3,3)
print(Z)
```
[[0 1 2]
 [3 4 5]
 [6 7 8]]
#### 9. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆) ####
```python
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
```
(array([0, 1, 4], dtype=int64),)
#### 10. Create a 3x3 identity matrix (★☆☆) ####
```python
Z = np.eye(3)
print(Z)
```
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
#### 11. Create a 3x3x3 array with random values (★☆☆) ####
```python
Z = np.random.random((3,3,3))
print(Z)
```
[[[ 0.5190761   0.90510138  0.57127825]
  [ 0.97503746  0.39988636  0.62865192]
  [ 0.55182293  0.62844173  0.5260797 ]]

 [[ 0.27621706  0.10009314  0.85326118]
  [ 0.34215806  0.89750769  0.8500942 ]
  [ 0.89163612  0.7121049   0.43796964]]

 [[ 0.86943137  0.88273243  0.62377535]
  [ 0.89692499  0.1381987   0.79772176]
  [ 0.35849073  0.54212388  0.50341262]]]
#### 12. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆) ####
```python
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Z)
print(Zmin, Zmax)
```
[[ 0.15894776  0.30131754  0.75573941  0.03532094  0.53163017  0.77451156
   0.5537195   0.37352288  0.62283488  0.48306281]
 [ 0.87276035  0.32120208  0.39650799  0.18402764  0.92829017  0.73402736
   0.17716287  0.83697971  0.48267776  0.2115827 ]
 [ 0.4093239   0.8347894   0.73828105  0.04512587  0.77250369  0.35119641
   0.80143225  0.03110841  0.95644224  0.98238442]
 [ 0.4787553   0.50921569  0.69873804  0.37242739  0.33087046  0.14930397
   0.30552512  0.62821932  0.51970666  0.37237441]
 [ 0.00733314  0.93158651  0.4586878   0.61762752  0.8685656   0.8749225
   0.95537816  0.88643747  0.30392893  0.87889974]
 [ 0.02311159  0.61817436  0.73525499  0.18051833  0.4974741   0.00991971
   0.03121947  0.31950717  0.72843669  0.40797627]
 [ 0.87317067  0.20822243  0.53608569  0.08184041  0.98946811  0.5153548
   0.19184599  0.95949498  0.6230231   0.40413761]
 [ 0.39321659  0.52677591  0.69449104  0.57892188  0.36990367  0.94604195
   0.11609149  0.93392417  0.30208378  0.43103179]
 [ 0.81005583  0.40861423  0.09996111  0.62144003  0.91654783  0.09693788
   0.25132765  0.41582798  0.31980521  0.7416483 ]
 [ 0.27819543  0.13098998  0.74844827  0.76274658  0.95768635  0.16514465
   0.86780239  0.22003272  0.02825509  0.27999058]]
(0.0073331363345950917, 0.98946810707586064)
#### 13. Create a random vector of size 30 and find the mean value (★☆☆) ####
```python
Z = np.random.random(30)
m = Z.mean()
print(Z)
print(m)
```
[ 0.03871581  0.82702986  0.65106871  0.18450624  0.269094    0.24981848
  0.42341955  0.35448939  0.70594605  0.80946581  0.89430903  0.52896422
  0.33203051  0.1350373   0.17939405  0.27451911  0.18904734  0.2006409
  0.3615084   0.82297766  0.15546717  0.18343661  0.66418436  0.47219128
  0.29031949  0.15244412  0.17728161  0.61654441  0.609821    0.45194895]
0.406854047653
#### 14. Create a 2d array with 1 on the border and 0 inside (★☆☆) ####
```python
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
```
[[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]]
#### 15. *What is the result of the following expression? (★☆☆) ####
```python
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 * 0.1
```
False
#### 16. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆) ####
```python
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
```
[[0 0 0 0 0]
 [1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]]
#### 17. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆) ####
```python
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
```
[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]
#### 18. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? ####
```python
print(np.unravel_index(100,(6,7,8)))
```
(1, 5, 4)
#### 19. Create a checkerboard 8x8 matrix using the tile function (★☆☆) ####
```python
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
```
[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]
#### 20. Normalize a 5x5 random matrix (★☆☆) ####
```python
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
```
[[ 0.55642364  0.83427692  0.15461693  0.42541982  0.96085237]
 [ 0.12518735  0.15050221  0.55964453  0.89484383  0.72599075]
 [ 0.3804377   0.30456337  0.52922025  0.77065076  0.67617333]
 [ 0.1947681   0.28272861  0.38190832  1.          0.63489674]
 [ 0.10578147  0.37447813  0.85450221  0.59814225  0.        ]]
#### 21. Create a custom dtype that describes a color as four unisgned bytes (RGBA) (★☆☆) ####
```python
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
```
#### 22. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆) ####
```python
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)
```
[[ 3.  3.]
 [ 3.  3.]
 [ 3.  3.]
 [ 3.  3.]
 [ 3.  3.]]
#### 23. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆) ####
```python
Z = np.arange(11)
print(Z)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)
```
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 0  1  2  3 -4 -5 -6 -7 -8  9 10]
#### 24. What is the output of the following script? (★☆☆) ####
```python
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
```
9
10