import sys
from skimage import io
import numpy as np

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
    b_float = a_float.copy()

    print(" 3. 线性化操作")

    for i, row in enumerate(a_float):
        print("Row {}: {}".format(i, row))
        for j, value in enumerate(row):
            if(value <= BLACK_LIMITED):
                b_float[i, j] = 0

            elif(value >= WHITE_LIMITED):
                b_float[i, j] = 1
            else:
                b_float[i, j] = value / (WHITE_LIMITED - BLACK_LIMITED)
    
    print(b_float)

    print(" 4. 确定图像的合理的 Bayer 模式")




    

    print("---------  END  ---------")


if __name__ == "__main__":
    main()