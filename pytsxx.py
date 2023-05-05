import pyttsx3 as p
name=["sonu","Lalit","Prakhar","Ram","Jays","KD","JD"]
student = ["Fail","Pass","Pass","Pass",
"Pass","Pass","Fail","Pass","Fail","Fail","Fail"]
engine=p.init()
for i in range(len(name)):
    engine.say(f"The Student name {name[i]} and Status is {student[i]}")
    engine.runAndWait()