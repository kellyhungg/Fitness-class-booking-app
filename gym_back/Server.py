import datetime
from flask import *
from gym.Tools import GetBranch, GetCoachDatas, GetCourseDatas, PostGet, GetMyPlans, GYMSignUp,GYMSignIn,GYMPostUpload,GYMJoinUs,GYMEditMyDatas

app = Flask(__name__)
TodayTime=''

def CheckToday():
    Time=str(datetime.date.today())
    file=open('Time.txt', 'r+')
    if(Time!=file.read()):
        file.close()
        file = open('Time.txt', 'w+')
        file.write(Time)
        file.close()
        GetBranch.GetBranch()
        GetCoachDatas.GetCoachDatas()
        GetCourseDatas.GetCourseDatas()
        PostGet.GetPost()
        return False
    else:
        return True

@app.route("/")
def Hello():
    return 'Hello,Welcome to My API for \"GYMSTER\" APP'

@app.route('/Put/EditMyDatas',methods=['POST'])
def EditMyDatas():
    Input = request.get_json()
    Member_ID = Input['Member_ID']
    Name = Input['Name']
    Phone_Number = Input['Phone_Number']
    Email = Input['Email']
    Password = Input['Password']
    return GYMEditMyDatas.EditInfo(Member_ID,Name,Phone_Number,Password,Email)

@app.route('/Post/JoinUs',methods=['POST'])
def JoinUs():
    Input = request.get_json()
    Gym_Name=Input['Gym_Name']
    Coach_ID=Input['Coach_ID']
    Course=Input['Course']
    Member_ID=Input['Member_ID']
    print(Gym_Name,Coach_ID,Course,Member_ID)
    return GYMJoinUs.JoinUs(Gym_Name,Coach_ID,Course,Member_ID)

@app.route('/Post/SignUp',methods=['POST'])
def SignUp():
    Input = request.get_json()
    Name=Input['Name']
    Phone_Number=Input['Phone_Number']
    Email=Input['Email']
    Gender=Input['Gender']
    Birthday=Input['Birthday']
    Password=Input['Password']

    return GYMSignUp.SignUp(Name, Phone_Number, Email, Gender, Birthday, Password)

@app.route('/Post/PostUpload',methods=['POST'])
def PostUpload():
    Input = request.get_json()
    Post_Title=Input['Post_Title']
    Post_Content=Input['Post_Content']
    Member_ID=Input['Member_ID']
    return GYMPostUpload.UploadPost(Post_Title,Post_Content,Member_ID)

@app.route('/Get/MyPlanDatas',methods=['POST'])
def MyPlanDatas():
    Input = request.get_json()
    Member_ID=Input['Member_ID']
    return GetMyPlans.GetMyPlan(Member_ID)

@app.route('/Get/SignIn',methods=['POST'])
def SignIn():
    Input = request.get_json()
    Email=Input['Email']
    Password=Input['Password']
    return GYMSignIn.SignIn(Email,Password)

@app.route('/Get/BranchDatas',methods=['GET'])
def BranchDatas():
    CheckToday()
    return open('Datas/Branch.json', 'r')

@app.route('/Get/CoachDatas',methods=['GET'])
def CoachDatas():
    CheckToday()
    return open('Datas/Coach.json', 'r')

@app.route('/Get/CourseDatas',methods=['GET'])
def CourseDatas():
    CheckToday()
    return open('Datas/Course.json', 'r')

@app.route('/Get/PostDatas',methods=['GET'])
def PostDatas():
    CheckToday()
    return open('Datas/Post.json', 'r')


if __name__ == "__main__":
    app.run(port=1013, debug=True)
