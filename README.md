# insight


There are still blind spots in how we understnad ourselves that we can't be sure of, even with deeper introspection. It’s like the saying goes, “nothing from the mind can save you from the mind”. We need others too to understand better ourselves. This idea has also been suggested by the psychologist [Tasha Eurich](https://tashaeurich.com/) in her book ‘Insight’, hence the name of the project.
On the other hand, guessing the outcomes of the different decisions we made in our life is almost a super power.

The main idea of this project is to be able to address the above two issues: getting insight about ourselves and anticipating the decisions we make in our life.



### System outline ###

The system is a web app made out of at least four components:

Component  | Task
------------- | -------------
Front end | Get input text, display output
Understanding engine | Process the user input to classify personality
Context | Generate random or saved context about the state of the person
Generate history | Generate story based on context and personality
<br>

![outline](https://github.com/mube1/insight/blob/main/cohere.png)

### Dataset ###
Data scrapped from [enneagram institute](https://www.enneagraminstitute.com/type-5) is used to train the model to classify people into their personalities.

### Demo ###
![Demo](https://github.com/mube1/insight/blob/main/cohere.gif)
