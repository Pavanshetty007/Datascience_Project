# -*- coding: utf-8 -*-


from tkinter import *
from firebase import firebase
firebase = firebase.FirebaseApplication('https://final-year-project-66644-default-rtdb.firebaseio.com', None)


def store(disease,mail):
    from datetime import date
    today = date.today()
    mail=str(mail).split(".")[0]
    import random
    n = random.randint(1000,5000) 
    print(n)
    firebase.put(str(mail),str(today)+"/result/"+str(n),disease)
    print("data stored")
    root = Tk()
    root.title("data stored")
    root.geometry("350x50")
    w = Label(root, text ='Scan Refrence number: '+str(n), font = "20",fg="red") 
    w.pack()
    root.mainloop()
    
    
    
def main(disease,mail):
    ws = Tk()
    ws.title('Hospital Suggestion')
    ws.geometry('700x400')
    ws.config(bg='#F2B90C')
    
    def display_selected(choice):
        choice = variable.get()
        t.delete('0.0', END)
        print(choice)
        if choice == "Bangalore":
            fact="""Apollo Hospital\nHospital Address:\n154/11, Bannerghatta Main Road,Bangalore 560076 India
\nFortis Hospital\nHospital Address:\n154/9, Bannerghatta Road, Opposite IIM-B Bangalore 560076 India
\nManipal Hospital\nHospital Address:\nOld Airport road Bangalore 560071 India"""
            t.insert(END, fact)
        if choice == "Mysore":
            fact="""Apollo Hospital\nHospital Address:\n154/11, Bannerghatta Main Road,Bangalore 560076 India
\nFortis Hospital\nHospital Address:\n154/9, Bannerghatta Road, Opposite IIM-B Bangalore 560076 India
\nManipal Hospital\nHospital Address:\nOld Airport road Bangalore 560071 India"""
            t.insert(END, fact)
        if choice == "Coorg":
            fact="""Apollo Hospital\nHospital Address:\n154/11, Bannerghatta Main Road,Bangalore 560076 India
\nFortis Hospital\nHospital Address:\n154/9, Bannerghatta Road, Opposite IIM-B Bangalore 560076 India
\nManipal Hospital\nHospital Address:\nOld Airport road Bangalore 560071 India"""
            t.insert(END, fact)
        if choice == "Belgaum":
            fact="""Apollo Hospital\nHospital Address:\n154/11, Bannerghatta Main Road,Bangalore 560076 India
\nFortis Hospital\nHospital Address:\n154/9, Bannerghatta Road, Opposite IIM-B Bangalore 560076 India
\nManipal Hospital\nHospital Address:\nOld Airport road Bangalore 560071 India"""
            t.insert(END, fact)
        if choice == "Chennai":
            fact="""Dr. Kodeeswaran Clinic - Neurosurgeon, Spine Surgeon, Brain Surgeon and Neurologist, Best Neurosurgeon 
            \nApollo Hospital\nHospital Address:\nOld Building, Boston Brain And Spine Care. 80A/129AE, 4th Ave,
            opposite to Sundaram Medical Foundation, Shanthi Colony, Anna Nagar, Chennai, Tamil Nadu 600040\nMobile no:  091506 33311
\nDr.Shyam Sundar\nHospital Address:\nNew No. 10, Old no 11, Parameswari Nagar, 3rd Street, Adyar, Chennai, Tamil Nadu 600020\nMobile no:  099620 72279
\nDr. M. Balamurugan - Best Neurosurgeon\nHospital Address:\n42, CIT 1st Main Rd\nPhone No: 044 4915 1111
\nChennai Neuroscience Foundation\nHospital Address:\nNo. 1051, Poonamallee High Rd\nMobile No • 096000 48121
\nApollo Proton Cancer Centre\nHospital Address:\n4/661, Dr Vikram Sarabai Instronic Estate 7th St • In Dr. VSI Estate\nMobile No • 073389 9222
\nNeuro Hospital\nHospital Address:\nNo 25 Rukmani Lakshmipathi Salai, Egmore\nPhone No:044 2855 3901
\nCancer Healer Centre\nHospital Address:\nAJ Arcade, Old No. 306 New, No.30, Valluvar Kottam High Rd, opp. Sangeetha Hotel Nungabakkam\nPhone no:044 4859 7272"""
            t.insert(END, fact)
        if choice == "Hyderabad":
            fact="""Dr Vijay Anand Reddy - Cancer Specialist | Best Oncologist \nApollo Hospitals\nHospital Address:\nDirector office Ground Floor, Apollo Cancer Hospital, Apollo Health City\nPhone No: 040 2355 6357
\nDr.Vinodh Maddireddy\nHospital Address:\nMEDICOVER CANCER INSTITUTE, opposite CYBER GATEWAY, beside Ibis hotel\nPhone No: 070323 13999
\nDr. B.S.V.Raju\nAster Prime Hospitals\nHospital Address:\Plot No: 2, Meghamala Apartment road\nPhone No: 040 4959 4959
\nAmerican Oncology Institute\nHospital Address:\nHyderabad Cancer treatment center,Nalagandla, Telangana\nPhone No:1800 208 2000
\nCancer treatment center\nHospital Address: \nMor Chambers, 5-9-30/13-15A, 1st floor\nPhone No: 099665 72757
\nDr.Kalyan Bommakanti\nGlobal Gleneagles Hospital\nPhone No:085200 03683"""
            t.insert(END, fact)
        if choice == "Mumbai":
            fact="""Dr. Rahul T. Chakor\nB. Y. L. Nair Hospital\nHospital Address:\nXRFF+F3P, B. Y. L. Nair Hospital, Mumbai Central, Mumbai, Maharashtra 400008\nPhone:9820747496
\nDr. Sunanda Anand\nHospital Address:\nSuresh Colony Building-3, Suresh Colony, 3, SV Rd, LIC Colony, Suresh Colony, Vile Parle West, Mumbai, Maharashtra 400056\nPhone: 022 2626 7500
\nGlobal Hospital, Parel\nHospital Address:\n35, Dr Ernest Borges Rd, opp. Shirodkar High School, Parel East, Parel, Mumbai, Maharashtra 400012\nPhone: 022 676 70101
\nKohinoor Hospital\nHospital Address:\nKirol Rd, off Lal Bahadur Shastri Road, Ali Yavar Jung, Kurla West, Kurla, Mumbai, Maharashtra 400070\nPhone: 022 6755 6755"""
            t.insert(END, fact)
        if choice == "Pune":
            fact="""Dr. Nilesh M. Bhandari (Neurologist)\nHospital Address:\nBHANDARI SPECIALITY CLINIC, Dandekar Pool Signal, 104 : Vrundavan Apartments, Near Golden Wheel Hotel , Indian Oil Petrol Pump Lane, Navi Peth, Off, Pune, Maharashtra 411030\nPhone: 097645 55565
\nDr. Rajas Deshpande\nHospital Address:\n#1206/4B, Durga Shankar, Near Shubham Hotel, Off, Jangali Maharaj Rd, Pune, Maharashtra 411004\nPhone: 98812 38031
\nDr. BHUSHAN JOSHI\nHospital Address:\nApollo Clinic Viman Nagar Pune, Nyati Millenium Premises Cooperative Society Limited, Shop No.S1 & Stilt Floor,, Building "c" Viman Nagar,, Pune, Maharashtra 411014\nPhone: 08071 266 266
\nSahyadri Specialty Hospital\nHospital Address:\nPlot No. 30-C, Erandvane, Karve Rd, Deccan Gymkhana, Pune, Maharashtra 411004\nPhone: 88888 22222
\nAditya Birla Memorial Hospital\nHospital Address:\nAddress:  Aditya Birla Hospital Marg, Thergaon, Pimpri-Chinchwad, Maharashtra 411033\nPhone: 020 3071 7500"""
            t.insert(END, fact)
        if choice == "kolar":
            fact="""Child Neurologist: Dr C P Ravi Kumar\nHospital Address:\nLeelavathi Childrens Hospital, Neeli Krishnappa Rd, Doddapet, Kolar, Karnataka 563101
\nManipal Hospitals Information Centre\nHospital Address:\nBharani Health Centre Opp. IMA Building, Near Microwave Station Bangarpet, Road, Kolar, Karnataka 563101\nPhone: 098450 05876
\nVamshodaya Hospital\nHospital Address:\n4th cross, Antharagange Main Rd, near Kuvempu Park, Kuvempu Nagara, Kolar, Karnataka 563101\nPhone: 072770 72770"""
            t.insert(END, fact)
        if choice == "Mangaluru":
            fact="""Dr Madhukar Nayak, Neuro and Spine Clinic\nHospital Address:\n209, Marian Paradise Avenue, Bikaranakatte Road, Near Nanthoor Circle, Mangaluru, Karnataka 575005\nPhone:095351 52345
\nDr.Muralidhar Pai\nHospital Address:\nKMC Hospital Mangaluru, Balmatta Rd, Near Jyoti Circle, Hampankatta, Mangaluru, Karnataka 575001
\nDr. Arjun Shetty\nHospital Address:\nRoom no.00029, 2nd floor,KMC Hospital Dr.B R Ambedkar Circle, Mangaluru, Karnataka 575001\nPhone: 1800 102 4647
\nDr. Muralidhar Pai\nHospital Address:\nRoom no.00028, 2nd floor,KMC Hospital Dr.B R Ambedkar Circle, Mangaluru, Karnataka 575001\nPhone: 1800 102 4647
\nDr. Mayur Kamath V\nHospital Address:\nRoom no.00030, 2nd floor,KMC Hospital Dr.B R Ambedkar Circle, Mangaluru, Karnataka 575001\nPhone: 1800 102 4647"""
            t.insert(END, fact)
        if choice == "hubli":
            fact="""Dr Suresh M Dugani\nHospital Address:\n84QQ+MX8, SHIVAKRUPA HOSPITAL AMBEDAKAR CIRCLE Lamington Road, Hubli, Karnataka 580020\nPhone: 0836 235 3133
\nDr. Aniruddh Kulkarni\nNeuroWorld\nHospital Address:\nSri Krishna kalyan Mantap, 1# Main, Road, Deshpande Nagar, Hubli, Karnataka 580029\nPhone: 078992 54790
\nDr Vijaymahantesh Pujari\nNara Vijnana Clinic\nHospital Address:\nNear, Giriraj Annexe Building, T B Road, Court Circle, Hubli, Karnataka 580029\nPhone: 0836 295 6622
\nBalaji Institute of Neuro Sciences & Trauma\nHosur Unkal Road, Vidya Nagar, Behind Hosur KSRTC Depot, Hubli, Karnataka 580021\nPhone: 0836 237 4444"""
            t.insert(END, fact)
        if choice == "Other":
            fact="Doing a Google search"
            t.insert(END, fact)
            import webbrowser
            webbrowser.open('https://www.google.co.uk/search?q='+disease+" tumor hospitals near me")
    label1 = Label(ws, text='Hospital Suggestion for Brain tumor ',font=("Arial", 20),fg="blue",bg='#F2B90C')
    label1.pack()
    countries = ['Choose City','Bangalore','Mysore', 'Coorg','Belgaum','Chennai','Hyderabad','Mumbai','Pune','kolar','Mangaluru','hubli','Other']
    
    # setting variable for Integers
    variable = StringVar()
    variable.set(countries[0])
    
    # creating widget
    dropdown = OptionMenu(
        ws,
        variable,
        *countries,
        command=display_selected
    )
    
    # positioning widget
    dropdown.place(x=250,y=70)
    # Create text widget and specify size.
    t = Text(ws, height = 10, width = 50)
    t.place(x=50,y=150)
    
    # infinite loop 
    ws.mainloop()
#store("brain","kannihya12@gmail.com")