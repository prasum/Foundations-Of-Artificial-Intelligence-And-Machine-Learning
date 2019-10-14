from pydataset import data
iris_data=data('iris')
iris_arr=iris_data.values

#Solution 1
sub_iris=iris_arr[(iris_arr[:,0] <= 5) & (iris_arr[:,1] <= 3)]
print(sub_iris)

#Solution 2
iris_ones=numpy.ones(sub_iris.shape,sub_iris.dtype)
print(iris_ones.shape)

#Solution 3
petal=iris_arr[(iris_arr[:,2] >2) & (iris_arr[:,2] < 6)]
print(petal.shape[0])

#Solution 4
species=numpy.array(iris_arr[:,4],dtype='<U15')
print(species.dtype)

#Solution 5
unique_species=numpy.unique(species)
species_list=species.tolist()
print(species_list)
print(len(species_list))


