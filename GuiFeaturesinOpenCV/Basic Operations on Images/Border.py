import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('temp.jpg')

# 这样也可以，只是效率太低了
# b,g,r = cv2.split(img1)
b = img1[:,:,0]
g = img1[:,:,1]
r = img1[:,:,2]

img1 = cv2.merge([r,g,b])

"""
    第一个参数，图片对象
    然后依次是边框距离图片边缘上下左右的宽度
    边框的类型，如果是BORDER_CONSTANT类型则多一个value参数代表颜色
"""
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
# Matplotlib显示的是 RGB颜色，而上面设置的是BGR颜色，所以蓝色显示的是红色
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

"""
    plt.subplot(231) 等价于 plt.subplot(2, 3, 1)
    意思是创建一个两行，三列的表格，这个图片是第一张
    plt.imshow()可选参数有：
        Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, 
        BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, 
        GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, 
        OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, 
        Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, 
        PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, 
        Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, 
        RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, 
        Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, 
        Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, 
        YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, 
        afmhot_r, autumn, autumn_r, binary, binary_r, bone, 
        bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, 
        coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, 
        flag, flag_r, gist_earth, gist_earth_r, gist_gray, 
        gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, 
        gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, 
        gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, 
        gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, 
        inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, 
        nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, 
        plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, 
        seismic_r, spectral, spectral_r, spring, spring_r, summer, 
        summer_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
"""
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()