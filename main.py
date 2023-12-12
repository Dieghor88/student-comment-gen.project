#INFO
comment_version = ["a", "b", "c"]
age_check = ["yes", "no"]

#PROVIDING THE STUDENT NAME
name = input("What´s the student´s name? \n")

#PROVIDING THE STUDENT´S SCORE
while True:
  score = int(input("What´s the student´s score? \n"))
  if score > 100 or score < 0:
    print(f"Invalid option. Please choose a score between 0 and 100.")
  else:
    break

#PROVIDING STUDENT´S AGE
while True:
  minor = input("Is the student under 18?\n").lower()
  if minor not in age_check:
    print(f"Invalid option. Please choose Yes or No.")
  else:
    break
  
#PROVIDING COMMENT VERSION
while True:
  version = input("Choose a comment version: a/b/c \n").lower()
  if version not in comment_version:
    print(f"Invalid option. Please choose a, b or c.")
  else:
    break

#COMMENTS A/B/C FOR SCORES 90+ (PT-BR for minors)
if minor == "yes" and version == "a" and score >= 90 and score <= 100:
  comment = f"Hello {name}!\n\nGostaria de te desejar meus parabéns pela sua nota de {score}! Você está sempre presente e demonstra interesse em aula. Sua dedicação e atencão em sala são exemplares e tenho certeza que suas notas serão sempre igualmente grandiosas! Great job!\n\nTeacher Diego"
elif minor == "yes" and version == "b" and score >= 90 and score <= 100:
  comment = f"Hey {name}!\n\nMeus parabéns pela sua nota {score}! Você tem demonstrado interesse, dedicação e atenção. Também fico muito feliz em ver como você se dá bem com os outros alunos e tenho certeza que você vai continuar sendo exemplar além de sempre conseguir ótimas notas!\n\nTeacher Diego"
elif minor == "yes" and version == "c" and score >= 90 and score <= 100:
  comment = f"Hi {name}!\n\nQuero te desejar meus parabéns pela sua nota de {score}! Sua dedicação, presença e interesse são exemplares. Seu comprometimento com as aulas é prova de que você se esforça e eu estou certo de que suas notas continuarão sendo excelentes ao longo de sua jornada no inglês!\n\nTeacher Diego"

#COMMENTS A/B/C FOR SCORES 80-90 (PT-BR for minors)
if minor == "yes" and version == "a" and (score >= 80 and score < 90):
  comment = f"Hello {name}!\n\nGostei muito de ver como você está se dedicando em sala. Você faz as tarefas, os exercícios em aula e vejo também como você mostra interesse genuíno em aprender. Sua nota de {score} foi boa, mas tenho certeza que com a sua dedicação e talvez algumas visitas ao English Club suas notas vão só aumentar. Continue assim, você está de parabéns!\n\nTeacher Diego"
elif minor == "yes" and version == "b" and (score >= 80 and score < 90):
  comment = f"Hey {name}!\n\nMeus parabéns pela sua nota de {score}! Suas notas no teste oral foram exemplares e sua nota na prova escrita também foi boa. Sei que a prova escrita pode ser um pouco mais difícil, mas tenho certeza que com a sua dedicação e interesse, suas notas podem e serão ainda maiores!\n\nTeacher Diego"
elif minor == "yes" and version == "c" and (score >= 80 and score < 90):
  comment = f"Hello {name}!\n\nFiquei muito feliz ao ver o seu empenho em sala de aula. Você se destaca quando faz as tarefas, participa das atividades em aula e demonstra um verdadeiro interesse pelo aprendizado. Sua nota de {score} foi boa, mas tenho certeza de que, com sua dedicação contínua e talvez algumas participações no English Club, suas notas vão continuar subindo. Continue assim, você está no caminho certo!\n\nTeacher Diego"

#COMMENTS A/B/C FOR SCORES 70-80 (PT-BR for minors)
if minor == "yes" and version == "a" and (score >= 70 and score < 80):
  comment = f"Hello {name}!\n\nSua nota de {score} foi satisfatória mas sinto pelo seu potencial que poderia ter sido melhor. Você precisa prestar um pouco mais de atenção nas aulas e nos exercícios, além das tarefas. Sinto que em sala com um pouco mais de esforço para falar em inglês e evitando distrações, você poder conseguir notas melhores. Se possível venha aos English Clubs nas sextas feiras. Assim, tenho certeza que suas notas serão sempre exemplares!\n\nTeacher Diego"
elif minor == "yes" and version == "b" and (score >= 70 and score < 80):
  comment = f"Hey {name}!\n\nSua nota de {score} foi boa mas abaixo da média da escola que é de 80. Nossas provas podem ser um pouco difícil por conta do conteúdo de duas unidades mas sei que você demonstra interesse e dedicação nas aulas, além de participar e se esforçar. Continue se dedicando assim e se possível venha aos English Clubs nas sextas-feiras para exercícios de revisão. Tenho certeza que dessa forma, suas notas no curso serão sempre muito boas.\n\nTeacher Diego"
