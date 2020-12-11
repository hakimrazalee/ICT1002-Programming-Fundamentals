# Project Objective



Chatbots – computer programs that can respond to queries typed in natural language – have recently
become a popular addition to web sites and other interactive applications.

The aim of this project is to implement a simple chatbot that can respond to simple queries made up of
a single question word (called the intent) and an object (called the entity). The chatbot will be able to
answer questions such as Where is the printer? or What is C? by identifying the intent (where or what)
and entity (printer or C) then looking up the answer corresponding to this pair in a simple database.

The chatbot will also be able to learn new answers by asking questions of the user. If a user asks a
question for which the database does not contain an answer, the user will be given the option to supply
an answer that can be used to respond to the same question in future. (This simulates having the chatbot
refer the unknown question to a third party who does know the answer.)

# Detailed Requirements

Your team is required to implement, in C, a chatbot of the kind described in the introduction. The
chatbot will converse in the console using a command-line-like interface; no graphical UI is required.
On each iteration of the main loop of the program (implemented for you in the main function in the
skeleton code), the program will display a prompt and wait for the user to type a question or instruction.

Firstly, your chatbot should recognise some stock words and phrases to which it can give rote replies.

These phrases will be referred to as smalltalk in the remainder of this document. For example, the
chatbot may reply “hello” whenever the user types “hello” or “hi”. Your chatbot should have at least
five items of smalltalk.

Apart from smalltalk, the chatbot will understand only a very simplified form of English in which all
sentences are composed of only two parts, called the intent and the entity, in that order.
- The intent represents what the user wants to do or to know. It may be a verb instructing the
chatbot to do something, or a question word like what, where, etc.
- The entity is a noun phrase representing the object to which the instruction or question refers.

For example, the user might type in Where is SIT?, which consists of an intent “WHERE” and an entity
“SIT”. The chatbot might answer SIT has campuses at each of Singapore’s polytechnics, and a
dedicated campus at Dover.

The chatbot will start without any knowledge of any entities, but can learn about them by asking the
user. If someone asks it a question for which it does not know the answer, the chatbot will print I don’t
know followed by the question. The user may then type in answer. If the user types an answer, the
chatbot will thereafter user this answer. If the user simply presses ‘enter’ without typing anything, the
chatbot will ignore the response. In either case, the chatbot will then go back to waiting for more
questions.

Once the chatbot has learned some entities, they can be saved to disk using the SAVE intent, and
recalled using the LOAD intent. The RESET intent will erase all of the chatbot’s knowledge, leaving
only the smalltalk in memory (but it will not erase any of the files created by SAVE, so that they can
be re-loaded later).

The LOAD intent should append all of the entities and responses in the file to whatever entities and
responses already exist in the chatbot’s memory. If an entity in the file is the same as one that is already
in memory, the corresponding response from the file should replace the response currently in memory.