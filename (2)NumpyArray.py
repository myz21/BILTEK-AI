import numpy as np

result = np.array([1,2,3,4])

print(result)

#belli bir aralıkta dizi yazdırma
rangedArray = np.arange(2,10)
print(rangedArray)
#[2,10) şeklinde yani sondaki değer dahil olmayacak şekilde integer değerlerini döndürür.

#belli bir aralıkta, belli artış değerine sahip dizi yazdırma
rangedStepArray = np.arange(13,91,13)
print(rangedStepArray)

#sadece sıfırlar, float tipi
onlyZeroArray = np.zeros(10)
print(onlyZeroArray)

#sadece birler, float tipi
onlyOnesArray = np.ones(10)
print(onlyOnesArray)

#belli bir aralığı, belli parçaya bölüyoruz. n parçaya bölüyorsak,n sayı döndürür.
dividedArray = np.linspace(0,100,3)
print(dividedArray)

#0'dan 5'e, 5 parça
print(np.linspace(0,5,5))

#belirli iki değer arasında rastgele bir tam sayı döndürüyoruz
randomInteger = np.random.randint(1,11)

#1 ile 10 aralığı
print(randomInteger)

#belirli iki değer arasında rastgele 3 tam sayı döndürüyoruz
print(np.random.randint(0,20,3))

#0 ile 1 arasında n değer yazdırıyoruz
print(np.random.rand(3))

#-1 ile 1 arasında n değer yazdırıyoruz
print(np.random.randn(5))

np_array = np.arange(2,37,2)
print(np_array)

#dizimizi yeniden şekilendiriyoruz
np_twoDimArray = np_array.reshape(3,6)
print(np_twoDimArray)

#sütunların toplamı
print(np_twoDimArray.sum(axis=0))

#satırların toplamı
print(np_twoDimArray.sum(axis=1))

#rastgele üretilen sayılar arasında en büyük olanı yazdır
rnd_numbers = np.random.randint(6,60,6)
max = rnd_numbers.max()

#üretilen sayılardan en küçüğünü bulur
min = rnd_numbers.min()

#üretilen sayıların ortalamasını alır
average = rnd_numbers.mean()

#en büyük sayının sırasını yazdırır.
indexMax = rnd_numbers.argmax()

print(rnd_numbers)
print(max)
print(min)
print(average)
print(indexMax)
