import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    
    kk_img = pg.image.load("ex01/fig/3.png") #こうかとん画像 読み込み
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img2 = pg.transform.rotozoom(kk_img,10, 1.0)
    kk_img3 = pg.transform.rotozoom(kk_img,20, 1.0)
    kk_img4 = pg.transform.rotozoom(kk_img,30 ,1.0)
    kk_imgs = [kk_img,kk_img2,kk_img3,kk_img4]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200 #横に進める変数
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        
        screen.blit(kk_imgs[tmr%len(kk_imgs)],[300,200])
        pg.display.update()
        tmr+=1
        clock.tick(1000)
        
        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()