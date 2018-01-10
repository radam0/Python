

#Nikhil Vemula
#cs61002
#March 29,2016

import os #importing required library files
from inspect import getsourcefile
import random

currdir = os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))

class VocabularyQuiz():  #
    def __init__(self,*args):
	self.mainfunction()
	
    def mainfunction(self,*args):
        self.voc_files_path = 'vocabulary/'
        ExistingFiles = os.listdir(self.voc_files_path)
        total_voc_files = []
        for eachfile in ExistingFiles:
            if eachfile.endswith('.txt'):
                total_voc_files.append(eachfile)

        if total_voc_files==[]:  #Checking for avaiabiltity of vocabulary files in the directory
            print 'No vocabulary files found in the directory...\n'
            return

        for i in range(0,len(total_voc_files)): # Printing available files
            print str(i+1)+') '+total_voc_files[i]

        wronganswers = []
        given_input = input('Please select one vocabulary file from the list above : ') # taking vocabulary file name from the user as input
        if given_input>0 and given_input<(len(total_voc_files)+1):
            given_input = given_input-1
            getcurrentdict = self.getdict(total_voc_files[given_input])
            quiz_len = input('How many words you like for the quiz: (1-'+str(len(getcurrentdict.keys()))+') : ') # Prompt the user for the number of words to be quized on
            if quiz_len>len(getcurrentdict.keys()) or quiz_len<=0: # Error check to make sure the number is valid.
                print 'Given number is not in between given range'
                return
            randnumbers = [] # Quiz the user by using a randomly generated list of English words from the dictionary
            while len(randnumbers)!=quiz_len:
                num = random.randint(0,len(getcurrentdict.keys())-1)
                if num not in randnumbers:
                    randnumbers.append(num)

            for i in range(0,quiz_len):
                print '\n\nQuestion: Enter opposite word for '+getcurrentdict.keys()[randnumbers[i]]
                answer = raw_input('Answer: ')
                if answer==getcurrentdict.values()[randnumbers[i]]:
                    print 'Right Answer'
                else:
                    wronganswers.append(getcurrentdict.keys()[randnumbers[i]])
                    print 'Wrong Answer'

            if wronganswers!=[]: 
                print '\n\n'+str(len(wronganswers))+' answer(s) given wrong. Missed questions are exported to below path\n'+os.path.join(currdir,'wrongAnswers.txt')
            else:
                print '\n\n All answers are correct...!'

            self.exporterrors('wrongAnswers.txt',wronganswers) #All the errors are exported to this file
                
        else:
            print 'Given number is not in the above list.'
        
        

    def getdict(self,filename):
        finalFilePath = os.path.join(self.voc_files_path,filename)
        fid = open(finalFilePath,'r')
        lines = fid.readlines()
        fid.close()

        voc_dict = {}
        for eachline in lines:
            eachline = eachline.replace('\n','').replace('\r','')
            splits = eachline.split(':')
            if len(splits)>1:
                voc_dict[splits[0]]=splits[1]

        return voc_dict

    def exporterrors(self,filename,directory):
        fid = open(os.path.join(currdir,filename),'w')
        for eachwrong in directory:
            fid.write('Missed question, '+eachwrong+'\r\n')
        fid.close()
        
        


if __name__ == '__main__':
    cls = VocabularyQuiz()
