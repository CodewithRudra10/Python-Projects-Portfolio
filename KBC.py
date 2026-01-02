Questions =["Who is Current Prime Minister of India?",
"Narendra Modi","Manmohan Singh","HD Devegowda","IK Gujral",1 ]
[
    "Who invented Python?",
"Guido Van Roussum","Michael Faraday","Robert Brown","John Ford",1]
[
    "In which continent does India is located?",
    "Asia","Africa","Australia","Europe",1]

[
    "Name the highest peak of the world?",
    "Nandi Hills","Mt Everest","Shiwaliks","Himadri",2]

levels=[1000,2000,3000,4000]

for i in range(0, len(Questions)):
    Question= Questions[i]
    print(f"Question for Rs. {levels[i]}" )
    print(Questions)
    print(f"a. {Questions[1]}            b.{Questions[2]} ")
    print(f"c. {Questions[3]}            d.{Questions[4]} ")      
    reply=int(input("Enter Your Answer (1-4)"))
if(reply == Questions(-4)):
    print(f"Correct Answer You have won Rs. levels{i}")
    if (i==1):
        money=1000
    else:
        print("Wrong Answer")

        print("you can take this money to home")
            
        
          