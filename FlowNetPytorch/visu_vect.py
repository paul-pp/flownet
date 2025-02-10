
import cv2

def gen_noyau_lissage(p):
    L=[]
    for k in range(2*p+1):
        L.append([1/((2*p+1)**2)] * (2*p+1)) 
    return L
    



def convo_loc(i,j,p,flow_output,L):
    s1=0
    s2=0
    for k in range (2*p+1):
        for l in range (2*p+1):
            v1=flow_output[0][j+l-p][i+k-p]
            v2=flow_output[1][j+l-p][i+k-p]
            s1=s1+(v1*(L[l][k]))
            s2=s2+(v2*(L[l][k]))

    return (s1,s2)


def create_im_vect(img1_file,name_img_vect,flow_output,L,facteur):
    # shutil.copy(img1_file,name_img_vect)
    img = cv2.imread(img1_file)
    w=len(flow_output[0][0])
    h=len(flow_output[0])
    img=cv2.resize(img, (w,h), interpolation = cv2.INTER_AREA)
    if img is None:
        print('impossible de charger les données du fichier')
    # img=cv2.arrowedLine(img, start_pt, end_pt, (0, 255, 0), 9)

    p=len(L)//2
    for i in range (p,w-p,p): 
        for j in range (p,h-p,p):
            # (start_pt,end_pt)=([0,0],[0,0])
            start_pt=[i,j]
            (e1,e2)=convo_loc(i,j,p,flow_output,L)
            end_pt=(i+int(e1*facteur),j+int(e2*facteur))
            img=cv2.arrowedLine(img, start_pt, end_pt, (70, 255, 255), 1, cv2.LINE_AA, 0, 0.1)

    cv2.imwrite(name_img_vect, img)

    return 0

