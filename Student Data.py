import mysql.connector 

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "list"
)

Stud_list=["AAKANSHA SHARMA","AAQUIB MULTANI","AASHI JAIN","AGAM JAIN","AKHILESH GUPTA",
"AMAN ARYA",
"AMIT SINGH",
"AMOL PANDEY",
"ANJALI PATIDAR",
"ANKITA MAHAWAR",
"ARNAV YADAV",
"DEV PATIDAR",
"ESHA SHROFF",
"FAIZAN KHAN",
"GANDHARVA SINGH CHOUHAN",
"GANPAT HADA",
"GARIMA MORE",
"GITALI BHAWSAR",
"GOURAV PRAJAPAT",
"GREESHM RATHORE",
"HARSH PANDEY",
"HARSHITA VISHWAKARMA",
"HIMANSHI VYAS",
"HRITIK DANGI",
"ISHAAN PATHAK",
"ISHIKA UPADHYAY",
"JAYA PATIDAR",
"JAYESH CHHABRA" ,
"KUSHALRAJ GOLANE",
"LALIT YADAV",
"LOVELY KORI",
"MANIK CHAND PARADIYA",
"MANISH PATIDAR",
"MUSKAN MANAWARE",
"MUSTANSIR SAIFEE",
"NIKHIL KUMAR",
"PAYAL BAGGAD",
"PRABHAT MALVIYA",
"PURVA DUBE",
"RAHUL AJNAR",
"RAJNISH BHARGAV"
"RATNESH JAIPAL",
"SANSKAR YADAV",
"SATVINDER SINGH BHATIA",
"SHADAB ALI",
"SHRUTHI MOHAN",
"SHWETA SINGH",
"SIMRAN TALREJA", 
"SOMYA AGRAWAL" ,
"TANMAY SHARMA",
"TANU BANIYA",
"VIDUSHI CHAUBEY ",
"VIRENDRA MUKHI ",
"VISHAL HARSUDE"
]


pointer = connection.cursor()

num = 1
for alpha in Stud_list:
    pointer.execute("INSERT INTO list(roll_number,name) VALUES (%s,%s)",(num,alpha,))
    num += 1
    
connection.commit()

pointer.close()