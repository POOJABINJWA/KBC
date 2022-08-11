question_list=["how many continents are there?",
               "what is capital of india?",
               "NG me konsa curse padhaya jata hai?",
              ]  
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],
                    ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
                   ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list = [3, 4, 1]     
lifeline = [['1.Four','3.seven'],
            ['2.Bhopal','4.Delhi'],
            ['1.Software Engineering','2.Counseling']]
print("welcome to KBC")
print("your game starts now")
   
i=0
money=0
c=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
          d=options_list[i][j]
          print(d)
          j=j+1
    if c<2:
        user_input=input("do yo using lifeline :")
        if user_input=="yes":
            c=c+1
            print("5050",lifeline[i])
    else:
        print("you cant use lifeline bacause you already use two lifeline")
    b=int(input("choose correct answer"))
    if b==solution_list[i]:
        money=money+5000
        print("your answer is correct")
        print("you win RS./-",money)
    else:
        print("your answer is wrong")
        break
    i=i+1


    

