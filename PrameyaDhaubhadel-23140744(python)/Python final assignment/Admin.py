from Doctor import Doctor
from Patient import Patient


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        self.__admin_username = username
        self.__admin_password = password
        self.__admin_address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if(self.__admin_username == username) & (self.__admin_password == password):
            return True
        else:
            print("Invalid username and password.")

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        
        doc_fname = input("Enter the doctor's first name: ")
        doc_sname = input("Enter the doctor's surname: ")
        doc_spec = input("Enter the doctor's speciality: ")

        return doc_fname,doc_sname,doc_spec

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

       
        op = input("Please choose the operation: ")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print("Enter the doctor's details:")
            # doc = self.get_doctor_details()
            doc_fname, doc_sname, doc_spec = self.get_doctor_details()
            # check if the name is already registered
            name_exists = False
            for a in doctors:
                if(doc_fname==a.get_first_name() and doc_sname==a.get_surname()):
                     print("Name already exists.")
                     break
            else:
                
                doctors.append(Doctor(doc_fname,doc_sname,doc_spec))
                print('Doctor registered.')
                
                   

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input("Enter the Doctor's ID: ")) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('Incorrect ID')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            i_op = int(input('Input: ')) # make the user input lowercase
            if(i_op == 1):
                new_firstname = input("Enter the new first name : ")
                doctors[index].set_first_name(new_firstname)
                print("Doctor's first name is updated.")
               
            elif(i_op == 2):
                new_surname = input("Enter the new surname : ")
                doctors[index].set_surname(new_surname)
                print("Doctor's surname is updated.")
               
            elif(i_op == 3):
                new_spec = input("Enter the new speciality : ")
                doctors[index].set_speciality(new_spec)
                print("Doctor's speciality is updated.")
               

            


        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            index = int(input("Enter the Doctor's ID to be deleted: "))-1
            doctor_index=self.find_index(index,doctors)
            if(doctor_index!=False):
                doctors.pop(index)
                print("Doctor deleted")
                

            else:
                print("The Id you have entered is not found.")

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input("Please enter the patient's ID:")

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('Incorrect Patient ID')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits mentioned symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input("Please enter the Doctor's ID: ")

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name()) 
                self.view(patients)
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                print('The patient assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The entered Id was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('Incorrect ID')

    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
       
        # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view_patient(patients)
        y_no = input("Do you want to discharge a patient (Y/N): ")
        if(y_no == 'y' or 'Y'):
             print("-----Discharge Patient-----")
             p_id = int(input("Please Enter the patient ID: "))-1
             if p_id  in range(len(patients)):
                discharge_patients.append(patients.pop(p_id))
                print("----------Sucessfully Deleted------------")
                self.view_patient(patients)
             else:
                print("Invalid patient ID.")
        else:
            print("Thank you, Done with Discharge.")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def admin_details(self):
        print(f"Username : {self.__admin_username}")
        print(f"Password : {self.__admin_password}")
        print(f"Address : {self.__admin_address}")

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        option = int(input('Choised field: '))

        if option == 1:
            self.admin_details()
            username1 = input('Enter the new username: ')
            # validate the username
            username2 = input('Enter the new username again: ')
            if(username1 == username2):
                print("Username matched.")
                self.__admin_username = username2
                print("------------------------------")
                self.admin_details()
                print("-----------Username sucessfully updated--------------")
            else:
                print("Username not matched")   


        elif option == 2:
            self.admin_details()
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__admin_password = password
                self.admin_details()
                print("----------------Password sucessfully updated---------------")

        elif option == 3:
            self.admin_details()
            address = input('Enter the new address: ')
            # validate the address
            if address == input('Enter the new address again: '):
                self.__admin_address = address
                self.admin_details()
                print("---------------address sucessfully updated-----------------")

        else:
            print("Invalid Choice.")


admin = Admin('prameya','123','Bhaktapur') # username is 'admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
discharged_patients = []


#admin.get_doctor_details()
# admin.view(doctors)
# admin.doctor_management(doctors)
# admin.view_patient(patients)
# admin.assign_doctor_to_patient(patients,doctors)
# admin.discharge(patients, discharged_patients)
# admin.update_details()