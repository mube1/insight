
import cohere
co = cohere.Client('') # This is your trial API key

class Story:
    
    """ This is a story generator class
       context_generator generates a context
       read_background reads users background from previous interactions

    """
    
    
    def __init__(self,user_input) -> None:
        self.user_input=user_input
        self.prompt='Tell me a story about a person who '
    
    background=None
    context=None
    
    def context_generator():
        pass

    def read_background():
        pass
    
    def prompt_generator(self,prompt):
        self.prompt=prompt
    
    def response(self):
        response = co.generate(
        model='command-xlarge-20221108',
        prompt=self.prompt+self.user_input,
        max_tokens=300,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=[],
        return_likelihoods='NONE')
        return response.generations[0].text

# print('Prediction: {}'.format(response.generations[0].text))
