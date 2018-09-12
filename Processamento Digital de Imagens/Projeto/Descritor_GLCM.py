import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.color import rgb2grey
from skimage.feature import greycomatrix, greycoprops
from skimage.io import imread, show, imshow
from skimage import exposure
import glob as g


def descritor():

    Alprazolam = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segAlprazolam/*.png")
    Domino = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segDomino/*.png")
    Medium = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segMedium cut/*.png")
    Tesla = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segTesla/*.png")
    Warner = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segWarner Bros/*.png")
    
#    Alprazolam = g.glob("C:/Users/Labvis/Desktop/SIIM/Alprazolam/*.jpg")
#    Domino = g.glob("C:/Users/Labvis/Desktop/SIIM/Domino/*.jpg")
#    Medium = g.glob("C:/Users/Labvis/Desktop/SIIM/Medium cut/*.jpg")
#    Tesla = g.glob("C:/Users/Labvis/Desktop/SIIM/Tesla/*.jpg")
#    Warner = g.glob("C:/Users/Labvis/Desktop/SIIM/Warner Bros/*.jpg")    
    

    d = 1
   # l = []
    for i, value in enumerate(Alprazolam):
        image = cv2.imread(value, 0)
        matrix_GLCM = greycomatrix(image, [d], [0], normed=True)
        vetor = np.zeros(6)
        print(np.squeeze(matrix_GLCM).max())
        plt.imshow(np.log10((np.squeeze(matrix_GLCM))))
        plt.axis('off')
        
        vetor[0] = (greycoprops(matrix_GLCM, 'contrast'))
        vetor[1] = (greycoprops(matrix_GLCM, 'dissimilarity'))
        vetor[2] = (greycoprops(matrix_GLCM, 'homogeneity'))
        vetor[3] = (greycoprops(matrix_GLCM, 'energy'))
        vetor[4] = (greycoprops(matrix_GLCM, 'correlation'))
        vetor[5] = (greycoprops(matrix_GLCM, 'ASM'))
        file_save(vetor, '0')  # one
    #    l.append(vetor)
        print('Alprazolam ->', value)

    for i, value in enumerate(Domino):
        image = cv2.imread(value, 0)
        matrix_GLCM = greycomatrix(image, [d], [0], normed=True)
        vetor = np.zeros(6)

        vetor[0] = (greycoprops(matrix_GLCM, 'contrast'))
        vetor[1] = (greycoprops(matrix_GLCM, 'dissimilarity'))
        vetor[2] = (greycoprops(matrix_GLCM, 'homogeneity'))
        vetor[3] = (greycoprops(matrix_GLCM, 'energy'))
        vetor[4] = (greycoprops(matrix_GLCM, 'correlation'))
        vetor[5] = (greycoprops(matrix_GLCM, 'ASM'))
        file_save(vetor, '1')  # one
        print('Domino ->', value)
      
    for i, value in enumerate(Medium):
        image = cv2.imread(value, 0)
        matrix_GLCM = greycomatrix(image, [d], [0], normed=True)
        vetor = np.zeros(6)

        vetor[0] = (greycoprops(matrix_GLCM, 'contrast'))
        vetor[1] = (greycoprops(matrix_GLCM, 'dissimilarity'))
        vetor[2] = (greycoprops(matrix_GLCM, 'homogeneity'))
        vetor[3] = (greycoprops(matrix_GLCM, 'energy'))
        vetor[4] = (greycoprops(matrix_GLCM, 'correlation'))
        vetor[5] = (greycoprops(matrix_GLCM, 'ASM'))
        file_save(vetor, '2')  # one
        print('Medium ->', value)
        
    for i, value in enumerate(Tesla):
        image = cv2.imread(value, 0)
        matrix_GLCM = greycomatrix(image, [d], [0], normed=True)
        vetor = np.zeros(6)

        vetor[0] = (greycoprops(matrix_GLCM, 'contrast'))
        vetor[1] = (greycoprops(matrix_GLCM, 'dissimilarity'))
        vetor[2] = (greycoprops(matrix_GLCM, 'homogeneity'))
        vetor[3] = (greycoprops(matrix_GLCM, 'energy'))
        vetor[4] = (greycoprops(matrix_GLCM, 'correlation'))
        vetor[5] = (greycoprops(matrix_GLCM, 'ASM'))
        file_save(vetor, '3')  # one
        print('Tesla ->', value)  

    for i, value in enumerate(Warner):
            image = cv2.imread(value, 0)
            matrix_GLCM = greycomatrix(image, [d], [0], normed=True)
            vetor = np.zeros(6)
            
    
            vetor[0] = (greycoprops(matrix_GLCM, 'contrast'))
            vetor[1] = (greycoprops(matrix_GLCM, 'dissimilarity'))
            vetor[2] = (greycoprops(matrix_GLCM, 'homogeneity'))
            vetor[3] = (greycoprops(matrix_GLCM, 'energy'))
            vetor[4] = (greycoprops(matrix_GLCM, 'correlation'))
            vetor[5] = (greycoprops(matrix_GLCM, 'ASM'))
            file_save(vetor, '4')  # one
        #    l.append(vetor)
            print('Warner ->', value)
    

    return matrix_GLCM

def file_save(vetor, label):

    file = open('validation_001.libsvm', 'a+')
    file.write(str(label)+" "+" ".join(str(i+1)+":"+str(pix) for i, pix in enumerate(vetor))+"\n")
    file.close()


if __name__ == '__main__':
    l = descritor()
    print("arroz");
