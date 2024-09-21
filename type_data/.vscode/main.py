# tipe data adalah format penyimpanan data dalam data tertentu

# tipe data: angka satuan (1,2,3)
data_integer = 1 
print("data :", data_integer)
print("bertipe :",type(data_integer))


# type data float (1.00, 1.5)
data_float = 1.5
print("data :", data_float)
print("bertipe :",type(data_float))


#type data string ( tipe data huruf dengan ciri tanda petik dua)
data_string = "ucup"
print("data :", data_string)
print("bertipe :",type(data_string))

#type data boolean / biner (true or false)
data_bool = False
print("data :", data_bool)
print("bertipe :",type(data_bool))

## type data khusus
#type data komplek

data_komplek = complex(5,6)
print("data :", data_komplek)
print("bertipe :",type(data_komplek))

# type data dari bahasa C

from ctypes import c_double

data_C_double = c_double(10.5)
print("data :", data_C_double)
print("bertipe :",type(data_C_double))