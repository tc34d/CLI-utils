from time import time

# calculate the accuracy of input prompt
def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] != words[i]:
                continue
            else:
                errors +=1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# calculate the speed in words per minute
def typingSpeed(iprompt, stime, etime):
    global time
    global iwords

    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time

    return speed

# calculate total time elapsed
def timeElapsed(stime, etime):
    time = etime - stime

    return time

if __name__ == '__main__':
    print("note: the words per minute thing can be inaccurate")
    level = input('choose your difficulty\n easy\n medium\n hard ')

    if level == "easy":
         prompt = "Closed captions were created for deaf or hard of hearing individuals to assist in comprehension.\n They can also be used as a tool by those learning to read, learning to speak a non-native language, or\n in an environment where the audio is difficult\n to hear or is intentionally muted."
         print("Prompt: " + prompt)
         input("press enter when you are ready")

         stime = time()
         iprompt = input()
         etime = time()

         # gather all the information returned from functions
         time = round(timeElapsed(stime, etime), 2)
         speed = typingSpeed(iprompt, stime, etime) * 60
         errors = typingErrors(prompt)

         # printing all the required data
         print("Total Time elapsed : ", time, "s")
         print("Your Average Typing Speed was : ", speed, "words / minute")
         print("With a total of : ", errors, "errors")
         input("to restart, press enter")
         quit()

    if level == 'medium':
        prompt = "Proofreader applicants are tested primarily on their spelling, speed, and skill in finding errors in\n the sample text. Toward that end, they may be given a list of ten or twenty classically difficult\n words and a proofreading test, both tightly timed. The proofreading test will often have\n a maximum number of errors per quantity of text and a minimum amount of time to find them. The goal of\n this approach is to identify those with the best skill set."
        print("Prompt: " + prompt)
        input("press enter when you are ready")

        stime = time()
        iprompt = input()
        etime = time()

        # gather all the information returned from functions
        time = round(timeElapsed(stime, etime), 2)
        speed = typingSpeed(iprompt, stime, etime) * 60
        errors = typingErrors(prompt)

        # printing all the required data
        print("Total Time elapsed : ", time, "s")
        print("Your Average Typing Speed was : ", speed, "words / minute")
        print("With a total of : ", errors, "errors")
        input("to restart, press enter")
        quit()

    if level == 'hard':
        prompt = "Engineers, as practitioners of engineering, are people who invent, design, analyze, build, and test\n machines, systems, structures and materials to fulfill objectives and requirements while considering the limitations imposed by practicality,\n regulation, safety, and cost. The work of engineers forms the link between scientific discoveries and their subsequent applications to human and business\n needs and quality of life."
    else:
      print("please select a difficulty. restart application by pressing enter.\n then select a difficulty")
      input()
      quit()

    print("Prompt: " + prompt)
    input("press enter when you are ready")



    stime = time()
    iprompt = input()
    etime = time()



    # gather all the information returned from functions
    time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime) * 60
    errors = typingErrors(prompt)

    # printing all the required data
    print("Total Time elapsed : ", time, "s")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", errors, "errors")
    input("to restart, press enter")
    quit()
