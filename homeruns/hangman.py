
from pickle import FALSE, TRUE
import random
import time

print("Welcome to Hangman game")
name = input("Enter your name: ").upper()

print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!")
print("Let's play Hangman!")
time.sleep(3)





def hangman():
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants", "player", "worker", "escalator", "enumerate", "welcome","blush","blushing","board","boast","boat","boil","boiling","bolt","bomb","bone","book","books","boorish","boot","border","bore","bored","boring","borrow","bottle","bounce","bouncy","boundary","boundless","bow","box","boy","brainy","brake","branch","brash","brass","brave","brawny","breakable","breath","breathe","breezy","brick","bridge","brief","bright","broad","broken","brother","brown","bruise","brush","bubble","bucket","building","bulb","bump","bumpy","burly","burn","burst","bury","bushes","business","bustling","busy","butter","button","buzz","cabbage","cable","cactus","cagey","cake","cakes","calculate","calculating","calculator","calendar","call","callous","calm","camera","camp","can","cannon","canvas","cap","capable","capricious","caption","car","card","care","careful","careless","caring","carpenter","carriage","carry","cars","cart","carve","cast","cat","cats","cattle","cause","cautious","cave","ceaseless","celery","cellar","cemetery","cent","certain","chalk","challenge","chance","change","changeable","channel","charge","charming","chase","cheap","cheat","check","cheer","cheerful","cheese","chemical","cherries","cherry","chess","chew","chicken","chickens","chief","childlike","children","chilly","chin","chivalrous","choke","chop","chubby","chunky","church","circle","claim","clam","clammy","clap","class","classy","clean","clear","clever","clip","cloistered","close","closed","cloth","cloudy","clover","club","clumsy","cluttered","coach","coal","coast","coat","cobweb","coherent","coil","cold","collar","collect","color","colorful","colossal","colour","comb","combative","comfortable","command","committee","common","communicate","company","compare","comparison","compete","competition","complain","complete","complex","concentrate","concern","concerned","condemned","condition","confess","confuse","confused","connect","connection","conscious","consider","consist","contain","continue","control","cooing","cook","cool","cooperative","coordinated","copper","copy","corn","correct","cough","count","country","courageous","cover","cow","cowardly","cows","crabby","crack","cracker","crash","crate","craven","crawl","crayon","crazy","cream","creator","creature","credit","creepy","crib","crime","crook","crooked","cross","crow","crowd","crowded","crown","cruel","crush","cry","cub","cuddly","cultured","cumbersome","cup","cure","curious","curl","curly","current","curtain","curve","curved","curvy","cushion","cut","cute","cycle","cynical","dad","daffy","daily","dam","damage","damaged","damaging","damp","dance","dangerous","dapper","dare","dark","dashing","daughter","day","dazzling","dead","deadpan","deafening","dear","death","debonair","debt","decay","deceive","decide","decision","decisive","decorate","decorous","deep","deeply","deer","defeated","defective","defiant","degree","delay","delicate","delicious","delight","delightful","delirious","deliver","demonic","depend","dependent","depressed","deranged","describe","descriptive","desert","deserted","deserve","design","desire","desk","destroy","destruction","detail","detailed","detect","determined","develop","development","devilish","didactic","different","difficult","digestion","diligent","dime","dinner","dinosaurs","direction","direful","dirt","dirty","disagree","disagreeable","disappear","disapprove","disarm","disastrous","discover","discovery","discreet","discussion","disgusted","disgusting","disillusioned","dislike","dispensable","distance","distinct","distribution","disturbed","divergent","divide","division","dizzy","dock","doctor","dog","dogs","doll","dolls","domineering","donkey","door","double","doubt","doubtful","downtown","drab","draconian","drag","drain","dramatic","drawer","dream","dreary","dress","drink","drip","driving","drop","drown","drum","drunk","dry","duck","ducks","dull","dust","dusty","dynamic","dysfunctional","eager","ear","early","earn","earsplitting","earth","earthquake","earthy","easy","eatable","economic","edge","educate","educated","education","effect","efficacious","efficient","egg","eggnog","eggs","eight","elastic","elated","elbow","elderly","electric","elegant","elfin","elite","embarrass","embarrassed","eminent","employ","empty","enchanted","enchanting","encourage","encouraging","end","endurable","energetic","engine","enjoy","enormous","enter","entertain","entertaining","enthusiastic","envious","equable","equal","erect","erratic","error","escape","ethereal","evanescent","evasive","even","event","examine","example","excellent","exchange","excite","excited","exciting","exclusive","excuse","exercise","exist","existence","exotic","expand","expansion","expect","expensive","experience","expert","explain"]
    word = random.choice(words_to_guess)
    length = len(word)
    already_guessed = []
    correct_guess = []
    limit = 7
    done = False
    while not done and limit > 0:
        for letter in word:
            if letter.upper() in already_guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
         
        print(f"remaining tries left: {limit}")
        guess = (input("what is your next guess: "))
        already_guessed.append(guess.upper())
        if guess.lower() in word.lower():
                correct_guess += guess.lower()
        if guess.upper() not in word.upper():
            limit -= 1
            if limit == 0:
                break
        if correct_guess == word:
            print("you win")
        print(correct_guess, word)
        print(already_guessed, word)
        if correct_guess == word:
            print(f"you won!, the word was {word}")
        print(correct_guess, word)   
    for letter in word:
        if letter.upper() not in already_guessed:
            done = False
    if already_guessed == word:
        print(f"you win!, the word was {word}")
    if already_guessed != word:
        print(f"game over! :), the word was {word}")

    while input("play again? (Y/N): ").upper() == "Y":
        return hangman()

    print("goodbye")
hangman()