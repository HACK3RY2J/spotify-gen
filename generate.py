import random, os, sys
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']

# The Credit For This Code Goes To Panda Hackers https://github.com/HACK3RY2J/Spotify-gen/
# If You Wanna Take Credits, Please Look Yourself Again!!
# A Special Thanks To Yuvi!!

Accounts = ['clarky1980@hotmail.co.uk:Liam2002 | Spotify Premium Family | Cracked By HACK3RY2J', 'harrison.pershing@yahoo.com:Harrison51 | Spotify Premium | Cracked By HTH', 'neilkoschier@web.de:Ne3il4Ko5 | Spotify Premium | Cracked By HTH', 'snakeeyes185@gmail.com:Familj10 | Spotify Premium Family | Cracked By HTH', 'mr.c.williams@hotmail.com:77success | Spotify Premium | Cracked By HTH', 'philler_bunnies@hotmail.com:Alefzero0 | Spotify Premium Family | Cracked By Yuvi', 'clarky1980@hotmail.co.uk:Liam2002 | Spotify Premium Family | Cracked By HACK3RY2J', 'philler_bunnies@hotmail.com:Alefzero0 | Spotify Premium Family | Cracked By Yuvi', 'marcusgaultmuppet@googlemail.com:9r6arefy | Spotify Premium | Cracked By HACK3RY2J', 'bollomercado@hotmail.com:saxo24905 | Spotify Premium Family | Cracked By HACK3RY2J', 'uguraytugkacar@gmail.com:Ugur2003 | Spotify Premium Family | Cracked By HACK3RY2J', 'rothpatrick2@yahoo.com:pdflyer234 | Spotify Premium Family | Cracked By HTH', 'crispcalls@hotmail.com:cris1787 | Spotify Free | Cracked By HTH', 'clarky1980@hotmail.co.uk:Liam2002 | Spotify Premium Family | Cracked By HACK3RY2J', 'pedroab1186@aol.com:abel1182 | Spotify Premium | Cracked By HTH', 'blitz_biene@web.de:Bildung4 | Spotify Premium Family | Cracked By HTH', 'rothpatrick2@yahoo.com:pdflyer234 | Spotify Premium Family | Cracked By HTH', 'clarky1980@hotmail.co.uk:Liam2002 | Spotify Premium Family | Cracked By HACK3RY2J', 'snakeeyes185@gmail.com:Familj10 | Spotify Premium Family | Cracked By HTH', 'rothpatrick2@yahoo.com:pdflyer234 | Spotify Premium Family | Cracked By HTH', 'rothpatrick2@yahoo.com:pdflyer234 | Spotify Premium Family | Cracked By HTH', 'Spotify Premium | fla_th@yahoo.com.br:210377 | Cracked By HTH', 'Spotify Premium Duo | comeeverhere@hotmail.com:segredo55 | Cracked By HTH', 'Family Member | tayna_sena95@hotmail.com:seninha | Cracked By HTH', 'Spotify Premium | rf10_@hotmail.com:28111994 | Cracked By HTH', 'Family Member | brunaoliveira994@bol.com.br:bruna10 | Cracked By HTH', 'Spotify Premium Duo | glei.pongeti@hotmail.com:58210797 | Cracked By HTH', 'Family Member | joao_eduardo1@hotmail.com:16111994 | Cracked By HTH', 'Family Member | laryanekarina@hotmail.com:lary2101 | Cracked By HTH', 'Family Member | flavioribeiro999@hotmail.com:gabiroba | Cracked By HTH', 'Family Member | nanda2bs@yahoo.com.br:fer20cla | Cracked By HTH', 'Premium for Students | kauana-gouveia@hotmail.com:452369 | Cracked By HTH', 'Family Member | renata_cfoliver@hotmail.com:013579 | Cracked By HTH', 'Family Member | naiaratalita@hotmail.com:99273586 | Cracked By HTH', 'Family Member | b.n.s.verdao@gmail.com:renata100 | Cracked By HTH', 'Family Member | chicocavalca@gmail.com:chico58985 | Cracked By HTH', 'Spotify Premium | amanda_soares_13@hotmail.com:sacerdote | Cracked By HTH', 'Family Member | lbnascimento48@hotmail.com:izumeraki | Cracked By HTH', 'Family Member | camilasonoda@msn.com:csg210995 | Cracked By HTH', 'Premium for Students | celso.jr.07@gmail.com:cel970216 | Cracked By HTH', 'Spotify Premium | alexandre.tandy@gmail.com:certezas | Cracked By HTH', 'Spotify Premium | rubensalencarc@hotmail.com:pakalolo | Cracked By HTH', 'Spotify Premium | anymaq@hotmail.com:276510 | Cracked By HTH', 'Premium for Students | ingridymiilhomem@gmail.com:93709911 | Cracked By HTH', 'Premium for Students | karoline.cst@gmail.com:91045703 | Cracked By HTH', 'Family Member | lisandralucas@hotmail.com:91356420 | Cracked By HTH', 'Premium for Students | geovanivilela@yahoo.com.br:inavoeg | Cracked By HTH', 'Family Member | pytuka_am@yahoo.com.br:88034485 | Cracked By HTH', 'Family Member | degeeliane@hotmail.com:141281 | Cracked By HTH', 'Spotify Premium | tmirys@hotmail.com:bichinhos | Cracked By HTH', 'Family Member | orcedinojunior@gmail.com:luanalua | Cracked By HTH', 'Family Member | evelyn.teles@gmail.com:153621 | Cracked By HTH', 'Premium for Students | fchioatto@gmail.com:desenho | Cracked By HTH', 'Family Member | biancarosalima@gmail.com:elzaneri | Cracked By HTH', 'Premium for Students | ellen.b@hotmail.com.br:ellen1707 | Cracked By HTH', 'Family Member | davidalves.alves1@gmail.com:bicodepato | Cracked By HTH', 'Family Member | biiagodoy@gmail.com:45672909 | Cracked By HTH', 'Family Member | caique_iamthegreatest@live.com:astracruze | Cracked By HTH', 'Family Member | paulacarol2001@hotmail.com:31712701 | Cracked By HTH', 'Family Member | alzemirmds@gmail.com:742114257 | Cracked By HTH', 'Spotify Premium | pg.pinheiro@hotmail.com:gui88808 | Cracked By HTH', 'Spotify Premium | isaa.jpf@gmail.com:21348966 | Cracked By HTH', 'Family Member | juninho.hora10@hotmail.com:270294 | Cracked By HTH', 'Spotify Premium | keityane@gmail.com:k1k2k3 | Cracked By HTH', 'Family Member | vitor.syrio@hotmail.com:030493vi | Cracked By HTH', 'Family Member | veraferreira2007@hotmail.com:bonita47 | Cracked By HTH', 'Family Member | guhoog@hotmail.com:conversas1 | Cracked By HTH', 'Premium for Students | s2talytas2@hotmail.com:223200 | Cracked By HTH', 'Family Member | yahia@uol.com.br:yjhh6212 | Cracked By HTH', 'Family Member | milok10@gmail.com:123456 | Cracked By HTH', 'Family Member | murielleeu@hotmail.com:murielli | Cracked By HTH', 'Family Member | michellemep@gmail.com:Mi770100 | Cracked By HTH', 'Spotify Premium Duo | toneolive00@gmail.com:tone1995| Cracked By HTH', 'sznenci@gmail.com:Andriska01 | Spotify Premium Family Member | Cracked By HTH', 'aurore.meunier4@gmail.com:Citronvert01 | Spotify Premium Family Owner | Cracked By HTH', 'tcarregal@gmail.com:Paquito1 | Spotify Premium | Cracked By HTH', 'jennifer.chhean@gmail.com:Jennifer11 | Spotify Premium Family Member | Cracked By HTH', 'cindy.schultz01@gmail.com:Phoenix01 | Spotify Premium | Cracked By HTH', 'mat.morris@me.com:Riller77! | Spotify Premium | Cracked By HTH', 'lmorales306@gmail.com:Isamor21 | Spotify Premium Family Member | Cracked By HTH', 'tiago32.tv@gmail.com:Enzo1601 | Spotify Premium | Cracked By HTH', 'jaime.h.kim@gmail.com:Seoul001 | Spotify Premium Family Member | Cracked By HTH', 'abbeymaem2298@gmail.com:PickleKat12 | Spotify Premium overline:Trial | Cracked By HTH', 'lucas.piedade@gmail.com:Jardimbrasil450 | Spotify Premium Family Member | Cracked By HTH', 'kimhanbyul77@gmail.com:Widso001 | Spotify Premium | Cracked By HTH', 'sarahyeates88@me.com:Mutley01 | Spotify Premium | Cracked By HTH', 'rayann06@outlook.com:Marseille12 | Spotify Premium Family Member | Cracked By HTH', 'marciasottas@msn.com:Thaynan99 | Spotify Premium Family Member | Cracked By HTH', 'philippa.ginsberg@gmail.com:Figero123 | Spotify Premium Family Owner | Cracked By HTH', 'pedroab1186@aol.com:abel1182 | Spotify Premium | Cracked By HTH', 'crispcalls@hotmail.com:cris1787 | Spotify Free | Cracked By HTH', 'tieraray1234@gmail.com:704819012 | Premium for Students | Cracked By HTH', 'snakeeyes185@gmail.com:Familj10 | Spotify Premium Family | Cracked By HTH', 'crispcalls@hotmail.com:cris1787 | Spotify Free | Cracked By HTH', 'rothpatrick2@yahoo.com:pdflyer234 | Spotify Premium Family | Cracked By HTH', 'snakeeyes185@gmail.com:Familj10 | Spotify Premium Family | Cracked By HTH', 'bollomercado@hotmail.com:saxo24905 | Spotify Premium Family | Cracked By HACK3RY2J', 'tieraray1234@gmail.com:704819012 | Premium for Students | Cracked By HTH', 'marcusgaultmuppet@googlemail.com:9r6arefy | Spotify Premium | Cracked By HACK3RY2J', 'pedroab1186@aol.com:abel1182 | Spotify Premium | Cracked By HTH', 'harrison.pershing@yahoo.com:Harrison51 | Spotify Premium | Cracked By HTH', 'philler_bunnies@hotmail.com:Alefzero0 | Spotify Premium Family | Cracked By Yuvi', 'uguraytugkacar@gmail.com:Ugur2003 | Spotify Premium Family | Cracked By HACK3RY2J', 'uguraytugkacar@gmail.com:Ugur2003 | Spotify Premium Family | Cracked By HACK3RY2J', 'mr.c.williams@hotmail.com:77success | Spotify Premium | Cracked By HTH', 'pedroab1186@aol.com:abel1182 | Spotify Premium | Cracked By HTH', 'harrison.pershing@yahoo.com:Harrison51 | Spotify Premium | Cracked By HTH', 'snakeeyes185@gmail.com:Familj10 | Spotify Premium Family | Cracked By HTH', 'mr.c.williams@hotmail.com:77success | Spotify Premium | Cracked By HTH', 'harrison.pershing@yahoo.com:Harrison51 | Spotify Premium | Cracked By HTH', 'philler_bunnies@hotmail.com:Alefzero0 | Spotify Premium Family | Cracked By Yuvi', 'bollomercado@hotmail.com:saxo24905 | Spotify Premium Family | Cracked By HACK3RY2J', 'bollomercado@hotmail.com:saxo24905 | Spotify Premium Family | Cracked By HACK3RY2J', 'marcusgaultmuppet@googlemail.com:9r6arefy | Spotify Premium | Cracked By HACK3RY2J', 'snakeeyes185@gmail.com:Familj10 | Spotify Premium Family | Cracked By HTH', 'blitz_biene@web.de:Bildung4 | Spotify Premium Family | Cracked By HTH', 'bollomercado@hotmail.com:saxo24905 | Spotify Premium Family | Cracked By HACK3RY2J', 'uguraytugkacar@gmail.com:Ugur2003 | Spotify Premium Family | Cracked By HACK3RY2J', 'blitz_biene@web.de:Bildung4 | Spotify Premium Family | Cracked By HTH', 'mr.c.williams@hotmail.com:77success | Spotify Premium | Cracked By HTH', 'bollomercado@hotmail.com:saxo24905 | Spotify Premium Family | Cracked By HACK3RY2J', 'neilkoschier@web.de:Ne3il4Ko5 | Spotify Premium | Cracked By HTH', 'uguraytugkacar@gmail.com:Ugur2003 | Spotify Premium Family | Cracked By HACK3RY2J', 'clarky1980@hotmail.co.uk:Liam2002 | Spotify Premium Family | Cracked By HACK3RY2J', 'rothpatrick2@yahoo.com:pdflyer234 | Spotify Premium Family | Cracked By HTH', 'bollomercado@hotmail.com:saxo24905 | Spotify Premium Family | Cracked By HACK3RY2J', 'crispcalls@hotmail.com:cris1787 | Spotify Free | Cracked By HTH', 'marcusgaultmuppet@googlemail.com:9r6arefy | Spotify Premium | Cracked By HACK3RY2J', 'blitz_biene@web.de:Bildung4 | Spotify Premium Family | Cracked By HTH']
AC = print(random.choice(Accounts))

os.system("clear")
os.system("toilet -fmono12 -F gay SPOTIFY ")
print("██████████████████████████████████████████████████████████████")
print("██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
print("██        Code Made by github.com/HACK3RY2J                 ██")
print("██   Youtube : https://www.youtube.com/c/PandaHackers       ██")
print("██ Instagram : https://instagram.com/Panda_Hackers_Official ██")
print("██████████████████████████████████████████████████████████████")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print()
print("Free Spotify Account Generator")
print("Last Updated On 10/03/2020")
print()
op = input("Type 1 To Generate Account : ")
if op == "1" :
    print(AC)
else :
   print(" Enter a valid option... ")
