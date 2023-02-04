import random
# from cProfile import label
from django.shortcuts import render
from django import forms


import cohere
from cohere.classify import Example



p=[
'REFORMER',
'HELPER',
'ACHIEVER',
'INDIVIDUALIST',
'INVESTIGATOR',
'LOYALIST',
'ENTHUSIAST',
'CHALLENGER',
'PEACEMAKER']

desc={0:'AVERAGE',1:'REFORMER',2:'HELPER',3:'ACHIEVER',4:'INDIVIDUALIST',5:'INVESTIGATOR',6:'LOYALIST',7:'ENTHUSIAST',8:'CHALLENGER',9:'PEACEMAKER'}

full_desc={0:'Average',
    1 : 'The Rational, Idealistic ,Principled, Purposeful, Self-Controlled, and Perfectionistic',
    2: 'The Caring, Interpersonal ,Demonstrative, Generous, People-Pleasing, and Possessive',
    3:'The Success-Oriented, Pragmatic,  Adaptive, Excelling, Driven, and Image-Conscious',
    4:'The Sensitive, Withdrawn  ,Expressive, Dramatic, Self-Absorbed, and Temperamental',
    5:'The Intense, Cerebral , Perceptive, Innovative, Secretive, and Isolated',
    6:'The Committed, Security-Oriented  Engaging, Responsible, Anxious, and Suspicious',
    8:'The Powerful, Dominating Self-Confident, Decisive, Willful, and Confrontational',
    7:'The Busy, Fun-Loving, Spontaneous, Versatile, Distractible, and Scattered',
    9:'The Easygoing, Self-Effacing , Receptive, Reassuring, Agreeable, and Complacent'
    }

boiler_plates=[]


carrers=['Agriculture',
 'natural',
 'resources',
 'Architecture',
 'Construction',
 'Business',
 'management,',
 'finance,',
 'administrationEducation',
 'health',
 'science',
 'Information',
 'technology',
 'law',
 'public',
 'safety,',
 'Science',
 'engineering']

status=['succeded', 'challenged', 'failed', 'got stuck' ]

get_carrer= lambda :carrers[random.randint(0,len(carrers)-1)]
get_status=lambda :status[random.randint(0,len(status)-1)]
get_personality=lambda :p[random.randint(0,len(p))]
def get_words(word ):
    word=word.replace('The ','')
    words=word.split(',')
    return words[0],words[-1]

def predict(user_text):

    p=[
    'REFORMER',
    'HELPER',
    'ACHIEVER',
    'INDIVIDUALIST',
    'INVESTIGATOR',
    'LOYALIST',
    'ENTHUSIAST',
    'CHALLENGER',
    'PEACEMAKER']
    desc={0:'AVERAGE',1:'REFORMER',2:'HELPER',3:'ACHIEVER',4:'INDIVIDUALIST',5:'INVESTIGATOR',6:'LOYALIST',7:'ENTHUSIAST',8:'CHALLENGER',9:'PEACEMAKER'}
    
    examples_=[]
    for i in range(1,10):
        file_name='en'+str(i)+'.txt'
        file=open(file_name)
        text=file.read()
        lines=text.split('\n')
        for j in lines:
            if len(j)<3:
                continue
            temp=j.split('.')
            for k in temp:
                k=k.strip()
                if len(k)<3:
                    continue
                examples_.append(Example(k,desc[i]))
    
    co = cohere.Client('') # This is your trial API key
    if examples_:
        # examples_=random.shuffle(examples_)
        response = co.classify( model='large',  inputs=[user_text],examples=examples_)
        return p.index(response.classifications[0].prediction)
    return random.randint(0 ,8)

def get_prompt(idx):
    base='write a story '
    questions=[
        #  base+get_words(full_desc[idx])[0]+' person who ' + get_status()+ ' in ' + get_carrer(),
        #  base+ get_words(full_desc[idx])[-1] + ' persons\' challenge against in ' + get_carrer() + ' career',
        base+ ' how a ' + get_words(full_desc[idx])[-1] + get_status() + ' in life. and ' + ' about the life of Jhon who is ' +  get_words(full_desc[idx])[0]+ ' but also ' +get_words(full_desc[idx])[0]  
        # person and his challenges in life'


        ]

    return questions[random.randint(0,len(questions)-1)]
    



# Create your views here.

class UserBackgroundFrom(forms.Form):
    story=forms.Textarea()


# def get_prompt():
#     return 'Tell a success story in third person about how a person in person who '
    # return 'How alternate story of the a success story in third person about how a person in person who '
def getstory(user_input):
    # prompt=''
    print(' Now in get story ')
    prompt = get_prompt(predict(user_input))
        # prompt+=user_input

    # print(prompt)
    response = co.generate(
        model='command-xlarge-20221108',
        prompt=prompt,
        max_tokens=300,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return response.generations[0].text



def result(request):
    story=''
    return render(request,"insight/result.html", {'story':story})


def index(request,story=''):
    posted=False
    if request.method == 'POST':
        form = UserBackgroundFrom(request.POST)
        if form.is_valid():
            
            story = form.cleaned_data.get('story')
            a=form.cleaned_data.get('about')
            
            if a is not None:
                story=a
            s=request.POST.get('about')
            print(' This is what we got ', s)
            story_generated=getstory(s)

            
            posted=True
            return render(request,"insight/index.html",
            {
                'form':UserBackgroundFrom(),
                'story':story_generated,
                'posted':posted
            })
        else:
            # messages.success(request, 'Your account have been created')
            return render(request,"insight/index.html",
            {
                'form':UserBackgroundFrom(),
                'story':story,
                'posted':posted
            })
    else:
        return render(request,"insight/index.html",
            {
                'form':UserBackgroundFrom(),
                'story':story,
                'posted':posted
            })
    # return render(request, 'users/register.html', {'form': form})


