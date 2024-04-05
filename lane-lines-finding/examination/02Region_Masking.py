import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# 读取图像
image = mpimg.imread(r'C:\Users\hjame\Anaconda\lane-lines-finding\examination\test3.png')
print('This image is: ', type(image),'with dimensions:', image.shape)

# 获取图像的行数和列数
rows, cols = image.shape[:2]

# 定义四个角的坐标
bottom_left  = [cols*0.05, rows*0.9]
top_left     = [cols*0.38, rows*0.64]
bottom_right = [cols*0.95, rows*0.9]
top_right    = [cols*0.62, rows*0.64] 

# 创建一个空白图像，大小与原始图像相同
region_select = np.copy(image)

# 定义兴趣区域
pts = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)

# 在原始图像上绘制出兴趣区域（梯形）
cv2.polylines(region_select, [pts], isClosed=True, color=(255,0,0), thickness=3)

# 显示图像
plt.imshow(region_select)
plt.show()