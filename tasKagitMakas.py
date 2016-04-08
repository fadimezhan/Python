
def tasKagitMakas(player1, player2):
    message1 = "1. oyuncu kazandi!"
    message2 = "2. oyuncu kazandi!"
    message3 = "Berabere"
    message4 = "Hatali veri girisi!"
    # 1. oyuncu kazandiysa geriye 1 degeri
    # 2. oyuncu kazandiysa geriye 2 degeri
    # Berabere ise geriye 0 degeri
    # Veri girisinde hata varsa geriye -1 dondurulecektir.
    #kodunuz buraya
    #

    if ((player1 == "tas" & player2 == "makas")|(player1=="kagit")&(player2=="tas")):
        return 1

    #
    #
    return 0, message3 # ilk parametre sonuc,
    # ikinci parametre ise string olarak kimin kazandigini belirtmektedir.

def test():#Burasi test kodudur. Herhangi bir degisiklik yapmayin.
    #ustteki fonksiyonu duzgun yazdip kodu calistirdiginizda hata vermiyorsa
    #testleri basariyla gecmissiniz demektir.
    errorMessage = "Yanlis sonuc"
    inputErrorMessage = "Hatali veri girisi"
    assert tasKagitMakas("tas", "tas") == 0, errorMessage
    assert tasKagitMakas("tas", "kagit") == 2, errorMessage
    assert tasKagitMakas("tas", "makas") == 1, errorMessage
    assert tasKagitMakas("kagit", "kagit") == 0, errorMessage
    assert tasKagitMakas("kagit", "tas") == 1, errorMessage
    assert tasKagitMakas("kagit", "makas") == 2, errorMessage
    assert tasKagitMakas("makas", "makas") == 0, errorMessage
    assert tasKagitMakas("makas", "kagit") == 1, errorMessage
    assert tasKagitMakas("makas", "tas") == 2, errorMessage
    assert tasKagitMakas("kalem", "tas") == -1, inputErrorMessage
    assert tasKagitMakas("makas", "kalem") == -1, inputErrorMessage


test()
# kullanicidan 2 string isteyen ve sonucu ekrana yazdiran programi yaziniz.
# Orn:
# player1:tas
# player2:kagit
# 2. oyuncu kazandi
# Program tekrar tekrar soracak. 1. oyuncu 'cikis' yazdiginda ise programi sonlandirilacak.