elif minor == "yes" and version == "c" and (score >= 70 and score < 80):
  comment = f"Hello {name}!\n\nSua nota de {score} foi boa, porém ficou abaixo da média 80 da escola. Sei que as vezes o conteúdo das aulas e as provas podem ser desafiadoras, mas mas sei que com o seu interesse e um pouco de dedicação e participação extras nas aulas, você pode conseguir notas melhores. Se possível, participe dos English Clubs nas sextas-feiras para revisar o conteúdo. Tenho certeza de que assim, suas notas no curso serão sempre excelentes.\n\nTeacher Diego"

#COMMENTS A/B/C FOR SCORES 90+ (US-ENG for adults)
if minor == "no" and version == "a" and score >= 90 and score <= 100:
  comment = f"Hello {name}!\n\nI would like to congratulate you on your score of {score}! You are always present and show interest in class. Your dedication and attention in the classroom are exemplary, and I'm sure your grades will always be just as good or even better! Great job!\n\nTeacher Diego"
elif minor == "no" and version == "b" and score >= 90 and score <= 100:
  comment = f"Hey {name}!\n\nCongratulations on your score of {score}! You have shown interest in class and a lot of dedication. I am also happy to say that your participation in class was very productive. I am sure that you will continue to be a great student and always get great grades!\n\nTeacher Diego"
elif minor == "no" and version == "c" and score >= 90 and score <= 100:
  comment = f"Hi {name}!\n\nI want to say congratulations you on your score of {score}! Your dedication, focus, and interest are an exemple to everybody. In class you are committed and hardworking, and I am certain that your grades will continue to be excellent throughout your journey in English!\n\nTeacher Diego"

#COMMENTS A/B/C FOR SCORES 80-90 (US-ENG for adults)
if minor == "no" and version == "a" and (score >= 80 and score < 90):
  comment = f"Hello {name}!\n\nGostei muito de ver como você está se dedicando em sala. Você faz as tarefas, os exercícios em aula e vejo também como você mostra interesse genuíno em aprender. Sua nota de {score} foi boa, mas tenho certeza que com a sua dedicação e talvez algumas visitas ao English Club suas notas vão só aumentar. Continue assim, você está de parabéns!\n\nTeacher Diego"
elif minor == "no" and version == "b" and (score >= 80 and score < 90):
  comment = f"Hey {name}!\n\nCongratulations on your score of {score}! Your grades on the tests were great, and your performance in class was also good. I know the written test can be a bit more challenging, but I'm sure that with just a little bit more dedication and practice, your grades can and will be even higher!\n\nTeacher Diego"
elif minor == "no" and version == "c" and (score >= 80 and score < 90):
  comment = f"Hi {name}!\n\nI was very happy to see your dedication in the classroom. You did the exercises, participated in class activities, and showed a genuine interest in learning English. Your score of {score} was great, but I'm sure that with your continued dedication and maybe some extra practice, your grades will keep going up. Keep up the great job!\n\nTeacher Diego"

#COMMENTS A/B/C FOR SCORES 70-80 (US-ENG for adults)
if minor == "no" and version == "a" and (score >= 70 and score < 80):
  comment = f"Hello {name}!\n\nYour score of {score} was good, but I feel that considering your potential, it could have been better. You need to pay a bit more attention in class, during exercises, and with your homework. I believe that if you try a little harder to pay attention, to speak in English and to avoid distractions in class, you can get better grades. And if possible, please come to the English Clubs on Fridays. This way, I'm sure your grades will always be great!\n\nTeacher Diego"
elif minor == "no" and version == "b" and (score >= 70 and score < 80):
  comment = f"Hey {name}!\n\nYour score of {score} was good, but it's below the school average, which is 80. Our tests can be a bit challenging maybe because of the content from two units, but I know you show interest and dedication in class and you can be participative too. Try a bit harder in class, and if possible, come to the English Clubs on Fridays for review exercises. I'm sure that this way, your grades will always be very good.\n\nTeacher Diego"
elif minor == "no" and version == "c" and (score >= 70 and score < 80):
  comment = f"Hello {name}!\n\nYour score of {score} was good, but it is below the school's average of 80. I understand that sometimes what we see in class and tests can be challenging, but I know that with your interest and a little extra dedication and participation in class, you can get better grades. If possible, com to the English Clubs on Fridays to review the content. I'm sure that this way, your grades in will always be excellent.\n\nTeacher Diego"

#PRINTING THE COMMENT
if minor == "yes" and (score >= 90 and score <= 100):
  if version == "a":
    print(comment)
  elif version == "b":
    print(comment)
  else:
    print(comment)

if minor == "yes" and (score > 80 and score < 90):
  if version == "a":
    print(comment)
  elif version == "b":
    print(comment)
  else:
    print(comment)

if minor == "yes" and (score > 70 and score < 80):
  if version == "a":
    print(comment)
  elif version == "b":
    print(comment)
  else:
    print(comment)

if minor == "no" and (score >= 90 and score <= 100):
  if version == "a":
    print(comment)
  elif version == "b":
    print(comment)
  else:
    print(comment)

if minor == "no" and (score > 80 and score < 90):
  if version == "a":
    print(comment)
  elif version == "b":
    print(comment)
  else:
    print(comment)

if minor == "no" and (score > 70 and score < 80):
  if version == "a":
    print(comment)
  elif version == "b":
    print(comment)
  else:
    print(comment) 
