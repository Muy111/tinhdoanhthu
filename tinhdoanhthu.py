loaisp = ['Iphone 13', 'Iphone 13 pro', 'Iphone 13 pro max', 'Iphone 13 mini', 'Iphone 14']
giaban = [21.9,27.8,30.9,18.4, 22]
masp=[1,2,3,4,5]
tongtien=[]
tongluonghang=[]
sl=0

for i in range (len(loaisp)):
 print (loaisp[i], "có mã sản phẩm là", masp[i], 'giá', giaban[i], "triệu")

#Tính doanh thu của từng loại sản phẩm:
def tinhdoanhthu(a,b):
    for i in range (len(loaisp)):
        sm= a[i]*b[i]
        tongtien.append(sm)
    return sm  
  
#Nhập sản phẩm:  
def nhapsp():
    m= input("Bạn có muốn nhập hàng? Hãy gõ 'thỏ': ")
    print ("Hãy nhập số 10 nếu bạn muốn dừng nhập!")
    loaisp[1]=0
    loaisp[2]=0
    loaisp[3]=0
    loaisp[0]=0
    while m== 'thỏ':
         n= int(input("Vui lòng nhập mã sản phẩm: "))
         if n==1:
             sl=int(input("Vui lòng nhập số lượng sản phẩm bán được: "))
             loaisp[0]= loaisp[0] +sl
             tongluonghang.append(loaisp[0])
         elif n==2:
             sl=int(input("Vui lòng nhập số lượng sản phẩm bán được: "))
             loaisp[1]= loaisp[1] +sl
             tongluonghang.append(loaisp[1])
         elif n==3:
             sl=int(input("Vui lòng nhập số lượng sản phẩm bán được: "))
             loaisp[2]= loaisp[2] +sl
             tongluonghang.append(loaisp[2])
         elif n==4:
             sl=int(input("Vui lòng nhập số lượng sản phẩm bán được: "))
             loaisp[3]= loaisp[3] +sl
             tongluonghang.append(loaisp[3])
         elif n==10:
             break
         else:
           print ("Mã sản phẩm không đúng")

nhapsp()
tinhdoanhthu(giaban,loaisp)
print ("Số điện thoại bán ra trong ngày hôm nay là:", sum(tongluonghang))
print ("Doanh thu của cửa hàng trong hôm nay là", sum(tongtien), "triệu")

      
   


