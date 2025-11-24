import heapq

patients = []


def add():
   print("\n add new patient \n")
   nm = input(" name = ")
   sev = input(" severity(1-10) = ")

   try:
      sev = int(sev)
   except:
      print(" please enter number only \n")
      return

   heapq.heappush(patients , (-sev , nm))
   print("\n patient added ok \n")



def serve():
   if len(patients)==0:
      print("\n no patient in queue \n")
      return

   s , n = heapq.heappop(patients)
   print("\n patient now: ", n , "  severity:", -s , "\n")



def show():
   if len(patients)==0:
      print("\n queue empty \n")
      return

   print("\n all patients in queue : \n")
   for s , n in patients:
       print("  ", n , "  sev=", -s)
   print()



def menu():

   print("\n hospital patient queue system  ")
   print(" manage patients by severity \n")

   while True:

      print("1 add patient")
      print("2 serve next")
      print("3 show queue")
      print("4 exit \n")

      ch = input(" enter choice : ")

      if ch == "1":
         add()
      elif ch == "2":
         serve()
      elif ch == "3":
         show()
      elif ch == "4":
         print("\n bye \n")
         break
      else:
         print("\n wrong choice try again\n")



menu()
