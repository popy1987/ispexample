import sys
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    print("--------- Start ---------")
    # コマンドライン引数を取得する
    args = sys.argv[1:]
    # コマンドライン引数を出力する
    print(args)

    # RAWデータ読み込み
    I = io.imread('..\data\Canon-5DMarkII-Shotkit.tiff')
    BLACK_LIMITED = 1024
    WHITE_LIMITED = 15600

    print(I.shape)
    print(I.dtype)
    print(I.astype)
    print(I)
    a_float = np.array(I, dtype=float)
    print(a_float)

    # 配列xのコピー
    temp_float = a_float.copy()
    
    print(" 3. 线性化操作")

    for i, row in enumerate(a_float):
        # print("Row {}: {}".format(i, row))
        for j, value in enumerate(row):
            if(value <= BLACK_LIMITED):
                temp_float[i, j] = 0

            elif(value >= WHITE_LIMITED):
                temp_float[i, j] = 1
            else:
                temp_float[i, j] = value / (WHITE_LIMITED - BLACK_LIMITED)
    
    print(temp_float)

    # 创建RGB三色通道
    r_float = temp_float.copy()
    g_float = temp_float.copy()
    b_float = temp_float.copy()

    print(" 4. 确定图像的合理的 Bayer 模式")
    # for i, row in enumerate(temp_float):
    #     for j, value in enumerate(row):
    #         # R配列

    #         # 偶数行
    #         if i % 2 == 0:
                
    #             if j % 2 == 0:
    #                 # 偶数列, 左右之和的平均
    #                 r_float[i, j] = temp_float[i, j]
    #                 if(j == 0):
    #                     r_float[i, j] = temp_float[i, j + 1]
    #                 elif(j == row.size):
    #                     # 因为是 2 * 2，理论上不会有这个点 
    #                     r_float[i, j] = temp_float[i, j - 1]
    #                 else:
    #                     r_float[i, j] = (temp_float[i, j - 1] + temp_float[i, j + 1]) / 2 

    #             else:
    #                 # 奇数列，传感器本身的值
    #                 r_float[i, j] = temp_float[i, j]
    #         else:
    #             # 奇数行 的 偶数列，左上，右上，左下，右下之平均
    #             if j % 2 == 0:
    #                 r_float[i, j] = (temp_float[i - 1, j - 1] 
    #                                  + temp_float[i - 1, j + 1]
    #                                  + temp_float[i + 1, j - 1]
    #                                  + temp_float[i + 1, j + 1]) / 4
    #             else:
    #                 # 奇数行 的 奇数列，上下之和的平均
    #                 r_float[i, j] = (temp_float[i - 1, j] + temp_float[i + 1, j]) / 2


            # G配列




            # B配列


    print(r_float)

    print("0-255 变换")

    # 0-255 变换
    for i, row in enumerate(temp_float):
        for j, value in enumerate(row):
            r_float[i, j] = math.ceil(r_float[i, j] / 255)
            g_float[i, j] = math.ceil(g_float[i, j] / 255)
            b_float[i, j] = math.ceil(b_float[i, j] / 255)

    print(r_float)

    # Finally, 输出图像
    # fig = plt.figure()
    # fig.add_subplot(1, 3, 1)
    # plt.imshow(r_float)
    # fig.add_subplot(1, 3, 2)
    # plt.imshow(g_float)
    # fig.add_subplot(1, 3, 3)
    # plt.imshow(b_float)
    im_rgb = np.dstack((r_float, g_float, b_float))
    
    plt.imshow(im_rgb)
    plt.show()
    print("---------  END  ---------")


if __name__ == "__main__":
    main()