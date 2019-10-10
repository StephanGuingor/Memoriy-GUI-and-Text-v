from random import shuffle
import time
import os
class Cards:
    def __init__(self,card_list,art_cover):
        self.card_list=card_list #LIST #SHUFFLE
        self.card_list_size=len(card_list)
        self.art_cover_s=art_cover #BACKPART
    def len(self):
        return len(self.card_list)

    def shuffle_l(self):
        return shuffle(self.card_list)
    def art_cover(self):
        return self.art_cover_s
    
    def index(self,index):
        return self.card_list[index]
class Board:
    def __init__(self,card_list_obj,rules,size=4):
        self.card_list_obj = card_list_obj.shuffle_l
        self.size = size
        self.rules = rules
        self.no_rep_list=[]
    def position(self,index):
        position_list = ["A1","A2","A3","A4","B1","B2","B3","B4","C1","C2","C3","C4","D1","D2","D3","D4"]
        return position_list[index]

    def dictionary_maker(self,card_list_obj):
        index=0
        position_holder={}
       
        
        while index <16:
            position_list1 = self.position(index)
            position_holder[position_list1] = [card_list_obj.index(index),card_list_obj.art_cover()]
            index += 1
        print(position_holder)
        return position_holder

    def append_no_rep(self,value):
        self.no_rep_list.append(value)
        return self.no_rep_list

    def show_no_rep(self):
        return self.no_rep_list

    def print_draw(self,card_list_obj):
        dictionary = self.dictionary_maker(card_list_obj)
        user = input("\n...Ready to play...\n").lower()
        column = "Ready"
        row = "Ready"
        n=0
        tries=0
        if user == "si":
            while column != "QUIT" or row !="quit" or n <=8 or tries>50:
                tries += 1
                os.system('clear')
                print(" "," A  ","B  ","C  ","D  ")
                print("1",dictionary['A1'][1],dictionary['B1'][1],dictionary["C1"][1],dictionary["D1"][1],"\n")
                print("2",dictionary["A2"][1],dictionary["B2"][1],dictionary["C2"][1],dictionary["D2"][1],"\n")
                print("3",dictionary["A3"][1],dictionary["B3"][1],dictionary["C3"][1],dictionary["D3"][1],"\n")
                print("4",dictionary["A4"][1],dictionary["B4"][1],dictionary["C4"][1],dictionary["D4"][1],"\n\n\n")
                print(f"Score = {n}\n")
                column = input("Choose the column:").upper()
                row = input("Choose the row:")
                answer1 = (column+row).strip()
                if column != "QUIT" or row!="quit":
                    if answer1 in dictionary.keys():
                        dictionary[answer1][1] = dictionary[answer1][0]
                        new_value1 = dictionary[answer1][1]
                        os.system('clear')
                        print(" "," A  ","B  ","C  ","D  ")
                        print("1",dictionary['A1'][1],dictionary['B1'][1],dictionary["C1"][1],dictionary["D1"][1],"\n")
                        print("2",dictionary["A2"][1],dictionary["B2"][1],dictionary["C2"][1],dictionary["D2"][1],"\n")
                        print("3",dictionary["A3"][1],dictionary["B3"][1],dictionary["C3"][1],dictionary["D3"][1],"\n")
                        print("4",dictionary["A4"][1],dictionary["B4"][1],dictionary["C4"][1],dictionary["D4"][1],"\n\n\n")
                        print(f"Score = {n}\n")

                        column = input("Choose a new column:").upper()
                        row = input("Choose a new row:")
                        answer2 = (column+row).strip()
                    
                        if answer1 != answer2:
                            if column!= "QUIT" or row!="quit":
                                if answer2 in dictionary.keys():
                                    dictionary[answer2][1] = dictionary[answer2][0]
                                    new_value2 = dictionary[answer2][1]
                                    os.system('clear')
                                    print(" "," A  ","B  ","C  ","D  ")
                                    print("1",dictionary['A1'][1],dictionary['B1'][1],dictionary["C1"][1],dictionary["D1"][1],"\n")
                                    print("2",dictionary["A2"][1],dictionary["B2"][1],dictionary["C2"][1],dictionary["D2"][1],"\n")
                                    print("3",dictionary["A3"][1],dictionary["B3"][1],dictionary["C3"][1],dictionary["D3"][1],"\n")
                                    print("4",dictionary["A4"][1],dictionary["B4"][1],dictionary["C4"][1],dictionary["D4"][1],"\n\n\n")
                                    print(f"Score = {n}\n")
                                    time.sleep(2)

                                    if new_value1 == new_value2 and new_value1 not in self.show_no_rep():
                                        print("You got a pair!")
                                        n+=1
                                        self.append_no_rep(new_value1)
                                    else:
                                        if new_value1 in self.show_no_rep():
                                            print("YOU ALREADY HAVE THAT\n")
                                        else:
                                            print("No luck")
                                            dictionary[answer1][1]=card_list_obj.art_cover()
                                            dictionary[answer2][1]=card_list_obj.art_cover()
                                else:
                                    print("\nENTER VALID INPUT(2)\n")
                            else:
                                tries = 100
                                break
                        else:
                            print("Repeated value")
                    else:
                        print("\nENTER VALID INPUT\n")
                else:
                    tries = 100
                    break
                    
            else:
                if n >= 8:
                    print(f"You won in {tries} tries")
                elif tries>50:
                    print("You lost, too many tries")
                else:
                    print("BYE")
        else:
            print("BYE")